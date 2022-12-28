import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Ion_functions
from Ion_functions import Ion
import math 
import io, os, sys, types


def Trans_1ion_x_389s():
    global x1; global y1;
    
    x1=47; y1=92
    
    global filename
    filename = 'x_389s_meta'
    
    One(x1,y1,filename)
    
def Trans_1ion_x_395s():
    global x1; global y1;
    
    x1=47; y1=92
    
    global filename
    filename = 'x_395s_meta'
    
    One()    

def Trans_9ions_296V_1():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=40; y1=84
    x2=46; y2=85
    x3=52; y3=84
    x4=57; y4=86
    x5=61; y5=84 #from 83
    x6=65; y6=86
    x7=70; y7=85
    x8=76; y8=85
    x9=82; y9=86
    global ROI
    ROI= [[40, 39], [46, 47], [52, 53], [57, 56], [61, 60], [65, 64], [70, 71], [75, 76], [82, 81]]
    global filename
    filename = '9ions/9ions_296V_2'
    
    Nine()
ROI= [[40, 39], [46, 47], [52, 51], [57, 56], [61, 60], [65, 64], [70, 71], [75, 76], [82, 81]]

def Trans_9ions_296V_2():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    """x1=40; y1=84    
    x2=47; y2=85
    x3=52; y3=84
    x4=57; y4=86
    x5=61; y5=84
    x6=65; y6=86
    x7=70; y7=85
    x8=76; y8=85
    x9=82; y9=86
    
    #ROI= [[40, 41], [47, 46], [52, 53], [57, 56], [61, 60], [65, 64], [70, 71], [75, 76], [82, 81]]
    """
    global ROI
    global filename
    filename = '9ions/9ions_296V_2'
    
    
    ROI= [[40, 39], [46, 47], [52, 51], [57, 56], [61, 60], [65, 64], [70, 71], [75, 76], [82, 81]]
    x1= 40; y1= 85
    x2= 46; y2= 84
    x3= 52; y3= 85
    x4= 57; y4= 84
    x5= 61; y5= 87
    x6= 65;y6= 84
    x7= 70; y7= 86
    x8= 75; y8= 85
    x9= 82; y9= 86
    
    Nine()

def Trans_9ions_296V_3():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=40; y1=85
    x2=46; y2=84
    x3=52; y3=85
    x4=57; y4=84
    x5=61; y5=87
    x6=65; y6=84
    x7=70; y7=86
    x8=75; y8=85
    x9=82; y9=86
    global ROI
    global filename
    filename = '9ions/9ions_296V_3'
    ROI= [[40, 39], [46, 47], [52, 51], [57, 56], [61, 60], [65, 64], [70, 71], [75, 76], [82, 81]]
    Nine()
  
def Trans_9ions_296V_4():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    """x1=40; y1=84
    x2=47; y2=85
    x3=52; y3=85
    x4=57; y4=86
    x5=61; y5=87
    x6=65; y6=86
    x7=70; y7=85
    x8=76; y8=85
    x9=82; y9=86"""

    global ROI
    global filename
    filename = '9ions/9ions_296V_4'
    
    ROI= [[40, 41], [47, 46], [52, 53], [57, 56], [61, 60], [65, 64], [70, 71], [76, 75], [82, 83]]
    x1= 40; y1= 84
    x2= 47; y2= 85
    x3= 52; y3= 85
    x4= 57; y4= 86
    x5= 61; y5= 87
    x6= 65; y6= 86
    x7= 70; y7= 85
    x8= 76; y8= 85
    x9= 82; y9= 86
    
    
    
    Nine()
 
def Trans_9ions_296V_5():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=40; y1=84
    x2=47; y2=85
    x3=52; y3=85
    x4=57; y4=86
    x5=61; y5=87
    x6=65; y6=86
    x7=70; y7=85
    x8=76; y8=85
    x9=82; y9=86
  
    global filename
    filename = '9ions/9ions_296V_5'
    
    Nine()

def Trans_9ions_296V_8():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;global x10;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9;global y10 
    
    global ROI
    global filename
    filename = '9ions/9ions_296V_8'
    
    x1=40; y1=85
    x2=47; y2=85
    x3=52; y3=85
    x4=57; y4=86
    x5=61; y5=84
    x6=65; y6=86
    x7=70; y7=85
    x8=76; y8=86
    x9=82; y9=86
    
    
    ROI= [[40, 41], [47, 46], [52, 53], [57, 56], [61, 60], [65, 66], [70, 71], [76, 75], [82, 83]]
     
    
    Nine()
    
def Trans_9ions_370V_1():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=85
    x3=52; y3=84
    x4=56; y4=86
    x5=60; y5=84
    x6=64; y6=86
    x7=68; y7=84
    x8=73; y8=86
    x9=79; y9=85
    
    global filename
    filename = '9ions/9ions_370V_1'
    
    Nine()

