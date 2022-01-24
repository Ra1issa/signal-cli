import csv
import functools
import numpy as np
dir = "500B/"

def calculate_mean(data):
    mean = np.mean(data)
    std = np.std(data)
    distance_from_mean = abs(data - mean)
    max_dev = 2
    no_outliers = [x for x in data if (x > mean - max_dev * std)]
    no_outliers = [x for x in no_outliers if (x < mean + max_dev * std)]
    mean = np.mean(no_outliers)
    return mean

def read_data(file_name, vec):
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            vec.append(int(row[0]))


file_name = dir + 'nohecate_sx.txt'
data = []
read_data(file_name, data)
av_nsx = round(calculate_mean(data)/10**6,3)
print("Average No Hecate Sx is :" + str(av_nsx))

file_name = dir + 'nohecate_rx.txt'
data = []
read_data(file_name, data)
av_nrx = round(calculate_mean(data)/10**6,3)
print("Average No Hecate Rx is :" + str(av_nrx))


file_name = dir + 'hecate_sx.txt'
data = []
read_data(file_name, data)
av_sx = round(calculate_mean(data)/10**6,3)
print("Average Hecate Sx is :" + str(av_sx))

file_name = dir + 'hecate_rx.txt'
data = []
read_data(file_name, data)
av_rx = round(calculate_mean(data)/10**6,3)
print("Average Hecate Rx is :" + str(av_rx))

overhead_rx = round(100*(av_rx/av_nrx)-100,3)
overhead_sx = round(100*(av_sx/av_nsx)-100,3)
overhead_total= round(100*(av_sx+av_rx)/(av_nsx+av_nrx)-100,3)

print("Overhead Sx is :" + str(overhead_sx))
print("Overhead Rx is :" + str(overhead_rx))
print("Overhead Total is :" + str(overhead_total))
# file_name = dir + 'hecate_start.txt'
# start = []
# read_data(file_name, start)
# file_name = dir + 'hecate_end.txt'
# end = []
# read_data(file_name, end)
# av2 = calculate_mean(start, end)/10**6
# print("Average Hecate is :" + str(av2))
#
# overhead = (av2/av1)*100-100
# print("Percentage overhead is :" + str(overhead))
