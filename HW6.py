# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:51:05 2020

@author: charlescolgan
"""

#titanic_training.xlsx

#titanic_test.xlsx

import numpy as np
'Used for calculation'

import pandas as pd
'used for data storage and manipulation'

def read():
    'Read in training and test data from .xlsx file'
    
    check_train = False #validate training
    
    check_test = False #validate training
    
    
    names = ["Id", "pclass", "gender", "age", "sibsp", "parch", "fare", "embarked", "survived"]
    #Column names
    
    while check_train == False:  
        try:
           
            global file_train 
           
            file_train = pd.read_excel(input("Please enter file name for training data: "), header = None, names = names)            
            #Form data frame for training data
        
            check_train = True #Show valid
            
        except FileNotFoundError:
            print("file not found, please enter file name for training data: ")
            print() 
            
        except OSError:
            print("file not found, please enter file name for test data: ")
            print()
            
    while  check_test == False:
        try:
            
            global file_test
            
            file_test = pd.read_excel(input("Please enter file name for test data: "), header = None, names = names)
        
            check_test = True #Show valid
            
        except FileNotFoundError:
            print("file not found, please enter file name for test data: ")
            print()
            
        except OSError:
            print("file not found, please enter file name for test data: ")
            print()
                      
def main():
    read()
    print()
    
main()
        



        