def Trans_9ions_370V_2():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=85
    x3=52; y3=85
    x4=56; y4=86
    x5=60; y5=84
    x6=64; y6=86
    x7=68; y7=85
    x8=73; y8=85
    x9=79; y9=85
    
    
    global filename
    filename = '9ions/9ions_370V_2'
    
    Nine()
 
def Trans_9ions_370V_3():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=85
    x2=47; y2=84
    x3=52; y3=86
    x4=56; y4=83
    x5=60; y5=86
    x6=64; y6=83
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=86
    
    
    global filename
    filename = '9ions/9ions_370V_3'
    
    Nine()
    
def Trans_9ions_370V_4():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=85
    x3=52; y3=84
    x4=56; y4=86
    x5=60; y5=84
    x6=64; y6=86
    x7=68; y7=85
    x8=73; y8=86
    x9=79; y9=86
    
    
    global filename
    filename = '9ions/9ions_370V_4'
    
    Nine()
    
def Trans_9ions_370V_5():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=84
    x3=52; y3=86
    x4=56; y4=83
    x5=60; y5=86
    x6=63; y6=84
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=85
    
 
    global filename
    filename = '9ions/9ions_370V_5'
    
    Nine()
def Trans_9ions_370V_6():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=85
    x2=47; y2=84
    x3=52; y3=86
    x4=56; y4=83
    x5=60; y5=86
    x6=63; y6=84
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=86
    
    
    global filename
    filename = '9ions/9ions_370V_6'
  
    Nine()
def Trans_9ions_370V_7():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=85
    x3=52; y3=86
    x4=56; y4=86
    x5=60; y5=86
    x6=64; y6=86
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=85
 
    
    global filename
    filename = '9ions/9ions_370V_7'
    
    Nine()
def Trans_9ions_370V_8():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=84
    x3=52; y3=86
    x4=56; y4=83
    x5=60; y5=86
    x6=64; y6=83
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=85

    
    global filename
    filename = '9ions/9ions_370V_8'
    
    Nine()
def Trans_9ions_370V_9():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=84
    x3=52; y3=86
    x4=56; y4=83
    x5=60; y5=86
    x6=64; y6=83
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=86
 
    
    global filename
    filename = '9ions/9ions_370V_9'
    
    Nine()
def Trans_9ions_370V_10():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=48; y2=85
    x3=53; y3=84
    x4=57; y4=86
    x5=61; y5=83
    x6=64; y6=86
    x7=68; y7=85
    x8=73; y8=86
    x9=79; y9=86
    
    
    global filename
    filename = '9ions/9ions_370V_10'
    
    Nine()
def Trans_9ions_370V_11():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=85
    x2=48; y2=84
    x3=52; y3=86
    x4=56; y4=84
    x5=60; y5=87
    x6=64; y6=83
    x7=68; y7=86
    x8=73; y8=85
    x9=79; y9=86  
    
    global filename
    filename = '9ions/9ions_370V_11'
    
    Nine()
def Trans_9ions_370V_12():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=85
    x3=53; y3=84
    x4=56; y4=86
    x5=60; y5=84
    x6=64; y6=86
    x7=68; y7=84
    x8=73; y8=86
    x9=79; y9=85
    
    global filename
    filename = '9ions/9ions_370V_12'
    
    Nine()
def Trans_9ions_370V_13():
    global x1; global x2;global x3; global x4;global x5;global x6; global x7;global x8; global x9;
    global y1; global y2;global y3;global y4;global y5; global y6; global y7;global y8; global y9; 
    
    x1=41; y1=84
    x2=47; y2=85
    x3=52; y3=85
    x4=56; y4=86
    x5=60; y5=84
    x6=64; y6=86
    x7=68; y7=85
    x8=73; y8=85
    x9=79; y9=86  
    
    global filename
    filename = '9ions/9ions_370V_13'
    
    Nine()



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def Trans_5ions_120V_1():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    
    x1= 46; y1= 85          
    x2= 56; y2= 85       
    x3= 65; y3= 85
    x4= 74; y4= 85
    x5= 84; y5= 86
    
    
    global filename
    filename = '5ions/5ions_120V_1'
    
    Five() 
    
def Trans_5ions_120V_2():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 46; y1= 85          
    x2= 56; y2= 85       
    x3= 65; y3= 85
    x4= 74; y4= 85
    x5= 84; y5= 86
    
    
    global filename
    filename = '5ions/5ions_120V_2'
    
    Five()

    
def Trans_5ions_258V_1():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 47; y1= 84          
    x2= 55; y2= 85       
    x3= 62; y3= 85
    x4= 69; y4= 85
    x5= 77; y5= 85
    
    
    global filename
    filename = '5ions/5ions_258V_1'
    
    Five()

def Trans_5ions_258V_2():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 47; y1= 85          
    x2= 55; y2= 85       
    x3= 62; y3= 85
    x4= 69; y4= 85
    x5= 76 ;y5= 85
    
    
    global filename
    filename = '5ions/5ions_258V_2'
    
    Five()
    
