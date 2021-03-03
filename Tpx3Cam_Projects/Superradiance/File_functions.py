import numpy as np
import scipy
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.colors as mcolors
from mpl_toolkits import mplot3d
import glob
import pandas as pd
import math
import Ion_functions as func
from Ion_functions import Ion
import choose_file
import os

plt.rcParams["figure.figsize"] = (3,3)

global ion_1   
global ion_2   
global ion_3   
global ion_4
global ion_5   
global ion_6   
global ion_7   
global ion_8   
global Ion_1   
global Ion_2   
global Ion_3   
global Ion_4   
global Ion_5   
global Ion_6   


def show_duration(filename):
    it = pd.read_csv(filename)  
    it = it.drop(columns = {'Unnamed: 0'})
    
    fig, (ax0) = plt.subplots(ncols=1, figsize=(2,6))
    fig.suptitle(filename)
    h = ax0.hist2d(it['x'], it['time'], bins = [256, 200])
    ax0.set_xlabel('x position')
    ax0.set_ylabel('Time (ns)')
    
def duration_summary_now():  #uses whatever variables have been designated in Jupyter environment 

    sigma = 2
    single_photon = False
    
    ions = [ion_1, ion_2, ion_3, ion_4, ion_5, ion_6]
    bins = 25; num = 6
    total_bin_heights = np.zeros(bins)
    total_bin_centers = np.zeros(bins)
    real_heights = np.zeros(bins)
        
    for ion in ions:
            
        if type(ion.color) == int:
            print(f'Ion {ion.n} does not exist.')
            num -= 1
            continue
            
        else:
            from choose_file import filename
            bin_heights, bin_borders = np.histogram(ion.data['dt'], bins = 'auto', range = (0, .05), density = True)
            bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
            popt, pcov = curve_fit(func.expon, bin_centers, bin_heights, p0=[1/5e-4, bin_heights.max()])  # fits the histogram to exponential. Input parameters 
            
            # This part determines the theshold for the Bright/Dark state detection. Unless specified, the value 
            # will be set at the 2 sigma location based on fit params
            sigma_percent = stats.norm.cdf(sigma)                                                                # determine how much of the data should be used. %
            loc = 0; rate = popt[0] ; int_to = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / rate)        # turns percent into a number (threshold value)
            ion.upper_limit = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / (rate-(pcov[0][0]**2)))
            ion.lower_limit = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / (rate+(pcov[0][0]**2)))
            d = stats.expon.rvs(loc = loc, scale = rate, size = 10000)                                          # create random variables that follow the fit (for plotting)
                            
            ion.threshold = int_to
        
        
            
            # simple sorting method which sorts data based on the length of pause between events
            ion.bright = ion.data.query(f'dt < {ion.lower_limit}')
            ion.dark = ion.data.query(f'dt > {ion.upper_limit}')
            ion.uncertain_state = ion.data.query(f'{ion.lower_limit} <= dt <= {ion.upper_limit}')
        
            for i in ion.uncertain_state['index']:
                if i-1 in ion.bright['index'] and i+1 in ion.bright['index']:
                    ion.bright = ion.bright.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.dark['index'] and i+1 in ion.dark['index']:
                    ion.dark = ion.dark.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.bright['index'] and i+1 in ion.dark['index']:
                    ion.bright = ion.bright.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.dark['index'] and i+1 in ion.bright['index']:
                    ion.dark = ion.dark.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.bright['index']:
                    ion.bright = ion.bright.append(ion.uncertain_state.loc[[i]])
                else:
                    ion.dark = ion.dark.append(ion.uncertain_state.loc[[i]])
                
            ion.bright = ion.bright.sort_values('time')
            ion.dark = ion.dark.sort_values('time')

            
            b_or_d = []
            for i in ion.data['index']:
                if ion.data.at[i, 'dt'] <= ion.threshold:
                    b_or_d.append(1)
                else:
                    b_or_d.append(-1)
            ion.data['B/D'] = b_or_d
        
        
            ### plots histogram of 'dt' values separately for Bright/Dark states ### (upperbound made to eliminate regions of extremely long dark states)
            
            # identifies points where quantum jumps happen
            # using list comprehension
            misscount = 0
            ion.transpts.clear()
            for i in range(len(ion.data)) :
                if i not in ion.bright['index']:
                    misscount = misscount + 1
                    if misscount == 1:
                        ion.transpts.append(i)
                if i in ion.bright['index'] and misscount >= 1:
                    misscount = 0
                    ion.transpts.append(i)
            
                    
                    
            # DtB = dark to bright
            # BtD = bright to dark
            ion.DtB.clear()
            ion.BtD.clear()
            for i in range(len(ion.transpts)):
                if ion.transpts[i] in ion.bright['index']:
                    ion.DtB.append(ion.transpts[i])
                else:
                    ion.BtD.append(ion.transpts[i])
                    
            ### This functions finds the time between the events ('points') before a BtD transition,
            #  averages each 'point' and plots what can be referred to as an 'average transition' ###
            
            # Transition points determined in Ion_functions.setup() 
            # Append the length between state transitions to the corresponding state the ion was in. 
            Bduration = []
            Dduration = []
            for i in range(0, len(ion.BtD)-1):    #This just decides which state the function should start in. 
                                                    #If the first transition is DtB then the first length is in the dark state.
                if ion.BtD[0] < ion.DtB[0]:
                    Dduration.append(ion.data.at[ion.transpts[2*i+1], 'time'] - ion.data.at[ion.transpts[2*i], 'time'])
                    Bduration.append(ion.data.at[ion.transpts[2*i+2], 'time'] - ion.data.at[ion.transpts[2*i+1], 'time'])
                else:
                    Bduration.append(ion.transpts[2*i+1] - ion.transpts[2*i])
                    Dduration.append(ion.transpts[2*i+2] - ion.transpts[2*i+1])
    
            # Plot the histogram of Bright state duration times along with its exponential fit. 
            bin_heights, bin_borders = np.histogram(Bduration, bins = bins, range = [0,.2], density = True)
            real_heights, bin_borders = np.histogram(Bduration, bins = bins, range = [0,.2], density = False)
            bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
            
            total_bin_heights += bin_heights
            real_heights += real_heights
            total_bin_centers = bin_centers
            total_bin_errors = np.sqrt(real_heights)
            ratio = total_bin_heights[0] / real_heights[0]
            
        return total_bin_centers, total_bin_heights/num, total_bin_errors/num*ratio
    
    

