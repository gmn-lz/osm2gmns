import csv

# 读取CSV文件并写入WKT文本文件
with open('../../osm2/mapcsv/new.csv', 'r') as csvfile, open('mapnew.wkt', 'w') as wktfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳过第一行
    for row in csvreader:
        if any(row):  # 检查是否有非空数据
            wktfile.write(','.join(row) + '\n\n')  # 将非空数据行插入到WKT文件中，并在每行数据之间加一个空行