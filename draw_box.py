
import pya
##插入模块
layout=pya.Layout()
##建立layout文件
Top_cell=layout.create_cell("Top_cell")
##建立Top_cell原胞
l_PP=layout.layer(197,0,"PP")
##建立PP图层
Box_PP=pya.Box(0,0,50*1000,50*1000)
##绘制正方形，边长为50um
Box_cell=Top_cell.shapes(l_PP).insert(Box_PP)
##将正方形插入到l_PP层
layout.write("Box.gds")
##将文件保存为Box

import klayout.db as db #导入klayout的db模块

poly = db.DPolygon([ 
  db.DPoint(0, 0), db.DPoint(0, 5), db.DPoint(4, 5), db.DPoint(4, 4),
  db.DPoint(1, 4), db.DPoint(1, 3), db.DPoint(3, 3), db.DPoint(3, 2),
  db.DPoint(1, 2), db.DPoint(1, 0)
])

# rotate by 90 degree counterclockwise逆时针旋转90度

t1 = db.DTrans.R90
rotated_poly = t1 * poly

# rotate by 90 degree counterclockwise and shift by 10 µm to the right
# and 5 µm up逆时针旋转90度，并向右移动10微米，向上移动5微米

t2 = db.DTrans(db.DTrans.R90, 10.0, 5.0)
transformed_poly = t2 * poly

Top_cell.shapes(l_PP).insert(poly)
Top_cell.shapes(l_PP).insert(rotated_poly)
Top_cell.shapes(l_PP).insert(transformed_poly)
layout.write("polygons.gds")