import numpy as np


def _extend_matrix(mat): # 3*4 -> 4*4
    mat = np.concatenate([mat, np.array([[0., 0., 0., 1.]])], axis=0)
    return mat

calib_path = "/home/hgdx/mmdetection3d/data/4D_dataset/training/calib/000000.txt"

with open(calib_path, 'r') as f:
    lines = f.readlines()
    P2 = np.array([float(info) for info in lines[0].split(' ')[1:13]
                           ]).reshape([3, 4])

P2 = _extend_matrix(P2)


print(P2)