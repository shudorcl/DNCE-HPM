import os
import shutil

# 三字母代码列表
prefixes = [
    'CHQ', 'QIN', 'HAX', 'CHU', 'CXU', 'CSN', 'CLU', 'CHW', 'CZN',
    'CBI', 'CDI', 'CLN', 'CEN', 'CHA', 'CGN', 'CQN', 'CGU', 'CJA',
    'CYN', 'CTN', 'CWU', 'CYU', 'CMI', 'CSU', 'CQO', 'CPN', 'CLO',
    'DAX', 'SHU', 'TAI', 'XBI', 'MIG'
]

# 源文件夹路径
source_folder = r'D:\Vic3.04CN\mod\DNCE1.09\gfx\flags'

# 目标文件夹路径
destination_folder = '../temp/flags'

# 创建目标文件夹（如果不存在）
os.makedirs(destination_folder, exist_ok=True)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 检查文件名是否以列表中的任何一个前缀开头
    if any(filename.startswith(prefix) for prefix in prefixes):
        # 构建完整的文件路径
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        # 复制文件
        shutil.copy2(source_path, destination_path)
        print(f'Copied: {filename}')

print('File copying completed.')