def duration_summary():  # uses the data from whatever choose_file.________ function is before it. 
    
    
    ion_1 = choose_file.ion_1
    ion_2 = choose_file.ion_2
    ion_3 = choose_file.ion_3
    ion_4 = choose_file.ion_4
    ion_5 = choose_file.ion_5
    ion_6 = choose_file.ion_6
    Ion_1 = choose_file.Ion_1
    Ion_2 = choose_file.Ion_2
    Ion_3 = choose_file.Ion_3
    Ion_4 = choose_file.Ion_4
    Ion_5 = choose_file.Ion_5
    Ion_6 = choose_file.Ion_6


    filename = choose_file.filename
    old_data_table = choose_file.old_data_table
    data_table = choose_file.data_table
 


    sigma = 2
    single_photon = False
    
    ions = [ion_1, ion_2, ion_3, ion_4, ion_5, ion_6]
    bins = 25; num = 6
    total_bin_heights = np.zeros(bins)
    total_bin_centers = np.zeros(bins)
    real_heights = np.zeros(bins)
        
    for ion in ions:
            
        if type(ion.color) == int:
            print(f'Ion {ion.n} does not exist.')
            num -= 1
            continue
            
        else:
            from choose_file import filename
            bin_heights, bin_borders = np.histogram(ion.data['dt'], bins = 'auto', range = (0, .05), density = True)
            bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
            popt, pcov = curve_fit(func.expon, bin_centers, bin_heights, p0=[1/5e-4, bin_heights.max()])  # fits the histogram to exponential. Input parameters 
            
            # This part determines the theshold for the Bright/Dark state detection. Unless specified, the value 
            # will be set at the 2 sigma location based on fit params
            sigma_percent = stats.norm.cdf(sigma)                                                                # determine how much of the data should be used. %
            loc = 0; rate = popt[0] ; int_to = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / rate)        # turns percent into a number (threshold value)
            ion.upper_limit = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / (rate-(pcov[0][0]**2)))
            ion.lower_limit = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / (rate+(pcov[0][0]**2)))
            d = stats.expon.rvs(loc = loc, scale = rate, size = 10000)                                          # create random variables that follow the fit (for plotting)
                            
            ion.threshold = int_to
        
        
            
            # simple sorting method which sorts data based on the length of pause between events
            ion.bright = ion.data.query(f'dt < {ion.lower_limit}')
            ion.dark = ion.data.query(f'dt > {ion.upper_limit}')
            ion.uncertain_state = ion.data.query(f'{ion.lower_limit} <= dt <= {ion.upper_limit}')
        
            for i in ion.uncertain_state['index']:
                if i-1 in ion.bright['index'] and i+1 in ion.bright['index']:
                    ion.bright = ion.bright.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.dark['index'] and i+1 in ion.dark['index']:
                    ion.dark = ion.dark.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.bright['index'] and i+1 in ion.dark['index']:
                    ion.bright = ion.bright.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.dark['index'] and i+1 in ion.bright['index']:
                    ion.dark = ion.dark.append(ion.uncertain_state.loc[[i]])
                elif i-1 in ion.bright['index']:
                    ion.bright = ion.bright.append(ion.uncertain_state.loc[[i]])
                else:
                    ion.dark = ion.dark.append(ion.uncertain_state.loc[[i]])
                
            ion.bright = ion.bright.sort_values('time')
            ion.dark = ion.dark.sort_values('time')

            
            b_or_d = []
            for i in ion.data['index']:
                if ion.data.at[i, 'dt'] <= ion.threshold:
                    b_or_d.append(1)
                else:
                    b_or_d.append(-1)
            ion.data['B/D'] = b_or_d
        
        
            ### plots histogram of 'dt' values separately for Bright/Dark states ### (upperbound made to eliminate regions of extremely long dark states)
            
            # identifies points where quantum jumps happen
            # using list comprehension
            misscount = 0
            ion.transpts.clear()
            for i in range(len(ion.data)) :
                if i not in ion.bright['index']:
                    misscount = misscount + 1
                    if misscount == 1:
                        ion.transpts.append(i)
                if i in ion.bright['index'] and misscount >= 1:
                    misscount = 0
                    ion.transpts.append(i)
            
                    
                    
            # DtB = dark to bright
            # BtD = bright to dark
            ion.DtB.clear()
            ion.BtD.clear()
            for i in range(len(ion.transpts)):
                if ion.transpts[i] in ion.bright['index']:
                    ion.DtB.append(ion.transpts[i])
                else:
                    ion.BtD.append(ion.transpts[i])
                    
            ### This functions finds the time between the events ('points') before a BtD transition,
            #  averages each 'point' and plots what can be referred to as an 'average transition' ###
            
            # Transition points determined in Ion_functions.setup() 
            # Append the length between state transitions to the corresponding state the ion was in. 
            Bduration = []
            Dduration = []
            for i in range(0, len(ion.BtD)-1):    #This just decides which state the function should start in. 
                                                    #If the first transition is DtB then the first length is in the dark state.
                if ion.BtD[0] < ion.DtB[0]:
                    Dduration.append(ion.data.at[ion.transpts[2*i+1], 'time'] - ion.data.at[ion.transpts[2*i], 'time'])
                    Bduration.append(ion.data.at[ion.transpts[2*i+2], 'time'] - ion.data.at[ion.transpts[2*i+1], 'time'])
                else:
                    Bduration.append(ion.transpts[2*i+1] - ion.transpts[2*i])
                    Dduration.append(ion.transpts[2*i+2] - ion.transpts[2*i+1])
    
            # Plot the histogram of Bright state duration times along with its exponential fit. 
            bin_heights, bin_borders = np.histogram(Bduration, bins = bins, range = [0,.2], density = True)
            real_heights, bin_borders = np.histogram(Bduration, bins = bins, range = [0,.2], density = False)
            bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
            
            total_bin_heights += bin_heights
            real_heights += real_heights
            total_bin_centers = bin_centers
            total_bin_errors = np.sqrt(real_heights)
            ratio = total_bin_heights[0] / real_heights[0]
            
        return total_bin_centers, total_bin_heights/num, total_bin_errors/num*ratio