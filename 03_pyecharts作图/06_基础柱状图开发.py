from pyecharts.charts import Bar
from pyecharts.options import *

# 构建柱状图对象
bar = Bar()

# 添加 x 轴数据
bar.add_xaxis(["中国", "美国", "日本"])
# 添加 y 轴数据
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转 x/y 轴
bar.reversal_axis()

# 绘图
bar.render("基础柱状图.html")
