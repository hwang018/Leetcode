def shiftGrid(grid, k):
    import numpy as np
    arr = np.array(grid)
    save_shape = arr.shape
    arr = arr.reshape(-1)
    arr_shifted = np.roll(arr,k).reshape(save_shape)
    return arr_shifted