import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    myArray = np.array(list).reshape(3,3)

    calculations = {
        'mean': [myArray.mean(axis=0).tolist(), myArray.mean(axis=1).tolist(), myArray.mean()],
        'variance': [myArray.var(axis=0).tolist(), myArray.var(axis=1).tolist(), myArray.var()],
        'standard deviation': [myArray.std(axis=0).tolist(), myArray.std(axis=1).tolist(), myArray.std()],
        'max': [myArray.max(axis=0).tolist(), myArray.max(axis=1).tolist(), myArray.max()],
        'min': [myArray.min(axis=0).tolist(), myArray.min(axis=1).tolist(), myArray.min()],
        'sum': [myArray.sum(axis=0).tolist(), myArray.sum(axis=1).tolist(), myArray.sum()]
    }


    return calculations