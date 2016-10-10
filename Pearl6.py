from time import clock

start = clock() #assigns the current time to the variable "Start"
for i in range(1, 1000000):#Starts the for loop, counts from 1 up to 1000000
    pass # no operation

stop = clock() # Assigns the value after executing (current time after execution) to variable "Stop"
diff = stop - start #substracts the registered time in stop from Startand saves it into variable diff
print(diff) #prints the difference saved in variable diff
