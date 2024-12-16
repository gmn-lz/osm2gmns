import csv
from shapely.geometry import LineString
from shapely.ops import unary_union

# 从CSV文件中读取轨迹数据
lines = []
with open('../map.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过标题行
    for row in reader:
        # 去除LINESTRING并提取坐标点
        coordinates = row[0].replace('LINESTRING(', '').replace(')', '').split(',')
        for coord in coordinates:
            x, y = coord.strip().split()
            print(f'X坐标: {x}, Y坐标: {y}')
        coordinates = [(float(row[i].strip()), float(row[i+1].strip())) for i in range(1, len(row), 2)]
        line = LineString(coordinates)
        lines.append(line)

# 将所有线合并为一个几何对象
merged_lines = unary_union(lines)

# 找出非联通的线
disconnected_lines = [line for line in lines if not merged_lines.contains(line)]

# 输出非联通的线
for line in disconnected_lines:
    print(line)