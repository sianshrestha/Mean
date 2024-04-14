import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    l = np.array(list)
    print(l)

    mean_col = [l[[0,3,6]].mean(), l[[1,4,7]].mean(), l[[2,5,8]].mean()]
    mean_row = [l[[0,1,2]].mean(), l[[3,4,5]].mean(), l[[6,7,8]].mean()]

    var_col = [l[[0,3,6]].var(), l[[1,4,7]].var(), l[[2,5,8]].var()]
    var_row = [l[[0,1,2]].var(), l[[3,4,5]].var(), l[[6,7,8]].var()]

    std_col = [l[[0,3,6]].std(), l[[1,4,7]].std(), l[[2,5,8]].std()]
    std_row = [l[[0,1,2]].std(), l[[3,4,5]].std(), l[[6,7,8]].std()]

    max_col = [l[[0,3,6]].max(), l[[1,4,7]].max(), l[[2,5,8]].max()]
    max_row = [l[[0,1,2]].max(), l[[3,4,5]].max(), l[[6,7,8]].max()]

    min_col = [l[[0,3,6]].min(), l[[1,4,7]].min(), l[[2,5,8]].min()]
    min_row = [l[[0,1,2]].min(), l[[3,4,5]].min(), l[[6,7,8]].min()]

    sum_col = [l[[0,3,6]].sum(), l[[1,4,7]].sum(), l[[2,5,8]].sum()]
    sum_row = [l[[0,1,2]].sum(), l[[3,4,5]].sum(), l[[6,7,8]].sum()]
    

    return {
        'mean': [mean_col, mean_row, l.mean()],
        'variance': [var_col, var_row, l.var()],
        'standard deviation': [std_col, std_row, l.std()],
        'max': [max_col, max_row, l.max()],
        'min': [min_col, min_row, l.min()],
        'sum': [sum_col, sum_row, l.sum()]
    }
