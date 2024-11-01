import os
import shutil

# 定义文件夹路径
folder_b = '../history/countries'
folder_a = '../temp/history_backup'
folder_c = '../temp/history'

# 确保目标文件夹存在
if not os.path.exists(folder_c):
    os.makedirs(folder_c)

# 遍历文件夹A中的所有文件
for filename in os.listdir(folder_a):
    # 构建文件的完整路径
    file_path_a = os.path.join(folder_a, filename)
    
    # 检查是否为文件
    if os.path.isfile(file_path_a):
        # 构建文件夹B中的文件路径
        file_path_b = os.path.join(folder_b, filename)
        
        # 检查文件夹B中是否存在同名文件
        if os.path.isfile(file_path_b):
            # 构建文件夹C中的目标路径
            file_path_c = os.path.join(folder_c, filename)
            
            # 复制文件到文件夹C
            shutil.copy2(file_path_b, file_path_c)
            print(f'Copied {filename} to {folder_c}')

print("All matching files have been copied.")