def Trans_5ions_258V_3():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 47; y1= 85          
    x2= 55; y2= 85       
    x3= 62; y3= 85
    x4= 69; y4= 85
    x5= 77; y5= 86
    
    global filename
    filename = '5ions/5ions_258V_3'
    
    Five()
    
def Trans_5ions_258V_4():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 47; y1= 85          
    x2= 55; y2= 85       
    x3= 62; y3= 85
    x4= 69; y4= 85
    x5= 77; y5= 85
    
    
    global filename
    filename = '5ions/5ions_258V_4'
    
    Five()
    
def Trans_5ions_370V_1():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 47; y1= 85          
    x2= 54; y2= 85       
    x3= 60; y3= 85
    x4= 66; y4= 85
    x5= 73; y5= 85
    
    
    global filename
    filename = '5ions/5ions_370V_1'
    
    Five()
    
def Trans_5ions_370V_2():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 47; y1= 85          
    x2= 54; y2= 85       
    x3= 60; y3= 85
    x4= 66; y4= 85
    x5= 73; y5= 85
    
    
    global filename
    filename = '5ions/5ions_370V_2'
    
    Five()
    
def Trans_5ions_370V_3():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 48; y1= 85          
    x2= 54; y2= 85       
    x3= 60; y3= 85
    x4= 67; y4= 85
    x5= 73; y5= 85
    
    
    global filename
    filename = '5ions/5ions_370V_3'
    
    Five()
    
def Trans_5ions_370V_4():
    global x1; global x2;global x3; global x4;global x5;
    global y1; global y2;global y3;global y4;global y5;  
    
    x1= 48; y1= 85          
    x2= 54; y2= 85       
    x3= 60; y3= 85
    x4= 67; y4= 85
    x5= 73; y5= 85
    
    
    global filename
    filename = '5ions/5ions_370V_4'
    
    Five()
     
#x- -- ------ --- --- --- ---  ----  ------ -- ---  - -- --- -- -- ------- -- -- - -- -- ---- 
def Trans_4ions_370V_1():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
   
    x1= 51 ;y1= 85
    x2= 58 ;y2= 85
    x3= 65 ;y3= 85
    x4= 73 ;y4= 85

    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '4ions/4ions_370V_1'
    
    Four() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_4ions_258V_3():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 49 ;y1= 85
    x2= 57 ;y2= 85
    x3= 64 ;y3= 86
    x4= 73 ;y4= 86
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '4ions/4ions_258V_3'
    
    Four() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain



def Trans_4ions_258V_2():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers

    x1= 49 ;y1= 85
    x2= 57 ;y2= 85
    x3= 64 ;y3= 86
    x4= 73 ;y4= 86  
 
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '4ions/4ions_258V_2'
    
    Four() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

def Trans_4ions_258V_1():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 49 ;y1= 85
    x2= 57 ;y2= 85
    x3= 65 ;y3= 86
    x4= 73 ;y4= 86
    
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '4ions/4ions_258V_1'
    
    Four() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_4ions_120V_2():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 48 ;y1= 85
    x2= 59 ;y2= 85
    x3= 69 ;y3= 85
    x4= 79 ;y4= 86
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '4ions/4ions_120V_2'
    
    Four() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain



def Trans_4ions_120V_1():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 48 ;y1= 85
    x2= 59 ;y2= 85
    x3= 69 ;y3= 85
    x4= 79 ;y4= 86  
 
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '4ions/4ions_120V_1'
    
    Four() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

#x--- --- ---  --- -- ---  ------ ----- ---- --- ---- -- --

def Trans_3ions_335V_8():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
   
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 86

    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_8'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

def Trans_3ions_335V_8s():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
   
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 86

    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_8s'
    
    Three() 
def Trans_3ions_335V_7():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 86
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_7'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_3ions_335V_6():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85      
 
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_6'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

def Trans_3ions_335V_5():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
   
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85   
    
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_5'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_3ions_335V_4():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_4'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain



def Trans_3ions_335V_3():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85      
 
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_3'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain
def Trans_3ions_335V_3s():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85      
 
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_3s'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

def Trans_3ions_335V_2():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
   
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 86    
    
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_2'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_3ions_335V_1():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_1'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain
    
def Trans_3ions_335V_1s():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 54 ;y1= 85
    x2= 62 ;y2= 85
    x3= 70 ;y3= 85
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_335V_1s'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_3ions_120V_2():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    
    x1= 57 ;y1= 85
    x2= 69 ;y2= 86
    x3= 80 ;y3= 86

    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_120V_2'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_3ions_120V_1():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 57 ;y1= 85
    x2= 68 ;y2= 86
    x3= 80 ;y3= 86
    
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '3ions/3ions_120V_1'
    
    Three() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain
    
