import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
f_jp = open("D:\BaiduNetdiskDownload\资料\可视化案例数据\折线图数据\日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()  # Japan

f_us = open("D:\BaiduNetdiskDownload\资料\可视化案例数据\折线图数据\美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()  # America

f_in = open("D:\BaiduNetdiskDownload\资料\可视化案例数据\折线图数据\印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()  # India

# 去掉不合 JSON 规范的开头
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 去掉不合 JSON 规范的结尾
jp_data = jp_data[:-2]
us_data = us_data[:-2]
in_data = in_data[:-2]

# 将 JSON 转 Python 字典
jp_dict = json.loads(jp_data)
us_dict = json.loads(us_data)
in_dict = json.loads(in_data)

# 获取 trend key
jp_trend_data = jp_dict['data'][0]['trend']
us_trend_data = us_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于 x 轴，取 2020 年(到 314 下标结束)
jp_x_data = jp_trend_data['updateDate'][:314]
us_x_data = us_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据，用于 y 轴，取 2020 年(到 314 下标结束)
jp_y_data = jp_trend_data['list'][0]['data'][:314]
us_y_data = us_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()  # 构建折线图对象
# 添加 x 轴数据
line.add_xaxis(us_x_data)  # x 轴是公用的，使用一个国家的数据即可
# 添加 y 轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 添加全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")

)

# 调用 render 方法生成图表
line.render()

# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()
