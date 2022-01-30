import csv
import functools
import numpy as np
dir = "local/backup/"

def calculate_mean(data):
    mean = np.mean(data)
    std = np.std(data)
    distance_from_mean = abs(data - mean)
    max_dev = 2
    no_outliers = [x for x in data if x<11]
    no_outliers = [x for x in no_outliers if (x > mean - max_dev * std)]
    no_outliers = [x for x in no_outliers if (x < mean + max_dev * std)]
    mean = np.mean(no_outliers)
    return mean

def compute_diff(start, end):
    assert len(start) == len(end)
    diff = []
    for i in range(len(start)):
        diff.append(end[i] - start[i])
    return diff

def read_data_split(file_name, start, end):
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            if "Java:" in row[0]:
                s = row[0].replace("Java:","")
                start.append(int(s))
            elif "Rust:" in row[0]:
                s = row[0].replace("Rust:","")
                end.append(int(s))

def read_data(file_name, vec):
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            vec.append(int(row[0]))


file_name = dir + 'hecate_sx.txt'
start = []
end = []
read_data_split(file_name, start, end)
data = compute_diff(start, end)
mean_hecate_sx = round(calculate_mean(data), 3)
print("Average Hecate Sx is :" + str(mean_hecate_sx))

file_name = dir + 'nohecate_sx.txt'
start = []
end = []
read_data_split(file_name, start, end)
data = compute_diff(start, end)
mean_nohecate_sx = round(calculate_mean(data), 3)
print("Average No Hecate Sx is :" + str(mean_nohecate_sx))

file_name = dir + 'hecate_rx_start.txt'
start = []
read_data(file_name, start)
file_name = dir + 'hecate_rx_end.txt'
end = []
read_data(file_name, end)
data = compute_diff(start, end)
mean_hecate_rx = round(calculate_mean(data), 3)
print("Average Hecate Rx is :" + str(mean_hecate_rx))
#
file_name = dir + 'nohecate_rx_start.txt'
start = []
read_data(file_name, start)
file_name = dir + 'nohecate_rx_end.txt'
end = []
read_data(file_name, end)
data = compute_diff(start, end)
mean_nohecate_rx = round(calculate_mean(data), 3)
print("Average No Hecate Rx is :" + str(mean_nohecate_rx))

overhead_sx = round(100*(mean_hecate_sx/mean_nohecate_sx)-100, 3)
overhead_rx = round(100*(mean_hecate_rx/mean_nohecate_rx)-100, 3)
overhead_total = round(100*(mean_hecate_sx+mean_hecate_rx)/(mean_nohecate_sx+mean_nohecate_rx)-100, 3)
print("Overhead Sx :" + str(overhead_sx))
print("Overhead Rx :" + str(overhead_rx))
print("Overhead Total :" + str(overhead_total))