#--- -------- - --- --  --- -- - - - -- ---   - ---- --- ---   --- ----- ----  -- --

def Trans_2ions_370V_2():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 57; y1= 85          
    x2= 66; y2= 86       
 
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '2ions/2ions_370V_2'
    
    Two() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

def Trans_2ions_370V_1():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 56; y1= 86
    x2= 66; y2= 86    
    
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '2ions/2ions_370V_1'
    
    Two() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain


def Trans_2ions_270V():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    x1= 55; y1= 86
    x2= 65; y2= 87 
    
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '2ions/2ions_270V'
    
    Two() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain

def Trans_2ions_120V_2():
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    
    x1= 62; y1= 85
    x2= 75; y2= 86    


    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '2ions/2ions_120V_2'
    
    Two() # Perform function (defined at bottom of this page) that corresponds to number of ions in chain




def Trans_2ions_120V_1(dark):
    global x1; global x2; global x3; global x4; global x5; global x6;
    global y1; global y2; global y3; global y4; global y5; global y6;
    # Define the location of each of the ions in the data set. 
    # This must be done separately by making 2D histograms and finding centers
    x1= 61; y1= 85
    x2= 75; y2= 86
    
    if dark==True:
        global dx1; global dx2; global dx3;
        dx1=54;
        dx2=68;
        dx3=82
    
    # "global" allows the "variable" to be called in another Notebook
    # by saying choose_file.variable after this function is run
    global filename
    filename = '2ions/2ions_120V_1'
    
    Two(dark) # Perform function (defined at bottom of this page) that corresponds to number of ions in chain



#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________

