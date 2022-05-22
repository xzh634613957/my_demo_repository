
import math
import matplotlib.pyplot as plt

class AStarPlanner:
    
    def __init__(self, ox, oy, resolution, robot_radius):
        self.ox = ox
        self.oy = oy
        # 栅格地图的大小
        self.min_x = round(min(self.ox))  # round()用于返回四舍五入的浮点数
        self.min_y = round(min(self.oy))
        self.max_x = round(max(self.ox))
        self.max_y = round(max(self.oy))
        # 每个栅格的大小（分辨率）
        self.resolution = resolution
        # 机器人半径
        self.robot_radius = robot_radius
        # x方向上的栅格个数和y方向上的栅格个数
        self.width_x = round((self.max_x - self.min_x) / self.resolution)
        self.height_y = round((self.max_y - self.min_y) / self.resolution)
        # 用二维数组表示每个栅格是否有障碍物（全部初始化为Fasle）
        self.obstacle_map = [[False for _ in range(self.width_x)] for _ in range(self.height_y)]
        # 膨胀障碍物
        self.get_obstacle_map()
        # 机器人运动方式（八连通）[dx, dy, cost]
        self.motion = [[1, 0, 1],
                       [-1, 0, 1],
                       [0, 1, 1],
                       [0, -1, 1],
                       [1, 1, math.sqrt(2)],
                       [1, -1, math.sqrt(2)],
                       [-1, -1, math.sqrt(2)],
                       [-1, 1, math.sqrt(2)]]

    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # 数组中x方向的索引
            self.y = y  # 数组中y方向的索引
            self.cost = cost
            self.parent_index = parent_index  # 父节点在整个栅格中的索引值

    def get_obstacle_map(self):
        # 计算每个栅格中心在原图中的坐标
        for i in range(self.width_x):
            x = self.calculate_position(i, self.min_x)
            for j in range(self.height_y):
                y = self.calculate_position(j, self.min_y)
                # 检查每个障碍物的坐标与每个栅格的坐标之间的距离是否小于机器人半径（障碍物膨胀）
                for iox, ioy in zip(self.ox, self.oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.robot_radius:
                        self.obstacle_map[i][j] = True
                        break
                        
    def planning(self, sx, sy, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gx: goal x position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """
        start_node = self.Node(self.calculate_xy_index(sx, self.min_x), self.calculate_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calculate_xy_index(gx, self.min_x), self.calculate_xy_index(gy, self.min_y), 0.0, -1)
        # 待扩展列表open_set，已扩展列表closed_set
        open_set, closed_set = dict(), dict()
        # 将节点在栅格中唯一的索引值作为key
        open_set[self.calculate_index(start_node)] = start_node

        while True:
            # 弹出open_set中cost最小的节点
            # min(iterable, *[, key, default])，传入可迭代对象，按key函数指定的方法取最小值
            # 最终返回的是open_set中cost最小节点的key，即该节点在整个栅格中的唯一索引
            c_id = min(open_set, key=lambda o: open_set[o].cost + self.calculate_heuristic(goal_node, open_set[o]))
            current = open_set[c_id]

            # show graph
            plt.plot(self.calculate_position(current.x, self.min_x), self.calculate_position(current.y, self.min_y), "xc")
            # 当closed_set中的节点的数量每增加10个绘图一次
            if len(closed_set.keys()) % 10 == 0:
                plt.pause(0.001)

            # 若弹出的节点为终点则退出while循环
            if current.x == goal_node.x and current.y == goal_node.y:
                print("Find goal")
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break
            
            # 如果弹出的节点不是终点，则对该节点进行扩展(根据motion定义的八种运动方式)
            for dx, dy, cost in self.motion:
                # 根据不同的运动方式创建不同的子节点对象
                node = self.Node(current.x + dx, current.y + dy, current.cost + cost, c_id)
                # 计算出子节点在整个栅格中的唯一索引
                n_id = self.calculate_index(node)

                # 判断子节点是否在已扩展列表closed_set中(是否被其他节点发现并扩展过)，若已被扩展过则直接进入下一for循环
                if n_id in closed_set:
                    continue
                
                # 判断子节点的位置是否超出限制范围或在障碍物上，若是则直接进入下一for循环
                if not self.verify_node(node):
                    continue
                
                # 判断子节点是否在待扩展列表open_set中(是否被其他节点发现但未扩展过)
                # 若不在则表明该节点为新节点，将其加入到待扩展列表中
                if n_id not in open_set:
                    open_set[n_id] = node
                # 若在则表明该节点被其他节点发现过，需要比较从其他节点到该子节点的cost，和从当前节点到该子节点的cost
                # 当从当前节点到该子节点的cost较小时，将子节点的cost值和父节点索引更新
                else:
                    if open_set[n_id].cost >= node.cost:
                        open_set[n_id] = node

            # 从open_set中移除当前节点并放入到closed_set中
            del open_set[c_id]
            closed_set[c_id] = current

        # 循环结束后通过父节点的索引计算最终的路径坐标
        # 初始化rx,ry及父节点索引
        rx, ry = [self.calculate_position(goal_node.x, self.min_x)], [self.calculate_position(goal_node.y, self.min_y)]
        parent_index = goal_node.parent_index
        # 从终点循环至起点
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calculate_position(n.x, self.min_x))
            ry.append(self.calculate_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    def calculate_position(self, index, minp):
        """
            返回节点所占栅格在坐标系中的坐标值(x,y)
        """
        return index * self.resolution + minp

    def calculate_xy_index(self, position, minp):
        """
            返回该节点在栅格数组中的下标(x方向的栅格索引,y方向的栅格索引)
        """
        return round((position - minp) / self.resolution)

    def calculate_index(self, node):
        """
            返回该节点在整个栅格中的唯一索引(index)
        """
        return node.y * self.width_x + node.x

    def calculate_heuristic(self, node1, node2):
        """
            启发式函数(欧式距离)
        """
        w1 = 1.0
        d = w1 * math.hypot(self.calculate_position(node1.x, self.min_x) - self.calculate_position(node2.x, self.min_x), 
                            self.calculate_position(node1.y, self.min_y) - self.calculate_position(node2.y, self.min_y))
        return d
    
    def verify_node(self, node):
        """
            判断节点的位置坐标是否超出界限或在障碍物上
        """
        px = self.calculate_position(node.x, self.min_x)
        py = self.calculate_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        if px >= self.max_x:
            return False
        if py < self.min_y:
            return False
        if py >= self.max_y:
            return False
        if self.obstacle_map[node.x][node.y]:
            return False

        return True



if __name__ == '__main__':
    
    sx = 0.0
    sy = 0.0
    gx = 50.0
    gy = 50.0
    grid_size = 2.0
    robot_radius = 1.0

    ox, oy = [], []
    for i in range(-10, 60):
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 61):
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60):
        ox.append(i)
        oy.append(60.0)
    for i in range(-9, 60):
        ox.append(-10.0)
        oy.append(i)
    for i in range(-10, 40):
        ox.append(10.0)
        oy.append(i)
    for i in range(20, 60):
        ox.append(40.0)
        oy.append(i)
    
    plt.plot(ox, oy, '.k')
    plt.plot(sx, sy, 'og')
    plt.plot(gx, gy, 'xb')
    plt.axis('square')

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    plt.plot(rx, ry, "-r")
    plt.pause(0.01)
    plt.show()
