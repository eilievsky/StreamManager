## Data Stream Demo

### Problem Description

Suppose you have a stream of data divided into 10 segments. Within each segment, all messages are integers sorted in ascending order.

For example: <br>
Segment 1: 	[1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]<br>
Segment 2: 	[1,1,1,1,1,2,2,2,2,2,3,3,3,3,4]<br>
Segment 3: 	[2,2,2,2,2,3]<br>
…<br>
Segment 10: 	[2,2,2,2,4,4,6,8]<br>

This solution provide application to read all thoses messages and write them to a single destination which has all messages sorted in an increasing order:<br>

Destination:	[1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,6,8]

### Solution
There are 2 type of solutions.
First solution to perform the task s a single process . Second solution was done to perform the same task with a mutiprocessing approach

In both cases implemented algorithm was the same:
- Create data buffer with number of data cells that is equal to number of data source (files in this case)
- Initiate the process that will read values sequencially from files into data buffer with following logic:
    - Each file have only one cell in data buffer
    - Data from file will be written into designated cell of data buffer only when value in data buffer is None
- Initite process of processing data buffer with following logic:
    - Find mimumal number in data buffer
    - Extract from data buffer all numbers that defined as minimal and process it (in this solution print it)
    - Replace numbers that were extracted to None value
- Process will be finished when all values in data buffer are None


### Assumptions
- All files (streams) contains only numbers in sequencial order
- File have at least one number

### Files and Folders
- segments (Folder) - contains files that were defined for streaming activites
- process (Folder) - contains streaming process files
    - multiprocess.py - multi process data stream demo
    - singleprocess.py - single process data stream demo

### Activation
- From virtual environment run following command to run multiptocessing data stream
~~~ 
python app.py multi
~~~ 
- From virtual environment run following command to run single process data stream
~~~ 
python app.py single
~~~ 

NOTE: Docker image can be created but could not execute it

- Build docker image (from venv environment)
~~~ 
docker build --pull --rm -f "DockerFile" -t data-stream-demo:latest "." 
~~~
- Run created docker image
~~~ 
docker container run -it data-stream-demo:latest
~~~

