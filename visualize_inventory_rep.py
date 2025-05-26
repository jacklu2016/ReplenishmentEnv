import  pandas as pd
import os
import matplotlib
matplotlib.use('TkAgg')  # ✅ 添加这一行

import matplotlib.pyplot as plt


# 设置全局字体为支持中文的字体
plt.rcParams['font.family'] = 'SimHei'
# 禁用 Unicode 减号，使用普通减号
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams.update({
    'axes.spines.top': False,  # 全局隐藏上边框
    'axes.spines.right': False,  # 全局隐藏右边框
})

state_line_style = [
    {'marker': '*', 'linestyle': '-', 'color': '#0000FF', 'label': 'demand'},
    {'marker': 'o', 'linestyle': '-', 'color': '#FF0000', 'label': 'in_stock'},
    {'marker': 's', 'linestyle': '-', 'color': '#006400', 'label': 'replenish'},
    {'marker': 'd', 'linestyle': '-', 'color': '#8B008B', 'label': '(s,Q)'}
]
def visualize(folder,algorithm):
    #读取store1 三个商品的demand，replenishment,stock
    path = os.path.join(folder, 'sku3.3_stores.standard', algorithm)

    store1_sku0_state = pd.read_csv(os.path.join(path, 'store1_SKU0.csv'))
    store1_sku1_state = pd.read_csv(os.path.join(path, 'store1_SKU1.csv'))
    store1_sku2_state = pd.read_csv(os.path.join(path, 'store1_SKU2.csv'))
    store2_state = pd.read_csv(os.path.join(path, 'store2_overview.csv'))
    stores_data = [store1_sku0_state, store1_sku1_state, store1_sku2_state, store2_state]

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    for i in range(len(stores_data)):
        ax = axes[i//2][i % 2]
        store_data = stores_data[i]
        for j in range(3):
            ax.plot(range(len(store1_sku0_state)),
                    store_data[state_line_style[j]["label"]],
                    color=state_line_style[j]['color'], marker=state_line_style[j]['marker'],
                    linestyle=state_line_style[j]['linestyle'],
                    alpha=.5, label=state_line_style[j]["label"])

        ax.legend(fontsize=16)
        ax.set_xlabel('时间', fontsize=16)
        ax.set_ylabel('药店库存', fontsize=16)
        ax.set_title(f'药店（{i}）库存',
                     y=-0.15,  # 负值下移标题
                     fontsize=16,
                     fontweight='bold',
                     verticalalignment='top')  # 文本顶部对齐坐标轴
    # 自动调整布局
    plt.subplots_adjust(hspace=0.2, wspace=0.3, top=0.9, bottom=0.1)
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    folder = 'output_demand_normal'
    visualize(folder, 'sS_hindsight')