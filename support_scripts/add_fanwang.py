import os

# 要遍历的文件夹路径
folder_path = r'../temp/countries'

# 要插入的内容
insert_line = 'feudal_kingdom = {220 202 96}\n'

# 遍历指定文件夹中的所有文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # 检查是否为文件
    if os.path.isfile(file_path):
        # 读取文件内容
        with open(file_path, 'r', encoding='gb18030') as file:
            lines = file.readlines()
        
        # 在第二行之前插入新行
        if len(lines) >= 1:  # 确保文件至少有一行
            lines.insert(1, insert_line)  # 插入到索引1的位置，即第二行
        
        # 将修改后的内容写回文件
        with open(file_path, 'w', encoding='gb18030') as file:
            file.writelines(lines)

print("All files have been processed.")