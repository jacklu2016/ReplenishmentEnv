
import numpy as np
import pandas as pd

size = 1219
# 生成正态分布数据
mu, sigma = 20, 5
data_normal = np.random.normal(loc=mu, scale=sigma, size=size * 3)

# 转换为 DataFrame 并保存为 CSV
df_normal = pd.DataFrame({'Normal_Data': np.round(data_normal[0: size - 1]),
                          'Normal_Data1': np.round(data_normal[size: size * 2 - 1]),
                          'Normal_Data2': np.round(data_normal[size * 2: size * 3 - 1])})
df_normal.to_csv('normal_distribution.csv', index=False)


# 生成泊松分布数据
lambda_ = 15
data_poisson = np.random.poisson(lam=lambda_, size=size * 3)

# 转换为 DataFrame 并保存为 CSV
#df_poisson = pd.DataFrame(data_poisson, columns=['Poisson_Data', 'Poisson_Data1', 'Poisson_Data2'])
df_poisson = pd.DataFrame({'Poisson_Data': np.round(data_poisson[0: size - 1]),
                          'Poisson_Data1': np.round(data_poisson[size: size * 2 - 1]),
                          'Poisson_Data2': np.round(data_poisson[size * 2: size * 3 - 1])})
df_poisson.to_csv('poisson_distribution.csv', index=False)


# 生成均匀分布数据
low, high = 0, 40
data_uniform = np.random.uniform(low=low, high=high, size=size * 3)

# 转换为 DataFrame 并保存为 CSV
#df_uniform = pd.DataFrame(data_uniform, columns=['Uniform_Data'])
df_uniform = pd.DataFrame({'Uniform_Data': np.round(data_uniform[0: size - 1]),
                          'Uniform_Data1': np.round(data_uniform[size: size * 2 - 1]),
                          'Uniform_Data2': np.round(data_uniform[size * 2: size * 3 - 1])})
df_uniform.to_csv('uniform_distribution.csv', index=False)


# 生成随机分布数据
n, p = 20, 0.5
data_random = np.random.randint(1, 40, size=size * 3)

# 转换为 DataFrame 并保存为 CSV
#df_binomial = pd.DataFrame(data_binomial, columns=['Binomial_Data'])
df_random = pd.DataFrame({'Uniform_Data': np.round(data_random[0: size - 1]),
                          'Uniform_Data1': np.round(data_random[size: size * 2 - 1]),
                          'Uniform_Data2': np.round(data_random[size * 2: size * 3 - 1])})
df_random.to_csv('randomm_distribution.csv', index=False)

# 合并所有数据
