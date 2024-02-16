import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open("../assets/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 全部数据
# 关闭文件
f.close()
# 取到各省份的数据
data_dict = json.loads(data)
# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装各个省份和确诊人数为元组，并将各个省的数据都封装如列表内
data_list = []  # 绘图需要用到的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    # 由于新版 pyecharts 显示地图中各个地区的全称，'疫情.txt' 中的 JSON 数据需要加上省略的部分
    if province_name == "新疆":
        province_name += "维吾尔自治区"
    elif province_name == "西藏" or province_name == "内蒙古":
        province_name += "自治区"
    elif province_name == "北京" or province_name == "上海" or province_name == "重庆" or province_name == "天津":
        province_name += "市"
    elif province_name == "宁夏":
        province_name += "回族自治区"
    elif province_name == "广西":
        province_name += "壮族自治区"
    elif province_name == "香港" or province_name == "澳门":
        province_name += "特别行政区"
    else:
        data_list.append((province_name+"省", province_confirm))
    data_list.append((province_name, province_confirm))

# 创建地图对象
my_map = Map()
# 添加数据
my_map.add("各省份确诊人数", data_list, "china")
# 设置全局配置，定制分段的视觉映射
my_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-499", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "label": ">100000", "color": "#990033"}
        ]
    )
)
# 生成图表
my_map.render("全国疫情地图.html")
