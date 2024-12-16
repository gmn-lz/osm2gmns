import pyproj

def convert_to_web_mercator(latitude, longitude):
    # 定义原始的经纬度坐标系统和目标Web墨卡托投影坐标系统
    crs_wgs84 = pyproj.CRS("EPSG:4326")  # WGS84经纬度坐标系
    crs_web_mercator = pyproj.CRS("EPSG:3857")  # Web墨卡托投影坐标系

    # 创建转换器
    transformer = pyproj.Transformer.from_crs(crs_wgs84, crs_web_mercator, always_xy=True)

    # 进行坐标转换
    web_mercator_coords = transformer.transform(longitude, latitude)

    return web_mercator_coords

# 给定经纬度
loc=[
    31.763331,117.288501
]

# 转换为Web墨卡托投影坐标
web_mercator_coords = convert_to_web_mercator(loc[0], loc[1])
print(web_mercator_coords)
