# 导入 Line 功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 得到折线图对象
line = Line()
# 添加 X 轴数据
line.add_xaxis(["中国", "日本", "韩国", "中国台湾"])
# 添加 Y 轴数据
line.add_yaxis("GDP", [50, 40, 30, 20])

# 设置全局配置项 set_global_opts 来设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP Exhibition", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)


# 生成图表
line.render()
