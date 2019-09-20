# -*- coding: utf-8 -*-
"""
Program to graph the virtual time vs time relation of n threads in a single processor Proptional scheduling 
system.

@author: Prince John
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


end_time = int(input('end_time: '))

time_step = int(input('time_step: '))
t = np.arange(0 , end_time, time_step)
thread_count = int(input('Number of threads: '))
thread = []
thread_ratio =[]
virtual_time = []#list of lists that stores the virtual times for the threads
scale=0



def thread_select(threads):
    max_time = np.asarray([max(i) for i in threads]) # numpy array with max times of all lists
    print(max_time)
    return np.argmin(max_time)

for i in range(0, thread_count, 1):
    thread.append(i)
    virtual_time.append([0])
    thread[i]=plt.subplot()
    thread_ratio.append(int(input('ratio: ')))
    scale +=thread_ratio[i]
    


scaling_factor = [((end_time/scale)*i)/time_step for i in thread_ratio]

for i in range(0, end_time, time_step):
    active_thread = thread_select(virtual_time)
    for i in range(0, thread_count, 1):
        if i == active_thread:
            virtual_time[i].append(virtual_time[i][-1]+time_step*scaling_factor[i])
        else:
            virtual_time[i].append(virtual_time[i][-1])
#plot
t = np.arange(0 , end_time+1, time_step)
for i in range(0, thread_count):
    thread[i].plot(t, virtual_time[i])


plt.xticks(np.arange(0, end_time+1, time_step))
plt.xlabel='time'
plt.grid()
plt.ylabel='virtual time'
plt.title='Proportional Scheduling'
plt.show()
                



#(lambda x: x if x != 0 else 1)(virtual_time[i][-1])
