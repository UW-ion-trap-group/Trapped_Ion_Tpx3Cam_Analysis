import numpy as np
import scipy
import scipy.optimize
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.colors as mcolors
from mpl_toolkits import mplot3d
import glob
import time
import pandas as pd
import math

plt.rcParams["figure.figsize"] = (3,3)


class Ion:
    def __init__(self, n, x, y, r0, color, data, debugPrinting=False):
        self.n = n # Ion number (left to right)
        self.x = x # x-position
        self.y = y # y-position
        self.r0 = r0 # radius
        self.color = color # display color
        self.data = data # Dataframe used 
        self.debugPrinting = debugPrinting
        
        self.threshold = [] # differentiator between bright/dark states by 'dt' between events in ROI
        
        self.bright = [] # stores data for only bright events
        self.dark = [] # stores data for only dark events
        
        self.transpts = []  # Transition points (index number)
        # DtB = dark to bright
        # BtD = bright to dark
        self.DtB = []
        self.BtD = []
        
        # 
        self.pretransition = [] # not sure
        self.leadArray = []  # array of arrays. Each value is the index of the points before a transition
        self.leadIndices = [] # ^ original point in leadArray that is used to call the point of transition
        self.hasoutliers = [] # not sure
        
        
        ### Display Ion within Region of Interest (ROI) ###
    def show_ion(self): 
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(6, 2.5))

        xbounds = (self.data['x'].min(), self.data['x'].max())
        ybounds = (self.data['y'].min(), self.data['y'].max())
        xbins = int(self.data['x'].max()-self.data['x'].min()+1)
        ybins = int(self.data['y'].max()-self.data['y'].min()+1)
        # create 2D histogram of ROI with proper binning and range
        h = ax0.hist2d(self.data['x'], self.data['y'], bins=(xbins, ybins), range=[xbounds, ybounds])
        fig.colorbar(h[3], ax = ax0)

        # create the same plot on a log-scale
        h = ax1.hist2d(self.data['x'], self.data['y'], bins=(xbins, ybins), range=[xbounds, ybounds], norm=mpl.colors.LogNorm())
        fig.colorbar(h[3], ax = ax1)
        fig.suptitle(f'Ion {self.n}')
        fig.tight_layout()
        plt.show()
        
        ### Display Ion after post processing of position data ### (must include centroided data in Dataframe)
    def show_ion_centroided(self):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(6, 2.5))

        h = ax0.hist2d(self.data['xc'], self.data['yc'], bins=int(2*self.r0), range=[(self.x-self.r0, self.x+self.r0), (self.y-self.r0, self.y+self.r0)])
        fig.colorbar(h[3], ax = ax0)

        h = ax1.hist2d(self.data['xc'], self.data['yc'], bins=(2*self.r0), range=[(self.x-self.r0, self.x+self.r0), (self.y-self.r0, self.y+self.r0)], norm=mpl.colors.LogNorm())
        fig.colorbar(h[3], ax = ax1)
        fig.tight_layout()
        plt.show()
        

        ### plot histogram of x values in ROI ### (should be ~gaussian)
    def xhistogram(self, bins):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        
        xbounds = (self.data['x'].min(), self.data['x'].max())
        xbins = int(self.data['x'].max()-self.data['x'].min()+1)
        fig, ax0 = plt.subplots(ncols=1, figsize=(5, 3))
        plt.hist(self.data['x'], bins=(xbins), range=xbounds, color = 'r', ec = 'k')
        plt.xlabel('x-value',fontsize = 12)
        plt.ylabel('counts',fontsize = 12)
        plt.title(f'Ion {self.n}')
        plt.show()
        
        hist_x, bins_x = np.histogram(self.data['x'], xbins, xbounds) #, density=True),
        bin_centres_x = (bins_x[:-1] + bins_x[1:])/2
        xguess_mean = (self.x)
        xguess_sigma = 1
        xguess_amp = hist_x.max()
        xguess_c = hist_x.max()/10
        xguess  = np.array([xguess_mean,xguess_sigma,xguess_amp,xguess_c])
        popt_x, pcov_x = scipy.optimize.curve_fit(Gaussian, bin_centres_x, hist_x, p0=xguess, maxfev = 50000)
        print(popt_x[0], popt_x[1])
        
        
        ### plot histogram of y values in ROI ### (should be ~gaussian)
    def yhistogram(self, bins):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        
        ybounds = (self.data['y'].min(), self.data['y'].max())
        ybins = int(self.data['y'].max()-self.data['y'].min()+1)
        fig, ax0 = plt.subplots(ncols=1, figsize=(5, 3))
        plt.hist(self.data['y'], bins=ybins, range = ybounds, color = 'r', ec = 'k')
        plt.xlabel('y-value',fontsize = 12)
        plt.ylabel('counts',fontsize = 12)
        plt.title(f'Ion {self.n}')
        plt.show()
        
        hist_x, bins_x = np.histogram(self.data['y'], ybins, ybounds) #, density=True),
        bin_centres_x = (bins_x[:-1] + bins_x[1:])/2
        xguess_mean = (self.y)
        xguess_sigma = 1
        xguess_amp = hist_x.max()
        xguess_c = hist_x.max()/10
        xguess  = np.array([xguess_mean,xguess_sigma,xguess_amp,xguess_c])
        popt_x, pcov_x = scipy.optimize.curve_fit(Gaussian, bin_centres_x, hist_x, p0=xguess, maxfev = 50000)
        print(popt_x[0], popt_x[1])
        
        
        ### plot histogram of radius density values in ROI ### (should be half of a ~gaussian distribution)
    def rhistogram(self, bins):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        r = (((self.data['x']-(self.x))**2 + (self.data['y']-(self.y))**2)**(1/2))
        hist, bin_edges = np.histogram(r, range=(0,self.r0), bins=bins, density=True)
        bin_centres = (bin_edges[:-1] + bin_edges[1:])/2
        fig, ax0 = plt.subplots(1, 1, figsize=(5, 3))
        ax0.scatter(bin_centres, hist/(np.pi*(bin_centres**2-(bin_centres-(self.r0/bins))**2)), label=f'{self.n} radial density',s=150/bins)
        ax0.legend()
        
       ### plot histogram of the time-over-threshold of the center pixel of hits in the ROI ### (can be changed to 'cluster flux' if desired)
    def flux_histogram(self):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        fig, ax0 = plt.subplots(ncols=1, figsize=(5, 4))
        ax0.hist(self.data['center flux'], bins = 100, range=(0,5000), color = 'r', ec = 'k', label=f'{self.n}')
        ax0.set_title("Center Flux", fontsize = 12) # change the title
        ax0.set_xlabel('TOT(ns)',fontsize = 12)
        ax0.set_ylabel('counts',fontsize = 12)
        
        ### Mulitple plots of flux that can be stacked to compare ### (requires building the figure in a different cell)
    def flux_histogram_stackable(self):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        hist, bin_edges = np.histogram(self.data['center flux'], range=(0,5000), bins=100, density=True)
        bin_centres = (bin_edges[:-1] + bin_edges[1:])/2
        plt.plot(bin_centres, hist/hist.max(), color=self.color, label=f'{self.n}', lw=1); plt.legend(); 
        plt.ylabel('counts'); plt.xlabel('ToT(ns)')
                
        
        ### Plots histogram of how many events occured durring sets of time ### (must define time frame and duration)
    def fluorescence_histogram(self, start, duration, bins):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        used_data = (self.data
                     .query(f"{start} < time < {start+duration}")
                           )
        fig, ax = plt.subplots(1, 1, figsize=(8, .75))
        ax.hist(used_data['time'], bins = bins)
        ax.set_ylabel(f'{self.n}')
        
        
