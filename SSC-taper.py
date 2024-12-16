import pya

# 创建一个新的布局对象
layout = pya.Layout()

# 创建一个新的单元格
cell = layout.create_cell("SSC_taper")

# 设置层
layer1 = layout.layer(11, 0)  # 第一层，使用层1和掩模0
layer2 = layout.layer(12, 0)  # 第二层，使用层2和掩模0
layer3 = layout.layer(13, 0)  # 第三层，使用层3和掩模0

# 第一层梯形参数
height1 = 200*1000 # 高度
top_width1 = 1.5*1000  # 上底
bottom_width1 = 450  # 下底

# 第二层梯形参数
height2 = 400*1000
top_width2 = 6*1000
bottom_width2 = 450

# 第三层梯形参数
height3 = 600*1000
top_width3 = 12*1000
bottom_width3 = 800

# 计算每层梯形的坐标，使其居中对齐
# 绘制第一层梯形
x1 = 0  # 上底左侧坐标
y1 = 0  # 梯形的起始y坐标
shape1 = pya.Polygon([
    pya.Point(x1, y1 + top_width1/2),
    pya.Point(x1, y1 - top_width1/2),
    pya.Point(x1 + height1, y1 - bottom_width1/2),
    pya.Point(x1 + height1, y1 + bottom_width1/2)
])
cell.shapes(layer1).insert(shape1)

# 绘制第二层梯形
x2 = 0
y2 = 0  
shape2 = pya.Polygon([
    pya.Point(x2, y2 + top_width2/2),
    pya.Point(x2, y2 - top_width2/2),
    pya.Point(x2 + height2, y2 - bottom_width2/2),
    pya.Point(x2 + height2, y2 + bottom_width2/2)
])
cell.shapes(layer2).insert(shape2)

# 绘制第三层梯形
x3 = 0
y3 = 0  
shape3 = pya.Polygon([
    pya.Point(x3, y3 + top_width3/2),
    pya.Point(x3, y3 - top_width3/2),
    pya.Point(x3 + height3, y3 - bottom_width3/2),
    pya.Point(x3 + height3, y3 + bottom_width3/2)
])
cell.shapes(layer3).insert(shape3)

# 保存布局到文件
layout.write("D:/daily_work/ledit_practice/klayout_py/SSC_taper.gds")

# 打印完成信息
print("三层梯形锥形布局已生成，并保存为 'SSC_taper' 文件。")