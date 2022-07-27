import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def task1():
    data = np.load('data.npz')
    fig = plt.figure()
    sns.histplot(data, x='coef', binwidth=0.001, kde=True)
    print(np.mean(data['coef']), np.var(data['coef']))
    fig2 = plt.figure()
    sns.histplot(data, x='interception', binwidth=0.001, kde=True)
    print(np.mean(data['interception']), np.var(data['interception']))
    plt.show()


def task2():
    data_in = np.load('data_independ.npz')
    data_de = np.load('data_depend.npz')

    fig = plt.figure()
    sns.histplot(data_in, x='coef', binwidth=0.001, kde=True, color='coral', label='in')
    sns.histplot(data_de, x='coef', binwidth=0.001, kde=True, color='teal', label='de')
    print(np.mean(data_in['coef']), np.var(data_in['coef']))
    plt.grid(alpha=0.5)
    plt.legend()

    fig2 = plt.figure()
    sns.histplot(data_in, x='interception', binwidth=0.001, kde=True, color='coral', label='in')
    sns.histplot(data_de, x='interception', binwidth=0.001, kde=True, color='teal', label='de')
    print(np.mean(data_in['interception']), np.var(data_in['interception']))


    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # task1()
    task2()
