import numpy as np

# 文件路径
file1_path = 'G:/Implicit-Stacked-Autoregressive-Model-for-Video-Prediction-main (2)/data/seadata/sea_windv_data_init_716_asc/windu-2024-07-16T23-00-00.asc'
file2_path = 'G:/Implicit-Stacked-Autoregressive-Model-for-Video-Prediction-main (2)/data/seadata/ISAMseawindu_asc/wave-2024-07-16T23-00-00.asc'


# 读取文件数据并跳过元数据行的函数
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 跳过前6行（元数据），并将剩余行连接起来
    data_lines = lines[6:]
    data = ' '.join(data_lines).split()

    # 将数据转换为浮点数列表
    data = [float(value) for value in data]
    return data


# 读取两个文件的数据
data1 = read_data(file1_path)
data2 = read_data(file2_path)

# 确保两个数据集长度相同
if len(data1) != len(data2):
    raise ValueError("两个文件的数据点数量必须相同")

# 将列表转换为numpy数组以便更容易计算
data1 = np.array(data1)
data2 = np.array(data2)

# 计算 MAE 和 MSE
mae = np.mean(np.abs(data1 - data2))
mse = np.mean((data1 - data2) ** 2)

# 打印结果
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
