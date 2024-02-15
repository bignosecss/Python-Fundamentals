from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
my_map = Map()
# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖北省", 299),
    ("香港特别行政区", 399),
    ("台湾省", 499)
]
# 添加数据
my_map.add("测试地图", data, "china")
# 设置全局选项
my_map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)
# 绘图
my_map.render()
