import numpy as np


def run_averages(file_input='test_sample.csv', file_output='test_average.csv'):
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')
    averages = planes.mean(axis=0)[np.newaxis, :]
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')

def method2():
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt("test_sample.csv", data_input, fmt='%d', delimiter=',')
