import os
import shutil

# 三字母代码列表
prefixes = [
    'CHQ', 'QIN', 'HAX', 'CHU', 'CXU', 'CSN', 'CLU', 'CHW', 'CZN',
    'CBI', 'CDI', 'CQI', 'CEN', 'CHA', 'CGN', 'CQN', 'CGU', 'CJA',
    'CYN', 'CTN', 'CWU', 'CYU', 'CMI', 'CSU', 'CQO', 'CPN', 'CLO',
    'DAX', 'SHU', 'TAI', 'XBI', 'MIG'
]

correspondence = {
    "CHQ": "QiGuo",
    "QIN": "QinGuo",
    "HAX": "JinGuo",
    "CHU": "ChuGuo",
    "CXU": "XuGuo",
    "CSN": "SongGuo",
    "CLU": "LuGuo",
    "CHW": "WeyGuo",
    "CZN": "WeiGuo",
    "CBI": "BaiGuo",
    "CDI": "DaiGuo",
    "CQI": "QingGuo",
    "CEN": "ChenGuo",
    "CHA": "HuangGuo",
    "CGN": "GanGuo",
    "CQN": "DianGuo",
    "CGU": "GuiGuo",
    "CJA": "JiangGuo",
    "CYN": "KuiGuo",
    "CTN": "TangGuo",
    "CWU": "WuGuo",
    "CYU": "YueGuo",
    "CMI": "FuGuo",
    "CSU": "ShuGuo",
    "CQO": "QiongGuo",
    "CPN": "NingGuo",
    "CLO": "LiaoGuo",
    "DAX": "ShuGuo",
    "SHU": "YanGuo",
    "TAI": "ZhouGuo",
    "XBI": "SuGuo",
    "MIG": "MingGuo"
}

# 源文件路径
source_file = r'..\history\countries\CHQ - Qiguo.txt'

# 目标文件夹路径
destination_folder = r'..\temp\history'

# 创建目标文件夹（如果不存在）
os.makedirs(destination_folder, exist_ok=True)

# 读取源文件
with open(source_file, 'r') as file:
    content = file.read()

# 遍历三字母代码列表，重命名并复制文件
for prefix in prefixes:
    # 构建新的文件名
    new_filename = f'{prefix} - {correspondence[prefix]}.txt'
    
    # 构建目标文件路径
    destination_path = os.path.join(destination_folder, new_filename)
    
    # 写入内容到新文件
    with open(destination_path, 'w') as new_file:
        new_file.write(content)
    
    # print(f'{prefix} = \"countries\{correspondence[prefix]}.txt\"')

print('File renaming and copying completed.')