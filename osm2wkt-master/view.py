import geopandas as gpd
from shapely.wkt import loads
import matplotlib.pyplot as plt

# 读取WKT文件并创建GeoDataFrame
with open('133.wkt', 'r') as file:
    data = file.readlines()

geoms = [loads(line) for line in data if line.strip()]  # 从WKT创建几何对象
gdf = gpd.GeoDataFrame(geometry=geoms)

# 可视化轨迹数据
fig, ax = plt.subplots()
gdf.plot(ax=ax, color='blue', linewidth=2)
plt.show()