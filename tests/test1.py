from src import *
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from src_time_independ import *


def trial(sample):
    coef_lst = []
    int_lst = []

    def run():
        n_trial = 400
        for _ in range(n_trial):
            results = main(sample)
            all_division_time = np.sort(np.array(results)[:, 2])
            num = 300
            conn = {"log N-1": np.log(np.arange(num) + 1), "time": all_division_time[:num]}
            xdata = conn["log N-1"].reshape(-1, 1)
            ydata = conn["time"]
            regr = LinearRegression()
            regr.fit(xdata, ydata)
            coef_lst.append(regr.coef_[0])
            int_lst.append(regr.intercept_)

    run()
    return coef_lst, int_lst


if __name__ == "__main__":
    hypermeter_lst = (np.arange(100) + 1)/3
    
    result1 = []
    result2 = []
    N =20
    for _e in range(N):
        T = hypermeter_lst[_e]
        def sample(born_time):
            def gamma(a, b):
                return 5 * np.sin(b * (2 * np.pi / T) + a) + 5

            gamma_max = 10
            tau_star = 0

            while True:
                u1 = np.random.uniform(0, 1)
                tau_star -= np.log(u1) / gamma_max
                u2 = np.random.uniform(0, 1)
                if u2 <= gamma(tau_star, born_time + tau_star) / gamma_max:
                    break

            return tau_star

        coef_lst, int_lst = trial(sample)

        data = pd.DataFrame({'coef': coef_lst, 'interception': int_lst})
        np.savez_compressed('data_independ' + str(_e) + '.npz', **data)
        plt.show()
        
        result1.append(np.mean(coef_lst))
        result2.append(np.mean(int_lst))
        
    fig1 = plt.figure()
    plt.plot(hypermeter_lst[:N], result1, label='coef')
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()

    fig2 = plt.Figure()
    plt.plot(hypermeter_lst[:N], result2, label='interception')
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()
