import argparse
import json
from lxml import etree
import glob
import shutil
import logging
import re
import csv
import pyproj

# def createargs():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--osm', required = True, type=str)
#     args = parser.parse_args()
#     return args

def getid2points(xml):
    nodes = {}
    ways = {}
    i = 0
    for idx, element in xml:
        if element.tag == "node":
            nodes[element.attrib["id"]] = [str(element.attrib["lat"]), str(element.attrib["lon"])]
        elif element.tag == "way":
            matching_elements = [ v.attrib['v']
                                  for i, v in enumerate(element)
                                  if v.tag == "tag" and v.attrib['k'] == 'name']
            if not matching_elements:
                name='road'+str(i)
                i=i+1
            else:
                name=matching_elements[0]
            print(name, idx)
            ways[element.attrib["id"]] = {}
            ways[element.attrib["id"]]["points"] = [ nodes[ v.attrib['ref'] ] for i, v in enumerate(element) if v.tag == "nd" ]
            ways[element.attrib["id"]]["name"] = name
    return ways

def createwkt(id2points, name):
    with open(name + '.kwt', 'w') as txtfile:
        for v in id2points:
            linestring = "LINESTRING("
            for idx, val in enumerate(id2points[v]["points"]):
                x, y = transformer.transform(val[1], val[0])  # val[1]为经度，val[0]为纬度
                linestring += f"{x} {y}, "
            linestring = linestring[0:len(linestring)-2]
            linestring+=' )'
            txtfile.write(f"{linestring}\n\n")  # 在每行数据之间加一个空行
def main(dirmap):
    # args = createargs()

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    logging.info('Reading {}.'.format(dirmap))

    xml = etree.iterparse((dirmap))

    id2points = getid2points(xml)
    logging.info('{} ways found.'.format(len(id2points)))

    createwkt(id2points, dirmap.split('/')[-1].split('.')[0])


if __name__ == '__main__':
# 定义经纬度和平面坐标系
    wgs84 = pyproj.CRS("EPSG:4326")  # WGS84经纬度坐标系
    utm = pyproj.CRS("EPSG:32632")   # UTM平面坐标系，这里以32N为例

    # 创建坐标转换器
    transformer = pyproj.Transformer.from_crs(wgs84, utm, always_xy=True)

    dirmap='map.osm'
    main(dirmap)

# 直接处理osm数据——有非联通的路网