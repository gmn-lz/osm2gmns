import csv


def get_coordinates(traj):
    # 将轨迹数据切分为坐标对
    coordinates = [pair.split() for pair in traj.split(',')]
    return [(float(x), float(y)) for x, y in coordinates]


# 读取CSV文件
with open('../../osm2/output2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    # 获取所有轨迹数据
    trajectories = list(reader)

# 构建交点字典
intersection_dict = {}

for i in range(len(trajectories)):
    coords1 = get_coordinates(trajectories[i][0])

    for j in range(i + 1, len(trajectories)):
        coords2 = get_coordinates(trajectories[j][0])

        # 检查是否有公共交点
        for coord1 in coords1:
            if coord1 in coords2:
                if i not in intersection_dict:
                    intersection_dict[i] = set()
                intersection_dict[i].add(j)
                if j not in intersection_dict:
                    intersection_dict[j] = set()
                intersection_dict[j].add(i)
                break

# 查找连通的路线集合
visited = set()
connected_sets = []


def dfs(node, connected_set):
    visited.add(node)
    connected_set.add(node)

    if node in intersection_dict:
        for neighbor in intersection_dict[node]:
            if neighbor not in visited:
                dfs(neighbor, connected_set)


for i in range(len(trajectories)):
    if i not in visited:
        connected_set = set()
        dfs(i, connected_set)
        if connected_set:
            connected_sets.append(connected_set)

# 输出结果
for i, connected_set in enumerate(connected_sets):
    print(f"Connected Set {i + 1}: {', '.join(str(node) for node in connected_set)}")
