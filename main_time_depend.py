import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from src_time_depend import *


if __name__ == "__main__":
    coef_lst = []
    int_lst = []
    def run():
        for _ in range(1000):
            time_dependent_results = time_dependent_main()
            time_dependent_all_division_time = np.sort(np.array(time_dependent_results)[:,2])
            num = 300
            conn = {"log N-1": np.log(np.arange(num)+1), "time": time_dependent_all_division_time[:num]}
            xdata= conn["log N-1"].reshape(-1,1)
            ydata = conn["time"]
            regr = LinearRegression()
            regr.fit(xdata, ydata)
            coef_lst.append(regr.coef_[0])
            int_lst.append(regr.intercept_)
            # print(regr.coef_)
            # print(regr.intercept_)
    run()
    data = pd.DataFrame({'coef': coef_lst, 'interception': int_lst})
    np.savez_compressed('data.npz', **data)
    plt.show()