#_______### Begin Jumps Analysis ###_______________________________________________________________________________________
        
    
        ### Determines the Bright/Dark state threshold for time between photon hits in the ROI by statistical value sigma ###
    def auto_threshold(self, sigma=2, uncertainty_control = True): 
        
        # if the specified ion does not exist in the data set being analyzed, return a statement saying so. 
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        
        #Begin making plots of 'dt' histograms and their best fit match to an exponential distribution.
        from choose_file import filename
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (11, 3))
        bin_heights, bin_borders, _ = ax1.hist(self.data['dt'], bins = 'auto', range = (0, .05), alpha = .5, label='\'dt\' pdf', density = True)
        bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
        popt, pcov = curve_fit(expon, bin_centers, bin_heights, p0=[1/5e-4, bin_heights.max()])  # fits the histogram to exponential. Input parameters 
                                                                                 # for a specific data set but they seem to be pretty
                                                                                 # applicable to all datasets. 

        x_interval_for_fit = np.linspace(bin_centers[0], bin_centers[-1], 10000)       # define x values for fit
        ax1.plot(x_interval_for_fit, expon(x_interval_for_fit, *popt), label='fit')    # plot exponential fit on top of histogram
        ax1.set_yscale('log')                                                          # Display parameters 
        ax1.set_title(f'{filename} Ion #{self.n}')
        ax1.set_ylabel(f'Probability (log-base)');
        ax1.set_xlabel(f'Time between events in ROI (s)')
        
        # This part determines the theshold for the Bright/Dark state detection. Unless specified, the value 
        # will be set at the 2 sigma location based on fit params
        sigma_percent = stats.norm.cdf(sigma)                                                                # determine how much of the data should be used. %
        loc = 0; rate = popt[0] ; int_to = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / rate)        # turns percent into a number (threshold value)
        self.upper_limit = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / (rate-(pcov[0][0]**2)))
        self.lower_limit = stats.expon.ppf((sigma_percent), loc=loc, scale= 1 / (rate+(pcov[0][0]**2)))
        d = stats.expon.rvs(loc = loc, scale = rate, size = 10000)                                          # create random variables that follow the fit (for plotting)
        base = np.linspace(0,int_to,100000)
        ax1.plot(base,stats.expon.pdf(base,loc = loc, scale = 1 / rate), 'r', linewidth = 2,alpha = 0.4)     
        int_base1 = np.linspace(0,int_to,10000)                                                      #(below) plot a shaded region that displays the bright state values
        ax1.fill_between(int_base1, stats.expon.pdf(int_base1,loc = loc, scale = 1 / rate), color = 'b', linewidth = 0, alpha = .3, label = 'Bright')
        ax1.set_xlim(0, 2*int_to)
        ax1.legend()
        
        if uncertainty_control:
            ax1.axvline(self.lower_limit)
            ax1.axvline(self.upper_limit)

        
        #Print statements that tell you about the threshold and the fit parameters etc. 
        prob = 1 - stats.expon.cdf(int_to, loc=loc, scale= 1 / rate)
        z = (stats.norm.ppf(1-(prob)))
        #print(f'Ion {self.n} threshold: {int_to:.2e}(s)' )
        #print(f'Fit Parameters: [rate (lambda) = {popt[0]:.3e}] || [multiplier = {popt[1]:.3e}] \n')
        
        #Plot everything on a non-log base y-scale. 
        ax2.hist(self.data['dt'], bins = 'auto', range = (0, .05), alpha = .5, label='\'dt\' pdf', density = True)
        ax2.plot(x_interval_for_fit, expon(x_interval_for_fit, *popt), label='fit')
        ax2.set_title(f'{filename} Ion #{self.n}')
        ax2.set_ylabel(f'Probability')
        ax2.set_xlabel(f'Time between events in ROI (s)')
        ax2.plot(base,stats.expon.pdf(base,loc = loc, scale = 1 / rate), 'r', linewidth = 2,alpha = 0.4)
        ax2.fill_between(int_base1, stats.expon.pdf(int_base1,loc = loc, scale = 1 / rate), color = 'b', linewidth = 0, alpha = .3, label = 'Bright')
        ax2.set_ylim(0,bin_heights.max()*1.05)
        ax2.set_xlim(0, 2*int_to)
        ax2.legend()
        fig.tight_layout()
                        
        self.threshold = int_to
    
    
        
        ### sort the events into Bright/Dark states by referencing the time since the last event ###
    def sortbythreshold(self, uncertainty_control = True):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        
        if uncertainty_control:
            # simple sorting method which sorts data based on the length of pause between events
            self.bright = self.data.query(f'dt < {self.lower_limit}')
            self.dark = self.data.query(f'dt > {self.upper_limit}')
            self.uncertain_state = self.data.query(f'{self.lower_limit} <= dt <= {self.upper_limit}')
        
            for i in self.uncertain_state['index']:
                if i-1 in self.bright['index'] and i+1 in self.bright['index']:
                    self.bright = self.bright.append(self.uncertain_state.loc[[i]])
                elif i-1 in self.dark['index'] and i+1 in self.dark['index']:
                    self.dark = self.dark.append(self.uncertain_state.loc[[i]])
                elif i-1 in self.bright['index'] and i+1 in self.dark['index']:
                    self.bright = self.bright.append(self.uncertain_state.loc[[i]])
                elif i-1 in self.dark['index'] and i+1 in self.bright['index']:
                    self.dark = self.dark.append(self.uncertain_state.loc[[i]])
                elif i-1 in self.bright['index']:
                    self.bright = self.bright.append(self.uncertain_state.loc[[i]])
                else:
                    self.dark = self.dark.append(self.uncertain_state.loc[[i]])
                
            self.bright = self.bright.sort_values('time')
            self.dark = self.dark.sort_values('time')
        
        else: 
            self.bright = self.data.query(f'dt < {self.threshold}')
            self.dark = self.data.query(f'dt > {self.threshold}')

            
        #print(f'Bright events (#/%): {len(self.bright)} / {len(self.bright)/len(self.data)*100:.2f}% \n')
        b_or_d = []
        for i in self.data['index']:
            if self.data.at[i, 'dt'] <= self.threshold:
                b_or_d.append(1)
            else:
                b_or_d.append(-1)
        self.data['B/D'] = b_or_d
        
        
        ### plots histogram of 'dt' values separately for Bright/Dark states ### (upperbound made to eliminate regions of extremely long dark states)
    def stateHistograms(self, upperbound=0):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        # plots a histogram of time between events for both states
        # optional parameter sets an upper limit on the x axis of the histograms
        
        if upperbound > 0:
            dark = self.dark.query(f' dt <= upperbound')
            shortdTimeD = dark['dt']
            bright = self.bright.query(f' dt <= upperbound')
            shortdTimeB = bright['dt']

        fig, (ax01, ax11) = plt.subplots(ncols=2, figsize=(12, 4))

        if upperbound > 0:
            h = ax01.hist(shortdTimeB, bins=100, alpha=1, histtype='step', ec='blue', stacked=True)
            ax01.set_title("Time between events while in bright state (s)")
            ax01.set_xlabel("Time between events (s)")
            ax01.set_ylabel("Counts")
            ax01.tick_params(axis='x', labelrotation=45)
            ax01.set_yscale('log')

            h = ax11.hist(shortdTimeD, bins=100, alpha=1, histtype='step', ec='blue', stacked=True)
            ax11.set_title("Time between events while in dark state (s)")
            ax11.set_xlabel("Time between events (s)")
            ax11.set_ylabel("Counts")
            ax11.tick_params(axis='x', labelrotation=45)
            ax11.set_yscale('log')

            plt.show()
            
        if upperbound == 0:
            h = ax01.hist(self.bright['dt'], bins=100, alpha=1, histtype='step', ec='blue', stacked=True)
            ax01.set_title("Time between events while in bright state (s)")
            ax01.set_xlabel("Time between events (s)")
            ax01.set_ylabel("Counts")
            ax01.tick_params(axis='x', labelrotation=45)
            ax01.set_yscale('log')


            h = ax11.hist(self.dark['dt'], bins=100, alpha=1, histtype='step', ec='blue', stacked=True)
            ax11.set_title("Time between events while in dark state (s)")
            ax11.set_xlabel("Time between events (s)")
            ax11.set_ylabel("Counts")
            ax11.tick_params(axis='x', labelrotation=45)
            ax11.set_yscale('log')

            plt.show()
            
        ### Locate and save the locations that BtD and DtB transitions occur ###
    def transitions(self, single_photon_control = True):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        # identifies points where quantum jumps happen
        # using list comprehension
        misscount = 0
        self.transpts.clear()
        for i in range(len(self.data)) :
            if i not in self.bright['index']:
                misscount = misscount + 1
                if misscount == 1:
                    self.transpts.append(i)
            if i in self.bright['index'] and misscount >= 1:
                misscount = 0
                self.transpts.append(i)
        
        if single_photon_control:
            false_trans = []
            for i in range(0, len(self.transpts)):
                if self.transpts[i]+1 in self.transpts and self.transpts[i] in self.transpts and self.transpts[i+1] in self.dark['index']:
                    false_trans.append(self.transpts[i])
                    false_trans.append(self.transpts[i]+1)
            false_trans = list(set(false_trans))       
            for i in range(len(false_trans)):
                self.transpts.remove(false_trans[i])
                
                
        # DtB = dark to bright
        # BtD = bright to dark
        self.DtB.clear()
        self.BtD.clear()
        for i in range(len(self.transpts)):
            if self.transpts[i] in self.bright['index']:
                self.DtB.append(self.transpts[i])
            else:
                self.BtD.append(self.transpts[i])
                
        ### This functions finds the time between the events ('points') before a BtD transition,
        #  averages each 'point' and plots what can be referred to as an 'average transition' ###
        
        
    def setup(self, sigma=2, uncertainty_control = True, single_photon_control = False):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        
        self.auto_threshold(sigma, uncertainty_control)
        self.sortbythreshold(uncertainty_control)
        self.transitions(single_photon_control)
        
        
        
    def leadup(self, points, setthresh=False, showdark=False,  outliers=True):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        # The main mechanism for averaging every leadup to a quantum jump
        # optional parameters: 
        #     showdark: plots the average dark state time between photon events if True
        #     outliers: removes statistical outliers if false
        
        if setthresh==True and outliers==False:
            print("You picked two outlier removal options, put one back")
            return 0
        leadIndex = []
        points = points+1
        # iterate through bright-to-dark transitions
        # and record the index of the five events before each transition
        # stopping if another transition is encountered
        for i in range(len(self.BtD)):
            holding = []
            if self.BtD[i] < points:
                continue

            for j in range(1,points):
                if self.BtD[i]-j in self.transpts:
                    break
                holding.append(self.BtD[i] - j)
            leadIndex.append(holding.copy())
        self.leadIndices = leadIndex[:]
        
        # replace each item in that index with the value it represents
        if setthresh == True:
            for i in range(len(leadIndex)):
                for w in range(0, len(leadIndex[i])):
                    if self.data.at[leadIndex[i][w], 'dt'] <= self.threshold:
                        leadIndex[i][w] = self.data.at[leadIndex[i][w], 'dt']
        else:
            for i in range(len(leadIndex)):
                for w in range(0, len(leadIndex[i])):
                    leadIndex[i][w] = self.data.at[leadIndex[i][w], 'dt'] 
        
        self.leadArray = leadIndex.copy()
                        
        avgs = []
        for i in range(1,points):
            avgs.append([])
        for k in range(len(leadIndex)):
            for j in range(len(leadIndex[k])):
                avgs[j].append(leadIndex[k][j])
        self.pretransition = avgs.copy()
        
        if outliers==False:
            hitlist = list(itertools.chain.from_iterable(self.idOutliers(avgs)))
            temp = []
            for i in range(len(leadIndex)):
                if i not in hitlist:
                    temp.append(leadIndex[i])
            
            leadIndex = temp.copy()
        
        finalpoints = []
        dev = []
        for j in range(len(avgs)):
            finalpoints.append(np.average(avgs[j]))
            dev.append(np.std(avgs[j]))
        finalpoints = np.flip(finalpoints)
        print("Averages:", finalpoints, "\n")
        dev = np.flip(dev)

        themscountinwords = np.arange(len(finalpoints))
        errors = []
        for i in range(len(avgs)):
            errors.append(np.std(avgs[i])/np.sqrt(len(avgs[i])))
        errors = np.flip(errors)
        
        # Bright state average
        if outliers == False:
            overaverage = self.NoOutlierAvg()
            erroroveraverage = np.std(self.dtimeBout)/np.sqrt(len(self.dtimeBout))
            print("Average (no outliers)", overaverage, "\n")

        else:
            overaverage = np.average(self.bright['dt'])
            erroroveraverage = np.std(self.bright['dt'])/np.sqrt(len(self.bright['dt']))
            print("Standard Deviation with No Alteration:", np.std(self.bright['dt']), "\n")
            print("Average (unaltered)", overaverage, "\n")
        
        # Dark state average
        darkavg = np.average(self.dark['dt'])
        darkavgerr = np.std(self.dark['dt'])/np.sqrt(len(self.dark['dt']))
        
        # Plotting everything
        # The last photon before a bright->dark transition is represented by the rightmost point
        # The fifth-to-last is represented by the leftmost
        fig, ax = plt.subplots(1,1, figsize = (points**.75*.5, points**.5))
        ax.errorbar(themscountinwords, finalpoints, yerr=errors, fmt="bo")
        ax.axhline(overaverage, color='firebrick')
        ax.axhspan(overaverage-erroroveraverage, overaverage+erroroveraverage, alpha=0.5, color='lightpink')
        if showdark:
            ax.axhline(darkavg, color='darkblue')
            ax.axhspan(darkavg-darkavgerr, darkavg+darkavgerr, alpha=0.3, color='cornflowerblue')
        ax.set_title("Bright->Dark transition")
        ax.set_xlabel("Event #")
        ax.set_ylabel("Time since last event (s)")
        plt.show()
        
        
    def visRange(self, start, duration):
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        # plots a small slice of data 
        # and uses red/blue color coding to distinguish between the bright and dark state
        # useful for visualizing the effects of different sorting methods
        end = start+duration
        use = self.data.query(f'{start} <= time < {end}')
        index = np.arange(int(min(use['index'])), int(max(use['index'])))
        change = use['dt']
        linehere = []
        for j in index:
            if j in self.transpts:
                linehere.append(j)
        plt.figure(figsize=(15, 1.5))
        counting = use['time']
        plt.scatter(counting, change)
        plt.title("Visual representation of ion states")
        plt.xlabel("Event #")
        plt.ylabel("Time since last event (s)")
        plt.ylim(-self.threshold,10*self.threshold)

        if linehere != []:
            
            if index[0] in self.dark['index']:
                if index[0] in self.transpts:
                    plt.axvspan(self.data.at[index[0], 'time'], self.data.at[linehere[0], 'time'], alpha=0.3, color='blue')
                    plt.axvspan(start, self.data.at[index[0], 'time'], alpha=0.3, color='red')
                else:
                    plt.axvspan(start, self.data.at[linehere[0], 'time'], alpha=0.3, color='blue')
            if index[0] in self.bright['index']:
                if index[0] in self.transpts:
                    plt.axvspan(self.data.at[index[0], 'time'], self.data.at[linehere[0], 'time'], alpha=0.3, color='red')
                    plt.axvspan(start, self.data.at[index[0], 'time'], alpha=0.3, color='blue')
                else:
                    plt.axvspan(start, self.data.at[linehere[0], 'time'], alpha=0.3, color='red')

            if index[-1] in self.bright['index']:            
                plt.axvspan(self.data.at[linehere[-1], 'time'], end, alpha=0.3, color='red')
            if index[-1] in self.dark['index']:
                plt.axvspan(self.data.at[linehere[-1], 'time'], end, alpha=0.3, color='blue')
                
            for i in range(len(linehere)):
                plt.axvline(x=linehere[i])
            for i in range(len(linehere) - 1):
                if linehere[i] in self.DtB:
                    plt.axvspan(self.data.at[linehere[i], 'time'], self.data.at[linehere[i+1], 'time'], alpha=0.3, color='red')
                if linehere[i] in self.BtD:
                    plt.axvspan(self.data.at[linehere[i], 'time'], self.data.at[linehere[i+1], 'time'], alpha=0.3, color='blue')
            
            
        if linehere == []:
            if len(use) == (0 or 1):
                print(f'Ion {self.n} had {len(use)} hits during this time')
                plt.axvspan(start, end, alpha=0.3, color='blue')
            else:
                if index[0] in self.dark['index']:
                    plt.axvspan(self.data.at[index[0], 'time'], self.data.at[index[-1], 'time'], alpha=0.3, color='blue')
                else:
                    plt.axvspan(self.data.at[index[0], 'time'], self.data.at[index[-1], 'time'], alpha=0.3, color='red')
            plt.axvspan(self.data.at[index[-1], 'time'], end, alpha=0.3, color='blue')
            plt.axvspan(start, self.data.at[index[0], 'time'], alpha=0.3, color='blue')
            
        plt.xlim(start,end) 
        plt.axhline(self.threshold)
        plt.axhline(self.lower_limit)
        plt.axhline(self.upper_limit)
        plt.show()
        
        
        ###  Plots and fits bright state duration statistics as an exponential ###
    def duration_statistics(self, log=False):  # a log base can be used if log=True is plugged in when calling the function
        if type(self.color) == int:
            print(f'Ion {self.n} does not exist.')
            return
        
        # Transition points determined in Ion_functions.setup() 
        # Append the length between state transitions to the corresponding state the ion was in. 
        Bduration = []
        Dduration = []
        for i in range(0, len(self.BtD)-1):    #This just decides which state the function should start in. 
                                                #If the first transition is DtB then the first length is in the dark state.
            if self.BtD[0] < self.DtB[0]:
                Dduration.append(self.data.at[self.transpts[2*i+1], 'time'] - self.data.at[self.transpts[2*i], 'time'])
                Bduration.append(self.data.at[self.transpts[2*i+2], 'time'] - self.data.at[self.transpts[2*i+1], 'time'])
            else:
                Bduration.append(self.transpts[2*i+1] - self.transpts[2*i])
                Dduration.append(self.transpts[2*i+2] - self.transpts[2*i+1])

        # Plot the histogram of Bright state duration times along with its exponential fit. 
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 3))
        bin_heights, bin_borders, _ = ax1.hist(Bduration, bins= 50, alpha = .7, label='\'dt\' pdf', range = [0,.2], density = True)
        bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
        #popt, pcov = scipy.optimize.curve_fit(Superradiance, bin_centers, bin_heights, p0 = [15, 1.5])
        #popt, _ = curve_fit(expon, bin_centers, bin_heights, p0=[1/.02, 20])
        #print(f'Decay parameter: {1/popt[0]:.4f} (s)')
        #x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
        #ax1.plot(x_interval_for_fit, expon(x_interval_for_fit, *popt), label='fit')
        #ax1.plot(x_interval_for_fit, Superradiance(x_interval_for_fit, *popt), label='fit')
        ax1.set_xlabel('Time (s)')
        ax1.set_title('Bright State Duration')
        if log==False:
            ax1.set_ylabel('Probability Density')
        else:
            ax1.set_yscale('log')
            ax1.set_ylabel('Probability Density (log base)')
            
        # Plot the histogram of Dark state duration times along with its exponential fit. 
        bin_heights, bin_borders, _ = ax2.hist(Dduration, bins= 50, alpha = .7, label='\'dt\' pdf', range = [0,.2], density = True)
        bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
        bin_centers = np.array(bin_centers)
        bin_heights = np.array(bin_heights)
        centers = []
        heights = []
        for i in range(len(bin_centers)):
            centers.append(bin_centers[i])
            heights.append(bin_heights[i])
        index = []
        for i in range(len(centers)):
            if centers[1] < self.threshold:
                centers.pop(1)
                heights.pop(1)
        bin_centers = centers
        bin_heights = heights
                
        #popt, _ = curve_fit(expon, bin_centers, bin_heights, p0=[1/.02, 20])
        #print(f'Decay parameter: {1/popt[0]:.4f} (s)')
        x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
        #ax2.plot(x_interval_for_fit, expon(x_interval_for_fit, *popt), label='fit')
        ax2.set_xlabel('Time (s)')
        ax2.set_title('Dark State Duration')
        if log==False:
            ax2.set_ylabel('Probability Density')
        else:
            ax2.set_yscale('log')
            ax2.set_ylabel('Probability Density (log base)')


        #bin_heights, bin_borders, _ = ax2.hist(Dduration-self.threshold, bins= 100, alpha = .7, label='\'dt\' pdf', range = [0,.4], density = True)
        #bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
        #popt, _ = curve_fit(expon, bin_centers, bin_heights, p0=[1/.05, 150])

        #x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)
        #ax2.plot(x_interval_for_fit, expon(x_interval_for_fit, *popt), label='fit')
        #ax2.set_yscale('log')
        #print(1/popt[0])
        
