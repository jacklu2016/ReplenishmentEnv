import pandas as pd

# 读取 Tab 分隔文件
df = pd.read_csv("sku3.demand.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.demand.csv", sep=',', index=False)

df = pd.read_csv("sku3.store1.info.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.store1.info.csv", sep=',', index=False)

df = pd.read_csv("sku3.store1.selling_price.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.store1.selling_price.csv", sep=',', index=False)

df = pd.read_csv("sku3.store2.info.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.store2.info.csv", sep=',', index=False)

df = pd.read_csv("sku3.store2.selling_price.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.store2.selling_price.csv", sep=',', index=False)

df = pd.read_csv("sku3.store3.info.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.store3.info.csv", sep=',', index=False)

df = pd.read_csv("sku3.store3.selling_price.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.store3.selling_price.csv", sep=',', index=False)

df = pd.read_csv("sku3.super_vendor.selling_price.csv", sep='\t')
# 保存为逗号分隔 CSV
df.to_csv("sku3.super_vendor.selling_price.csv", sep=',', index=False)



