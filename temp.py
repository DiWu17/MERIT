import os

# 指定要读取的目录
directory = "./data/feta/test"

# 获取目录下的所有文件名
filenames = os.listdir(directory)

# 指定要写入的文件
output_file = "D:/python/MERIT-main/lists/lists_Synapse/test_vol.txt"

# 将文件名写入到文件中
with open(output_file, "w") as f:
    for filename in filenames:
        f.write(filename + "\n")