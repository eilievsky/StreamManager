#this file contains process of single process data streaming

import time

STREAM_NUMBERS = 10
files_manager_lst =[]
files_num_buffer = [None] * STREAM_NUMBERS


def init_stream_data()->None:
    #init array of files with stream data
    for file_el in range(1,STREAM_NUMBERS+1):
        file = open(f"segments/segment{str(file_el)}.txt", 'r')
        files_manager_lst.append(file)

def get_next_line() -> None:
    # this function will fill buffer of numbers. One number from file. If there is end of file
    buffer_index = 0
    for inputfile in files_manager_lst:  
        if files_num_buffer[buffer_index] is None:
            line = inputfile.readline()
            if (line is not None) and  (line != ''): 
                files_num_buffer[buffer_index] = int(line)
        buffer_index +=1

    
def check_if_all_none() -> bool:
    #check if all elements of buffer is null or not
    return any(item is not None for item in files_num_buffer)


def print_all_min_numbers() -> None:
    #this function print minimum number from buffer and replace it with None value
    min_value  =  min(lst_value for lst_value in files_num_buffer if lst_value is not None)
    buffer_index = 0
    for buffer_index in range(len(files_num_buffer)):
        if files_num_buffer[buffer_index] == min_value:
            # currently this only print next number for a stream. But this part can be replaced by any other activity fora number
            print(files_num_buffer[buffer_index])
            time.sleep(0.1)
            files_num_buffer[buffer_index] = None

def single_main_steam() -> None:
    #main function that need to be use to activate program
    init_stream_data()
    get_next_line()
    while check_if_all_none() == True:
        print_all_min_numbers()
        get_next_line()

                