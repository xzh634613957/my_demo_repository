"""
    封装案例2: 摆放家具
"""
"""
    **需求**
        1. **房子(House)** 有 **户型**、**总面积** 和 **家具名称列表**
           * 新房子没有任何的家具
        2. **家具(HouseItem)** 有 **名字** 和 **占地面积**，其中
           *  **席梦思(bed)** 占地 `4` 平米
           *  **衣柜(chest)** 占地 `2` 平米
           *  **餐桌(table)** 占地 `1.5` 平米
        3. 将以上三件 **家具** **添加** 到 **房子** 中
        4. 打印房子时，要求输出：**户型**、**总面积**、**剩余面积**、**家具名称列表**
        
    **剩余面积**
        1. 在创建房子对象时，定义一个 **剩余面积的属性**，**初始值和总面积相等**
        2. 当调用 `add_item` 方法，向房间 **添加家具** 时，让 **剩余面积** -= **家具面积**
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占用的面积为: %.1f平米." % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型: %s\n" \
               "总面积: %.1f平米\n" \
               "剩余面积: %.1f平米\n" \
               "家具名称列表: %s" % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        self.item_list.append(item.name)
        self.free_area = self.free_area - item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

house1 = House("两室一厅", 100)
house1.add_item(bed)
house1.add_item(chest)
house1.add_item(table)
print(house1)
