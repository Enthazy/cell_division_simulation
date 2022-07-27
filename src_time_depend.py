import numpy as np
import matplotlib.pyplot as plt


def init_cell(cell_id, born_time, expected_division_time, is_alive):
    """
    id: index
    t: born time
    division time: time take to divise
    is_alive: bool
    """
    return [cell_id, born_time, expected_division_time, is_alive]


def time_dependent_sample(born_time):
    def gamma(a, b):
        return 5 * np.sin(a + b) + 5

    # 3.2

    gamma_max = 10
    tau_star = 0

    while True:
        u1 = np.random.uniform(0, 1)
        tau_star -= np.log(u1) / gamma_max
        u2 = np.random.uniform(0, 1)
        if u2 <= gamma(tau_star, born_time + tau_star) / gamma_max:
            break

    return tau_star


def time_dependent_divise(cell_list, cell_id):
    target_cell = cell_list[cell_id]
    # 1. disactive cell with cell id
    target_cell[3] = False
    # 2. add two new cells
    N = len(cell_list)
    new_cell1 = init_cell(N, target_cell[2], target_cell[2] + time_dependent_sample(target_cell[2]), True)
    new_cell2 = init_cell(N + 1, target_cell[2], target_cell[2] + time_dependent_sample(target_cell[2]), True)
    cell_list.append(new_cell1)
    cell_list.append(new_cell2)


def find_next_divise_cell(cell_list):
    minimal = np.inf
    cell_id = -1
    for cell in cell_list:
        if cell[3] == True:
            if cell[2] <= minimal:
                minimal = cell[2]
                cell_id = cell[0]
    return cell_id


def time_dependent_run(cell_list):
    next_divise_cell_id = find_next_divise_cell(cell_list)
    time_dependent_divise(cell_list, next_divise_cell_id)
    return cell_list


def time_dependent_main():
    cell_list = []
    first_cell = init_cell(0, 0, time_dependent_sample(0), True)
    cell_list.append(first_cell)

    for _ in range(600):
        if _ < 5:
            print(cell_list)
        time_dependent_run(cell_list)

    return cell_list
