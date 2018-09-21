# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:37:10 2018

@author: javier soon
id 80436654
purpose of the lab was to classify pictures given a directory using recursion
"""
import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)] 
    
    return dir_list, file_list

def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


#////////////

def process_dir(path):

    #print (path)
    dir_list, file_list = get_dirs_and_files(path)
    #print(dir_list)
    #print(file_list)
    cat_list = []
    dog_list = []
    
    
    # Your code goes here
    if len(dir_list) == 0 and len(file_list) == 0:  # if there is no sub directory or files in the directory 
        return                                          # continue  to return 
 
    if(len(file_list) != 0):            # if there is something inside the file list it goes here
        for pic in file_list:               # use a for loop to traverse the file list
            if ".jpg" in pic:                   # checks to see if the file is a jpg ie picture if it is it classifies it
                #print(pic)
                if classify_pic(pic) > .5:  
                    dog_list.append(path + '/' + pic)       # appends the path and the picture into the correct list
                else:
                    cat_list.append(path + '/' + pic)
    #Robert-lists are not merged thus empty. only pics added are the ones that possibly exist in the first directory
 
    for directory in dir_list:          # for loop with recursion
            #print(directory)
        process_dir(path +'/' + directory)
    '''
    Robert-The directory list could have been traversed recursivly by using a index parameter to
    increment first by depth such as process_dir(path + '/' + dir_list[d], 0) zero being an index
    parameter d in subsiquent calls to the deeper directories then down the dir_list 
    list by passing (path, d+1) maintaining the depth of current directory but checking 
    the next in the list on return from checking deeper.
    '''
    print(dog_list)
    print(cat_list)
    return cat_list, dog_list
    
    
#    print (path)
#    if len(dir_list) == 0 and len(file_list) == 0:
#        return
#    if len(dir_list) == 0 and len(file_list ) != 0:
#        if classify_pic(file_list[0]) >= .5:
#            dog_list.append(file_list[0])
#        else:
#            cat_list.append(file_list[0])
#            del file_list[0]
#            return
#    else:
#        process_dir(path + '/' + dir_list[0])
#        del dir_list[0]
#        return process_dir(path + '/' + dir_list[0])
    
# =============================================================================

def main():
    #start_path = 'C:/Users/javie/OneDrive/1.1 CatsDogs/1.1 CatsDogs/Pictures' # where the directory was for me
    start_path = './'                 # current directory if the file is in this directory
    #print(start_path)
    process_dir(start_path)

    
main()
