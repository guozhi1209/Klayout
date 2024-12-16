import pya

# 创建一个新的布局对象
layout = pya.Layout()

# 创建一个新的单元格
cell = layout.create_cell("trapezoidal_cone_layers")

# 设置层
layer1 = layout.layer(1, 0)  # 第一层，使用层1和掩模0
layer2 = layout.layer(2, 0)  # 第二层，使用层2和掩模0
layer3 = layout.layer(3, 0)  # 第三层，使用层3和掩模0

# 第一层梯形参数
height1 = 200  # 高度
top_width1 = 1.5  # 上底
bottom_width1 = 0.45  # 下底

# 第二层梯形参数
height2 = 400
top_width2 = 6
bottom_width2 = 0.45

# 第三层梯形参数
height3 = 600
top_width3 = 12
bottom_width3 = 0.8

# 计算每层梯形的坐标，使其居中对齐
# 绘制第一层梯形
x1 = -top_width1 / 2  # 上底左侧坐标
y1 = 0  # 梯形的起始y坐标
shape1 = pya.Polygon([
    pya.Point(x1, y1),
    pya.Point(x1 + top_width1, y1),
    pya.Point(x1 + bottom_width1, y1 + height1),
    pya.Point(x1 - bottom_width1, y1 + height1)
])
cell.shapes(layer1).insert(shape1)

# 绘制第二层梯形
x2 = -top_width2 / 2
y2 = height1  # 第二层的y坐标是第一层的顶部y坐标
shape2 = pya.Polygon([
    pya.Point(x2, y2),
    pya.Point(x2 + top_width2, y2),
    pya.Point(x2 + bottom_width2, y2 + height2),
    pya.Point(x2 - bottom_width2, y2 + height2)
])
cell.shapes(layer2).insert(shape2)

# 绘制第三层梯形
x3 = -top_width3 / 2
y3 = height1 + height2  # 第三层的y坐标是第二层的顶部y坐标
shape3 = pya.Polygon([
    pya.Point(x3, y3),
    pya.Point(x3 + top_width3, y3),
    pya.Point(x3 + bottom_width3, y3 + height3),
    pya.Point(x3 - bottom_width3, y3 + height3)
])
cell.shapes(layer3).insert(shape3)

# 保存布局到文件
layout.write("trapezoidal_cone_layers.gds")

# 打印完成信息
print("三层梯形锥形布局已生成，并保存为 'trapezoidal_cone_layers.gds' 文件。")
