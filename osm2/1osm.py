import osm2gmns as og
net = og.getNetFromFile('C:\\Users\\4881\\Desktop\\Test.xml')  #这里为 导出的Test.osm 更改后缀名后的文件目录
og.consolidateComplexIntersections(net, auto_identify=True)
og.outputNetToCSV(net,'testcsv')   #指定原始csv文件的目录：会生成一些csv的文件

import csv
# 打开原始CSV文件和创建新的CSV文件
with open('testcsv/link.csv', 'r') as file_in, open('outputTest.csv', 'w', newline='') as file_out:
    # 创建CSV读取器和写入器
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    # 获取原始CSV文件的列标题
    headers = next(reader)

    # 查找"geometry"字段所在的列索引——即线路图
    geometry_index = headers.index('geometry')

    # 写入新的CSV文件的列标题
    writer.writerow(['WKT'])

    # 处理每一行数据
    for row in reader:
        # 判断是否为空行
        if not all(cell.strip() == '' for cell in row):
            # 保留只包含"geometry"字段的数据
            new_row = [row[geometry_index]]
            writer.writerow(new_row)

# 操作说明：在OSM上导出区域的api数据，就是xml数据
# 进行提取路网
# 要将osm后缀改为xml
# 要将路网数据 表头加入wkt 才可以导入QGIS
# 保留只包含"geometry"字段的数据————得到output.csv

# 这块代码运行时间久，不要中止
