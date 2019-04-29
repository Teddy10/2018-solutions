# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:08:07 2019

@author: ucapfas
"""


# =============================================================================
# ATTENTION!! -pws anoigw .csv files
#             -pws anoigw/kleinw json files
#             -otan antika8istw se mia lista me for, to kanw me arxikopoihsh-append
#             - ti einai ta comprehensions
# =============================================================================
            




import csv
import json
import matplotlib.pyplot as plt
import cmath



def json_to_dictionary():
    with open('python_language_1_data.csv') as init_data:
        data = csv.reader(init_data)
        
    data_dict = {}
    prev_year = 0
    
    next(data)
    
    for row in data:
        
        
        year = row[0]
        
        if prev_year != year:
            data_dict[year] = []
        data_dict[year].append(float(row[2]))
        prev_year = year
        
    with open('json_data.json', 'w') as jason:
        json.dump(data_dict, jason, sort_keys=True, indent=4)
    
        
        
 
    
def time_series(jason, year, colour):
    with open(jason, 'r') as new_jason:
        dictionary = json.load(new_jason)
        
        length = len(dictionary[year])
        r = range(1,length+1)
        
        list_of_days = []
        for n in r:
            list_of_days.append(n)
            
        y = dictionary[year]
#        x = [[year, day] for day in list_of_days]
        
              
        plt.plot(y, colour)
        plt.show()


        
def mean_rain(jason, start_year, final_year):
    with open(jason,'r') as new_jason:
        dictionary = json.load(new_jason)
        
        
    average_rain_per_year = []
    
    for year in dictionary:          
        if float(year) >= start_year and float(year) <= final_year:
            rain = 0
            days = 0
            for daily_rain in dictionary[year]:
                
                days = days + 1
                rain = rain + daily_rain                
            average_rain = rain/days
            average_rain_per_year.append(average_rain)
            
    
    r = range(start_year, final_year+1)
    x = []
    
    for n in r:
        x.append(n) 
    
    
    plt.plot(x, average_rain_per_year)
    plt.show()
        
     

def single_value_modifier(value):
    power = cmath.sqrt(2)
    multiplier = 1.2**power
    value = value*multiplier
    
    return value.real


def for_loop_modifier(jason, given_year):
    with open(jason, 'r') as new_jason:
        dictionary = json.load(new_jason)
        
    rain_list = dictionary[str(given_year)]
    
    new_data = []
    for value in rain_list:
        new_data.append(single_value_modifier(value))
# =============================================================================
#     for value in rain_list:
#         value = single_value_modifier(value)
# =============================================================================
        
    return new_data

def comprehension_modifier(jason, given_year):
    with open(jason, 'r') as new_jason:
        dictionary = json.load(new_jason)
        
    rain_list = dictionary[str(given_year)]
    new_rain_list = [single_value_modifier(value) for value in rain_list]
    
    return new_rain_list
            




    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
