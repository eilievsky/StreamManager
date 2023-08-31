#this file contains process of multi process data streaming
import multiprocessing
import random
import time

STREAM_NUMBERS = 10

# This function will process one single file/stream
def process_stream(file_name: str , buffer_index: int , data_buffer:list , process_indicator_buffer:list = None):
     file = open(file_name, 'r')
     read_continue = True
     while read_continue == True:
       
       if data_buffer[buffer_index] is None:
            line = file.readline()
            if (line is not None) and (line != ''): 
                data_buffer[buffer_index] = int(line)
                read_continue = True
            else:
                read_continue = False

# this orchestrator will check minimal number in in data buffer and pring all this numbers also
def stream_orchestrator(data_buffer:list , process_indicator_buffer:list = None) -> None:
    # 
     
    while True:
        time.sleep(0.2)
        continue_stream = any(item is not None for item in data_buffer)
        if continue_stream == False: return 0
        min_value  =  min(lst_value for lst_value in data_buffer if lst_value is not None)
        buffer_index = 0
        for buffer_index in range(len(data_buffer)):
            if data_buffer[buffer_index] == min_value:
                # currently this only print next number for a stream. But this part can be replaced by any other activity for extracted number
                print(data_buffer[buffer_index])
                data_buffer[buffer_index] = None



def multi_main_stream():
    processes = []

    with multiprocessing.Manager() as manager:
        files_num_buffer = [None] * STREAM_NUMBERS
        shared_array = manager.list(files_num_buffer)

        # Start parallel processes as number of files with stream data
        for i in range(STREAM_NUMBERS):
            process = multiprocessing.Process(target=process_stream, args=(f"segments/segment{str(i+1)}.txt",i,shared_array))
            processes.append(process)
            process.start()
        
        # define orchestration processes
        process = multiprocessing.Process(target=stream_orchestrator, args=(shared_array,))
        processes.append(process)
        process.start()
    
        for process in processes:
            process.join()
    
            
    

