import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from matplotlib.font_manager import FontProperties
data = {"项目一":40,"项目二":20}
fig,ax = plt.subplots()

font = FontProperties(fname="")

ax.text(0.8,0.2,"python",ha="center",va="bottom",transform=ax.transAxes,fontsize=20,)
ax.barh(y=[5,10,15,20],width=[10,10,20,20])
plt.show()