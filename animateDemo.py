import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"C:\Windows\Fonts\simkai.ttf", size=10)

# 1. 定义数据（与图表关联）
data = {"项目一": 15, "项目二": 25, "项目三": 10, "项目四": 20}  # 可替换为你的真实数据
labels = list(data.keys())  # 项目名称（y轴标签）
values = list(data.values())  # 项目数值（条形长度）

# 2. 创建图表对象（调整尺寸更美观）
fig, ax = plt.subplots(figsize=(8, 5))  # 宽8英寸，高5英寸
ax.set_yticklabels(labels, fontproperties=font)  # Y轴类别标签用黑体
ax.set_title("项目数值对比", fontproperties=font, fontsize=14)  # 标题用黑体
# 3. 绘制水平条形图（匹配data数据）
y_pos = range(len(data))  # y轴位置（0~3，对应4个项目）
ax.barh(
    y=y_pos,               # 每个条形的y轴位置
    width=values,          # 条形长度（对应data数值）
    height=0.6,            # 条形厚度（调整为0.6更紧凑）
    color='#1f77b4',       # 条形颜色（ matplotlib默认蓝）
    alpha=0.8              # 透明度（0~1，0.8更柔和）
)

# 4. 设置轴标签与标题（让图表更清晰）
ax.set_yticks(y_pos)                  # 设置y轴刻度位置
ax.set_yticklabels(labels, fontsize=10)  # 用项目名称作为y轴标签
ax.set_xlabel('数值', fontsize=12)    # x轴标签（数值）
ax.set_title('项目数值对比', fontsize=14, fontweight='bold')  # 图表标题（加粗）

# 5. 添加文本（可选，增强视觉重点）
ax.text(
    x=0.85, y=0.15,          # 文本位置（相对于轴的比例，0.85=x轴85%，0.15=y轴15%）
    s='Python',              # 文本内容
    fontsize=20,             # 字体大小
    color='#ff7f0e',         # 文本颜色（橙色）
    ha='center',             # 水平对齐（居中）
    va='bottom',             # 垂直对齐（底部）
    transform=ax.transAxes   # 使用轴坐标（避免绝对数值）
)

# 6. 保存图表（关键：在plt.show()前保存，否则无法生成文件）
plt.savefig(
    'project_chart.png',    # 保存文件名（PNG格式，清晰度高）
    dpi=300,                # 分辨率（300DPI适合打印/展示）
    bbox_inches='tight'     # 自动裁剪图表边缘（避免标签被截断）
)

# 7. 显示图表（可选，运行时会弹出窗口）
plt.show()
