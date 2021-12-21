import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sql_repo


def unic_name(list_name):
    a = []
    for i in list_name:
        if i.lower() not in [j.lower() for j in a]:
            a.append(i)
    return a


def generate_device_hist(connection):
    list_name = sql_repo.__getdevicesname(connection)
    tick_list = unic_name(list_name)

    num_elements = len(tick_list)
    index = np.arange(num_elements)
    values1 = []
    for i in np.arange(len(tick_list)):
        values1.append(list_name.count(list_name[i]))
        if list_name.count(list_name[i]) == 2:
            list_name.remove(list_name[i])
            i -= 1

    tick_values = range(0, len(tick_list))

    plt.title('Frequency of device use')
    plt.bar(index, values1)
    plt.xticks(ticks=tick_values, labels=tick_list, rotation=90, fontsize=8)
    plt.show()


def generate_speed_index(value):
    data = {'Without index': [0, value[0]],
            'With index': [0, value[1]]}
    df = pd.DataFrame(data)
    x = np.arange(2)
    plt.axis([0, 1.5, 0, 0.005])
    plt.plot(x, df)
    plt.legend(data, loc=2)
    plt.show()


def generate_speed_count(value):
    data = {'USE [COUNT]': [0, value[0]],
            'USE [EXIST]': [0, value[1]]}
    df = pd.DataFrame(data)
    x = np.arange(2)
    plt.axis([0, 1.5, 0, 0.005])
    plt.plot(x, df)
    plt.legend(data, loc=2)
    plt.show()


