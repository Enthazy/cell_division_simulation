import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
if __name__ == "__main__":
    data = np.load('data.npz')

    fig = plt.figure()
    sns.histplot(data, x='coef',binwidth=0.001, kde=True)
    print(np.mean(data['coef']), np.var(data['coef']))
    fig2 = plt.figure()
    sns.histplot(data, x='interception',binwidth=0.001, kde=True)
    print(np.mean(data['interception']), np.var(data['interception']))
    plt.show()