def Five(afterpulse_control = True):

    global old_data_table 

    # Calls the file in which you are taking the data from. '.cvs' files are read,
    # My files were made special as a pandas Dataframe, but any file can be read 
    # so long as they have the correct variable names. 
    old_data_table = pd.read_csv(f'{filename}')
    old_data_table = old_data_table.drop(columns = 'Unnamed: 0')
    old_data_table['time'] = (25*old_data_table['time'])/(4096)
    
    R = 2 # radius of region of interest. Individual ions can be given different radii 
    global Ion_1
    global Ion_2
    global Ion_3
    global Ion_4
    global Ion_5
    global Ion_6
    global Ion_7
    global Ion_8
    
    Ion_6 = []; Ion_7 = []; Ion_8 =[]
    
    R1 = R
    Ion_1 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x1})**2 + (y-{y1})**2)**(1/2) <= {R1}") #circular ROI
        
        .reset_index(drop=True)
    )
    
    #Loop that creates and saves the difference in time between events in the ROI
    name = Ion_1
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_1['dt'] = dt
    
    if afterpulse_control:
        Ion_1.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_1.reset_index(inplace = True)
    Ion_1['index'] = np.arange(len(name)) # new index is used in certain functions in class: "Ion"
    
    
    ### Same for the rest of the Ions ### 
    R2 = R
    Ion_2 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x2})**2 + (y-{y2})**2)**(1/2) <= {R2}")
        .reset_index(drop=True)
    )
    name = Ion_2
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_2['dt'] = dt
    
    if afterpulse_control:
        Ion_2.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_2.reset_index(inplace = True)
    Ion_2['index'] = np.arange(len(name))
    
    R3 = R
    Ion_3 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x3})**2 + (y-{y3})**2)**(1/2) <= {R3}")
        .reset_index(drop=True)
    )
    name = Ion_3
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_3['dt'] = dt
    
    if afterpulse_control:
        Ion_3.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_3.reset_index(inplace = True)
    Ion_3['index'] = np.arange(len(name))
    
    R4 = R
    Ion_4 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x4})**2 + (y-{y4})**2)**(1/2) <= {R4}")
        .reset_index(drop=True)
    )
    name = Ion_4
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_4['dt'] = dt
    
    if afterpulse_control:
        Ion_4.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_4.reset_index(inplace = True)
    Ion_4['index'] = np.arange(len(name))
    
    R5 = R
    Ion_5 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x5})**2 + (y-{y5})**2)**(1/2) <= {R5}") #circular ROI
        
        .reset_index(drop=True)
    )
    
    #Loop that creates and saves the difference in time between events in the ROI
    name = Ion_5
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_5['dt'] = dt
    
    if afterpulse_control:
        Ion_5.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_5.reset_index(inplace = True)
    Ion_5['index'] = np.arange(len(name)) # new index is used in certain functions in class: "Ion"
    

    
    # Creates a data set to call in the actual analysis Notebook
    global data_table
    
    data_table = Ion_1
    data_table = data_table.append(Ion_2)
    data_table = data_table.append(Ion_3)
    data_table = data_table.append(Ion_4)
    data_table = data_table.append(Ion_5)

    
    #Define the different ions with the given functions associated 
    # with the class: "Ion"
    global ion_1
    global ion_2
    global ion_3
    global ion_4
    global ion_5
    global ion_6
    global ion_7
    global ion_8
    
    
    ion_1 = Ion(1, x1, y1, R1, 'r', Ion_1)
    ion_2 = Ion(2, x2, y2, R2, 'tab:orange', Ion_2)
    ion_3 = Ion(3, x3, y3, R3, 'yellow', Ion_3)
    ion_4 = Ion(4, x4, y4, R4, 'g', Ion_4)
    ion_5 = Ion(5, x5, y5, R5, 'k', Ion_5)
    ion_6 = Ion(6, 0, 0, 0, 0, 0)
    ion_7 = Ion(7, 0, 0, 0, 0, 0)
    ion_8 = Ion(8, 0, 0, 0, 0, 0)
    
    sigma = 2
    uncertainty = True
    single_photon = False
    #ion_1.setup(sigma, uncertainty, single_photon)
    #ion_2.setup(sigma, uncertainty, single_photon)
    #ion_3.setup(sigma, uncertainty, single_photon)
    #ion_4.setup(sigma, uncertainty, single_photon)
    
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (15, 4))
    ax1.hist2d(old_data_table['x'], old_data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    ax2.hist2d(data_table['x'], data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    plt.show()
    #This last part prints the ROI for each ion so that you can verify the code is correct.   

#____________________________________________________________________________________________________________________

def Four(afterpulse_control = True):

    global old_data_table 

    # Calls the file in which you are taking the data from. '.cvs' files are read,
    # My files were made special as a pandas Dataframe, but any file can be read 
    # so long as they have the correct variable names. 
    old_data_table = pd.read_csv(f'{filename}')
    old_data_table = old_data_table.drop(columns = 'Unnamed: 0')
    old_data_table['time'] = (25*old_data_table['time'])/(4096)
    
    R = 2 # radius of region of interest. Individual ions can be given different radii 
    global Ion_1
    global Ion_2
    global Ion_3
    global Ion_4
    global Ion_5
    global Ion_6
    global Ion_7
    global Ion_8
    
    Ion_5 = []; Ion_6 = []; Ion_7 = []; Ion_8 =[]
    
    R1 = R
    Ion_1 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x1})**2 + (y-{y1})**2)**(1/2) <= {R1}") #circular ROI
        
        .reset_index(drop=True)
    )
    
    #Loop that creates and saves the difference in time between events in the ROI
    name = Ion_1
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_1['dt'] = dt
    
    if afterpulse_control:
        Ion_1.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_1.reset_index(inplace = True)
    Ion_1['index'] = np.arange(len(name)) # new index is used in certain functions in class: "Ion"
    
    
    ### Same for the rest of the Ions ### 
    R2 = R
    Ion_2 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x2})**2 + (y-{y2})**2)**(1/2) <= {R2}")
        .reset_index(drop=True)
    )
    name = Ion_2
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_2['dt'] = dt
    
    if afterpulse_control:
        Ion_2.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_2.reset_index(inplace = True)
    Ion_2['index'] = np.arange(len(name))
    
    R3 = R
    Ion_3 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x3})**2 + (y-{y3})**2)**(1/2) <= {R3}")
        .reset_index(drop=True)
    )
    name = Ion_3
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_3['dt'] = dt
    
    if afterpulse_control:
        Ion_3.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_3.reset_index(inplace = True)
    Ion_3['index'] = np.arange(len(name))
    
    R4 = R
    Ion_4 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x4})**2 + (y-{y4})**2)**(1/2) <= {R4}")
        .reset_index(drop=True)
    )
    name = Ion_4
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_4['dt'] = dt
    
    if afterpulse_control:
        Ion_4.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_4.reset_index(inplace = True)
    Ion_4['index'] = np.arange(len(name))

    
    # Creates a data set to call in the actual analysis Notebook
    global data_table
    
    data_table = Ion_1
    data_table = data_table.append(Ion_2)
    data_table = data_table.append(Ion_3)
    data_table = data_table.append(Ion_4)

    
    #Define the different ions with the given functions associated 
    # with the class: "Ion"
    global ion_1
    global ion_2
    global ion_3
    global ion_4
    global ion_5
    global ion_6
    global ion_7
    global ion_8
    
    
    ion_1 = Ion(1, x1, y1, R1, 'r', Ion_1)
    ion_2 = Ion(2, x2, y2, R2, 'tab:orange', Ion_2)
    ion_3 = Ion(3, x3, y3, R3, 'yellow', Ion_3)
    ion_4 = Ion(4, x4, y4, R4, 'g', Ion_4)
    ion_5 = Ion(5, 0, 0, 0, 0, 0)
    ion_6 = Ion(6, 0, 0, 0, 0, 0)
    ion_7 = Ion(7, 0, 0, 0, 0, 0)
    ion_8 = Ion(8, 0, 0, 0, 0, 0)
    
    sigma = 2
    uncertainty = True
    single_photon = False
    #ion_1.setup(sigma, uncertainty, single_photon)
    #ion_2.setup(sigma, uncertainty, single_photon)
    #ion_3.setup(sigma, uncertainty, single_photon)
    #ion_4.setup(sigma, uncertainty, single_photon)
    
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 4))
    ax1.hist2d(old_data_table['x'], old_data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    ax2.hist2d(data_table['x'], data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    plt.show()
    
    #This last part prints the ROI for each ion so that you can verify the code is correct.   

#_____________________________________________________________________________________________________________________    
#_____________________________________________________________________________________________________________________


def Three(afterpulse_control = True):
    
    global old_data_table 
    
    old_data_table = pd.read_csv(f'{filename}')
    old_data_table = old_data_table.drop(columns = 'Unnamed: 0')
    old_data_table['time'] = (25*old_data_table['time'])/(4096)
    
    R = 2 
    global Ion_1
    global Ion_2
    global Ion_3
    global Ion_4
    global Ion_5
    global Ion_6
    global Ion_7
    global Ion_8
    
    Ion_4 = []; Ion_5 = []; Ion_6 = []; Ion_7 = []; Ion_8 =[]
    
    R1 = R
    Ion_1 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x1})**2 + (y-{y1})**2)**(1/2) <= {R1}")
        .reset_index(drop=True)
    )
    name = Ion_1
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_1['dt'] = dt
    
    if afterpulse_control:
        Ion_1.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_1.reset_index(inplace = True)
    Ion_1['index'] = np.arange(len(name))
    
    R2 = R
    Ion_2 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x2})**2 + (y-{y2})**2)**(1/2) <= {R2}")
        .reset_index(drop=True)
    )
    name = Ion_2
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_2['dt'] = dt
    
    if afterpulse_control:
        Ion_2.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_2.reset_index(inplace = True)
    Ion_2['index'] = np.arange(len(name))
    
    R3 = R
    Ion_3 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x3})**2 + (y-{y3})**2)**(1/2) <= {R3}")
        .reset_index(drop=True)
    )
    name = Ion_3
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_3['dt'] = dt
    
    if afterpulse_control:
        Ion_3.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_3.reset_index(inplace = True)
    Ion_3['index'] = np.arange(len(name))
    
    global data_table
    data_table = Ion_1
    data_table = data_table.append(Ion_2)
    data_table = data_table.append(Ion_3)

    global ion_1
    global ion_2
    global ion_3
    global ion_4
    global ion_5
    global ion_6
    global ion_7
    global ion_8
    
    
    ion_1 = Ion(1, x1, y1, R1, 'r', Ion_1)
    ion_2 = Ion(2, x2, y2, R2, 'tab:orange', Ion_2)
    ion_3 = Ion(3, x3, y3, R3, 'yellow', Ion_3)
    ion_4 = Ion(4, 0, 0, 0, 0, 0)
    ion_5 = Ion(5, 0, 0, 0, 0, 0)
    ion_6 = Ion(6, 0, 0, 0, 0, 0)
    ion_7 = Ion(7, 0, 0, 0, 0, 0)
    ion_8 = Ion(8, 0, 0, 0, 0, 0)
    
    sigma = 2
    uncertainty = True
    single_photon = False
    #ion_1.setup(sigma, uncertainty, single_photon)
    #ion_2.setup(sigma, uncertainty, single_photon)
    #ion_3.setup(sigma, uncertainty, single_photon)
    
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 4))
    ax1.hist2d(old_data_table['x'], old_data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    ax2.hist2d(data_table['x'], data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    
    plt.show()
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________

def Two(afterpulse_control = True):
    global old_data_table 
        
    old_data_table = pd.read_csv(f'{filename}')
    old_data_table = old_data_table.drop(columns = 'Unnamed: 0')
    old_data_table['time'] = (25*old_data_table['time'])/(4096)
    
    R = 2
    
    global Ion_1
    global Ion_2
    
    
    R1 = R
    Ion_1 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x1})**2 + (y-{y1})**2)**(1/2) <= {R1}")
        .reset_index(drop=True)
    )
    name = Ion_1
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_1['dt'] = dt
    
    if afterpulse_control:
        Ion_1.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_1.reset_index(inplace = True)
    Ion_1['index'] = np.arange(len(name))
    
    R2 = R
    Ion_2 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x2})**2 + (y-{y2})**2)**(1/2) <= {R2}")
        .reset_index(drop=True)
    )
    name = Ion_2
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_2['dt'] = dt
    
    if afterpulse_control:
        Ion_2.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_2.reset_index(inplace = True)
    Ion_2['index'] = np.arange(len(name))

    
    global data_table 

    data_table = Ion_1
    data_table = data_table.append(Ion_2)

    global ion_1
    global ion_2
    global ion_3
    
    ion_1 = Ion(1, x1, y1, R1, 'r', Ion_1)
    ion_2 = Ion(2, x2, y2, R2, 'tab:orange', Ion_2)
   

    sigma = 2
    uncertainty = True
    single_photon = False
    #ion_1.setup(sigma, uncertainty, single_photon)
    #ion_2.setup(sigma, uncertainty, single_photon)
    
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 4))
    ax1.hist2d(old_data_table['x'], old_data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    ax2.hist2d(data_table['x'], data_table['y'],range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
   
    plt.show()
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________

def One(x1,y1,filename,afterpulse_control = True):
    
    global old_data_table 

    old_data_table = pd.read_csv(f'{filename}')
    old_data_table = old_data_table.drop(columns = 'Unnamed: 0')
    old_data_table['time'] = (25*old_data_table['time'])/(4096) #Output in ns
    
    R = 2
    global Ion_1
    global Ion_2
    global Ion_3
    global Ion_4
    global Ion_5
    global Ion_6
    global Ion_7
    global Ion_8
    
    Ion_2 = []; Ion_3 = []; Ion_4 = []; Ion_5 = []; Ion_6 = []; Ion_7 = []; Ion_8 =[]

    
    R1 = R
    Ion_1 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"((x-{x1})**2 + (y-{y1})**2)**(1/2) <= {R1}")
        .reset_index(drop=True)
    )
    name = Ion_1
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_1['dt'] = dt
    
    if afterpulse_control:
        Ion_1.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_1.reset_index(inplace = True)
    Ion_1['index'] = np.arange(len(name))
    
    global data_table 

    data_table = Ion_1


    global ion_1
    global ion_2
    global ion_3
    global ion_4
    global ion_5
    global ion_6
    global ion_7
    global ion_8
    
    
    ion_1 = Ion(1, x1, y1, R1, 'r', Ion_1)
    ion_2 = Ion(2, 0, 0, 0, 0, 0)
    ion_3 = Ion(3, 0, 0, 0, 0, 0)
    ion_4 = Ion(4, 0, 0, 0, 0, 0)
    ion_5 = Ion(5, 0, 0, 0, 0, 0)
    ion_6 = Ion(6, 0, 0, 0, 0, 0)
    ion_7 = Ion(7, 0, 0, 0, 0, 0)
    ion_8 = Ion(8, 0, 0, 0, 0, 0)
    
    sigma = 2
    uncertainty = True
    single_photon = False
    #ion_1.setup(sigma, uncertainty, single_photon)
    
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 4))
    ax1.hist2d(old_data_table['x'], old_data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    ax2.hist2d(data_table['x'], data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    plt.show()
#____________________________________________________________________________________________________________________________


def Nine(afterpulse_control=True):

    global old_data_table 

    # Calls the file in which you are taking the data from. '.cvs' files are read,
    # My files were made special as a pandas Dataframe, but any file can be read 
    # so long as they have the correct variable names. 
    old_data_table = pd.read_csv(f'{filename}')
    old_data_table = old_data_table.drop(columns = 'Unnamed: 0')
    old_data_table['time'] = (25*old_data_table['time'])/(4096)
    
    
    
    R = 1 # radius of region of interest. Individual ions can be given different radii
    global Ion_1;global dIon_1
    global Ion_2;global dIon_2
    global Ion_3;global dIon_3
    global Ion_4;global dIon_4
    global Ion_5;global dIon_5
    global Ion_6;global dIon_6
    global Ion_7;global dIon_7
    global Ion_8;global dIon_8
    global Ion_9;global dIon_9
    global dIon_10;

    
    
    R1 = R
    Ion_1 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f" x in {ROI[0]} and {y1-2*R1} <= y <= {y1+2*R1}")#circular ROI
        .reset_index(drop=True)
    )
    
    #Loop that creates and saves the difference in time between events in the ROI
    name = Ion_1
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_1['dt'] = dt
    
    if afterpulse_control:
        Ion_1.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_1.reset_index(inplace = True)
    Ion_1['index'] = np.arange(len(name)) # new index is used in certain functions in class: "Ion"
    
    
    ### Same for the rest of the Ions ### 
    R2 = R
    Ion_2 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[1]} and {y2-2*R2} <= y <= {y2+2*R2}")
        .reset_index(drop=True)
    )
    name = Ion_2
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_2['dt'] = dt
    
    if afterpulse_control:
        Ion_2.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_2.reset_index(inplace = True)
    Ion_2['index'] = np.arange(len(name))
    
    R3 = R
    Ion_3 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[2]} and {y3-2*R3} <= y <= {y3+2*R3}")
        .reset_index(drop=True)
    )
    name = Ion_3
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_3['dt'] = dt
    
    if afterpulse_control:
        Ion_3.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_3.reset_index(inplace = True)
    Ion_3['index'] = np.arange(len(name))
    
    R4 = R
    Ion_4 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[3]} and {y4-2*R4} <= y <= {y4+2*R4}")
        .reset_index(drop=True)
    )
    name = Ion_4
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_4['dt'] = dt
    
    if afterpulse_control:
        Ion_4.query(f' dt > 1e-7', inplace = True) # eliminate after pulsing effects, this prevents breaks in dark states, and peaks at 0(s) bright states
        Ion_4.reset_index(inplace = True)
    Ion_4['index'] = np.arange(len(name))
    
    R5 = R
    Ion_5 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[4]} and {y5-2*R5} <= y <= {y5+2*R5}")
        .reset_index(drop=True)
    )
    name = Ion_5
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_5['dt'] = dt
    
    if afterpulse_control:
        Ion_5.query(f' dt > 1e-7', inplace = True) 
        Ion_5.reset_index(inplace = True)
    Ion_5['index'] = np.arange(len(name))
    
    R6 = R
    Ion_6 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[5]} and {y6-2*R6} <= y <= {y6+2*R6}")
        .reset_index(drop=True)
    )
    name = Ion_6
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_6['dt'] = dt
    
    if afterpulse_control:
        Ion_6.query(f' dt > 1e-7', inplace = True) 
        Ion_6.reset_index(inplace = True)
    Ion_6['index'] = np.arange(len(name))
    
    
    R7 = R
    Ion_7 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[6]} and {y7-2*R7} <= y <= {y7+2*R7}")
        .reset_index(drop=True)
    )
    name = Ion_7
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_7['dt'] = dt
    
    if afterpulse_control:
        Ion_7.query(f' dt > 1e-7', inplace = True) 
        Ion_7.reset_index(inplace = True)
    Ion_7['index'] = np.arange(len(name))
    

    R8 = R
    Ion_8 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[7]} and {y8-2*R8} <= y <= {y8+2*R8}")
        .reset_index(drop=True)
    )
    name = Ion_8
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_8['dt'] = dt
    
    if afterpulse_control:
        Ion_8.query(f' dt > 1e-7', inplace = True) 
        Ion_8.reset_index(inplace = True)
    Ion_8['index'] = np.arange(len(name))
    
    
    R9 = R
    Ion_9 = (
        old_data_table
        #.query("`cluster size` > 3")
        .query(f"x in {ROI[8]} and {y9-2*R9} <= y <= {y9+2*R9}")
        .reset_index(drop=True)
    )
    name = Ion_9
    dt = []
    for i in range(0, len(name)-1):
        dt.append(name.at[i+1, 'time'] - name.at[i, 'time'])
    dt.append(0)
    Ion_9['dt'] = dt
    
    if afterpulse_control:
        Ion_9.query(f' dt > 1e-7', inplace = True) 
        Ion_9.reset_index(inplace = True)
    Ion_9['index'] = np.arange(len(name))
    
    
    
    
    # Creates a data set to call in the actual analysis Notebook
    global data_table;global ddata_table
    
    data_table = Ion_1
    data_table = data_table.append(Ion_2)
    data_table = data_table.append(Ion_3)
    data_table = data_table.append(Ion_4)
    data_table = data_table.append(Ion_5)
    data_table = data_table.append(Ion_6)
    data_table = data_table.append(Ion_7)
    data_table = data_table.append(Ion_8)
    data_table = data_table.append(Ion_9)
    
    
    #Define the different ions with the given functions associated 
    # with the class: "Ion"
    global ion_1;global dion_1
    global ion_2;global dion_2
    global ion_3;global dion_3
    global ion_4;global dion_4
    global ion_5;global dion_5
    global ion_6;global dion_6
    global ion_7;global dion_7
    global ion_8;global dion_8
    global ion_9;global dion_9
    global dion_10;
    
    ion_1 = Ion(1, x1, y1, R1, 'r', Ion_1)
    ion_2 = Ion(2, x2, y2, R2, 'tab:orange', Ion_2)
    ion_3 = Ion(3, x3, y3, R3, 'yellow', Ion_3)
    ion_4 = Ion(4, x4, y4, R4, 'g', Ion_4)
    ion_5 = Ion(5, x5, y5, R5, 'cyan', Ion_5)
    ion_6 = Ion(6, x6, y6, R6, 'b', Ion_6)
    ion_7 = Ion(7, x7, y7, R7, 'k', Ion_7)
    ion_8 = Ion(8, x8, y8, R8, 'k', Ion_8)
    ion_9 = Ion(9, x9, y9, R9, 'k', Ion_9)
    
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize = (10, 4))
    ax1.hist2d(old_data_table['x'], old_data_table['y'], range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    ax2.hist2d(data_table['x'], data_table['y'] ,range = [(min(data_table['x'])-2, max(data_table['x'])+2), (min(data_table['y'])-2, max(data_table['y'])+2)], bins = (int(max(data_table['x']) - min(data_table['x']) +5) , int(max(data_table['y']) - min(data_table['y']) +5)))
    
    plt.show()
    #This last part prints the ROI for each ion so that you can verify the code is correct.   