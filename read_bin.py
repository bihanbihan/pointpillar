import numpy as np
path = '/home/hgdx/mmdetection3d/data/4D_dataset/4D_dataset_gt_database/3099_Car_3.bin'
with open(path,'rb') as f:
    data = f.read()
num_attr = 6
num_size = 4
num = len(data)//(num_attr*num_size)

bin_data = np.frombuffer(data,np.float32)
print(bin_data.shape)

bin_data = bin_data.reshape(num,num_attr)