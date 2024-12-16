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