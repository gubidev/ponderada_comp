import numpy as np

def calculate(list):
 if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
 else: 
    list= np.array(list).reshape(3, 3)

    mean= np.mean(list).item()
    mean_x= np.mean(list, axis=0).tolist()
    mean_y= np.mean(list, axis=1).tolist()

    var= np.var(list).item()
    var_x= np.var(list, axis=0).tolist()
    var_y= np.var(list, axis=1).tolist()

    std= np.std(list).item()
    std_x= np.std(list, axis=0).tolist()
    std_y= np.std(list, axis=1).tolist()

    max= np.max(list).item()
    max_x= np.max(list, axis=0).tolist()
    max_y= np.max(list, axis=1).tolist()

    min= np.min(list).item()
    min_x= np.min(list, axis=0).tolist()
    min_y= np.min(list, axis=1).tolist()

    sum= np.sum(list).item()
    sum_x= np.sum(list, axis=0).tolist()
    sum_y= np.sum(list, axis=1).tolist()

    calculations= {
        'mean':[mean_x,mean_y,mean],
        'variance':[var_x,var_y,var],
        'standard deviation':[std_x,std_y,std],
        'max':[max_x,max_y,max],
        'min':[min_x,min_y,min],
        'sum':[sum_x,sum_y,sum]
    }

    return calculations