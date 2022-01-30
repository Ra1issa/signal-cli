import csv
import functools
import numpy as np
dir = "e2e/"

def calculate_mean(data):
    mean = np.mean(data)
    std = np.std(data)
    distance_from_mean = abs(data - mean)
    max_dev = 2
    no_outliers = [x for x in data if x<100]
    no_outliers = [x for x in no_outliers if (x > mean - max_dev * std)]
    no_outliers = [x for x in no_outliers if (x < mean + max_dev * std)]
    mean = np.mean(no_outliers)
    return mean

def compute_diff(start, end):
    assert len(start) == len(end)
    diff = []
    for i in range(len(start)):
        diff.append(end[i] - start[i])
        if diff[i] < 0 :
            print(i)
    return diff

def read_data_split(file_name, start):
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            if "Java:" in row[0]:
                s = row[0].replace("Java:","")
                start.append(int(s))

def read_data(file_name, vec):
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            vec.append(int(row[0]))


file_name = dir + 'hecate_sx.txt'
start = []
read_data_split(file_name, start)

file_name = dir + 'hecate_rx_end.txt'
end = []
read_data(file_name, end)
data = compute_diff(start, end)
mean_hecate = round(calculate_mean(data), 3)
print("Average E2E Hecate is :" + str(mean_hecate))

file_name = dir + 'nohecate_sx.txt'
start2 = []
read_data_split(file_name, start2)

file_name = dir + 'nohecate_rx_end.txt'
end2= []
read_data(file_name, end2)
data= compute_diff(start2, end2)
mean_nohecate = round(calculate_mean(data), 3)
print("Average E2E No Hecate is :" + str(mean_nohecate))

overhead_total = round((100*mean_hecate/mean_nohecate)-100, 3)
print("Overhead Total :" + str(overhead_total))
