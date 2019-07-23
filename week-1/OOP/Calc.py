# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

class Calc:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.__create_stats()
        
    def __create_stats(self):
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_variance()
        self.standev = self.__calc_standev()
    
    def __calc_mean(self, d = None):
        if d == None:
            return  sum(self.data)/len(self.data)
        else:
            return sum(d)/len(d)
    
    def __calc_median(self):
        dataLen = int(len(self.data))
        
        #if length is odd, take middle value, by dividing the length by 2, then rounding up
        if (dataLen % 2) == 1:
            return self.data[round(dataLen/2)]
        
        #if the length is even, take the mean of the middle two values, which have indices length/2 and (length/2 + 1)
        elif (dataLen % 2) == 0:
            #remember that indices are indexed at 0
            return self.__calc_mean([self.data[int(dataLen/2-1)], self.data[int(dataLen/2)]]) 
    
    def __calc_variance(self):
        # multiply 1/(length of data) by the sum of (data point - mean)^2, for each data point
        sum = 0
        for x in self.data:
            sum += (x - self.mean)**2
        return (1/(len(self.data)-1))*sum
    
    def __calc_standev(self):
        return math.sqrt(self.__calc_variance())
    
    def add_data(self, new_data):
        self.data.extend(new_data) # adds new data to end of list
        self.__create_stats() # updates all old stats to include new data
        return self.data
        
    def remove_data(self, position): # give position to remove data
        self.data.pop(position)
        return self.data