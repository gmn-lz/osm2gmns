import csv

file_path = r"C:\Users\48818\Desktop\WKT整合\ALLALL.wkt"  # 请替换为实际文件路径
output_file = "output3.csv"  # 输出CSV文件路径

data_list = []
current_data = ""

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith("LINESTRING") and current_data:
            data_list.append([current_data])
            current_data = ""
        current_data += line

if current_data:  # 处理最后一个数据
    data_list.append([current_data])

# 保存数据到CSV文件
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['WKT'])  # 添加表头信息
    for data in data_list:
        writer.writerow(data)

print("数据已保存到", output_file)
