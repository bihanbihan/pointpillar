import os

# 指定目标文件夹路径
# data_dir = '/home/hgdx/mmdetection3d/data/4D_dataset/training/velodyne_reduced'
data_dir = '/home/hgdx/mmdetection3d/data/4D_dataset/testing/velodyne'
# data_dir = '/home/hgdx/mmdetection3d/data/4D_dataset/4D_dataset_gt_database'
image_dir = '/home/hgdx/mmdetection3d/data/4D_dataset/training/image_2'
count = 0
count1 = 0
# 遍历文件夹中的所有文件
for filename in os.listdir(data_dir):
    if filename.endswith('.bin'):
        file_path = os.path.join(data_dir, filename)
        
        # 获取文件大小
        file_size = os.path.getsize(file_path)
        
        # 如果文件大小不能被6整除
        # if file_size % (6 * 4) != 0:
        if file_size == 0:
            # 输出文件名
            count1 += 1
            # print(f"文件 {filename} 不能被6整除，将被删除.")
            print(f"文件 {filename} empty.")
            
            # # 删除对应的 .txt 文件
            # image_txt_path = os.path.join(image_dir, os.path.splitext(filename)[0] + '.txt')
            # if os.path.exists(image_txt_path):
            #     os.remove(image_txt_path)
            #     print(f"删除 {image_txt_path}")
            
            # # 删除对应的 .bin 文件
            # os.remove(file_path)
            # print(f"删除 {file_path}")
        else:
            count += 1
        print(count,count1)
    