#____________________________________________________________________________________________________________________________________________________        
##### EQUATIONS #####


def expon(x, rate, multiplier):   # in scipy.stats.expon() the paramater 'scale = 1 / rate' when inputing the function
    return multiplier * np.exp(-rate * x)

def Lorentzian(x, x0, a, gam, b):
    return b + a * gam**2 / ( gam**2 + ( x - x0 )**2)

def Double_Lorentzian(x, x1, a1, gam1, b1, x2, a2, gam2):
    return b1 + a1 * gam1**2 / ( gam1**2 + ( x - x1 )**2) + a2 * gam2**2 / ( gam2**2 + ( x - x2 )**2)

def Linear(x, m, b):
    return m*x + b

def Oscillation(x, A, B, phase):
    return A + np.abs(B) *np.sin(2*np.pi*(x)/54.789717 + phase)

def Gaussian(x, xm, sigma, A, c):
    return np.absolute(A)*np.exp(-np.power((x-xm)/sigma,2)/2) + c

def Rscatt_(t, d, b, p, m):
    S = 2
    G = 20.4e6
    O = 1 / 54.789717e-9  * np.pi*2
    D = d - np.abs(b)*O*np.cos(O*10**-9*t +p)
    R = m*((G/2)**2/ (np.sqrt(1+S)*(G/2)**2 + (D)**2))
    return R

def Rscatt_high(t, m, S, d, v, p):
    G = 20.4e6 * (1+S)**.5 #Natural Linewidth
    O = np.pi * 2 / 54.789717e-9 #Driving Frequency
    k = np.pi * 2 / (3e8/(3e8/493e-9 + d)) #Wave number 
    D = d + k*v*np.sin(O*10**-9*t +p)*np.cos(np.pi/4) #Detuning
    R = m*(G/2) * (S) / ((S + 1) + (4 * (D / G)**2)) #Scattering rate
    return R

def Superradiance(t, G, A):
    prob = A * (1+4*G*t)*2*G*np.e**(-2*G*t)
    return prob
    
    
def find_nearest(array,value):
    idx = np.searchsorted(array, value, side="left")
    if idx > 0 and (idx == len(array) or math.fabs(value - array[idx-1]) < math.fabs(value - array[idx])):
        return array[idx-1]
    else:
        return array[idx]



