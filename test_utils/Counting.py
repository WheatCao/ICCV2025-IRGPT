import json
import re
import numpy as np

def load_json(file_path):
    """
    读取 JSON 文件
    :param file_path: JSON 文件路径
    :return: JSON 数据（字典列表）
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def extract_number(s):
    """
    从字符串中提取 <num> 标签内的数字
    :param s: 输入字符串
    :return: 提取的数字（整数），如果未找到则返回 None
    """
    match = re.search(r'<num>(\d+)</num>', s)
    if match:
        return int(match.group(1))
    return None

def calculate_metrics(data):
    """
    计算人群计数任务的评估指标（MAE, MSE, RMSE）
    :param data: JSON 数据（字典列表）
    :return: MAE, MSE, RMSE
    """
    absolute_errors = []
    squared_errors = []

    for sample in data:
        pred = extract_number(sample['answer'])  # 提取模型预测的数字
        label = extract_number(sample['label'])  # 提取真实标签的数字

        if pred is not None and label is not None:
            absolute_errors.append(abs(pred - label))
            squared_errors.append((pred - label) ** 2)

    mae = np.mean(absolute_errors)  # 计算 MAE
    mse = np.mean(squared_errors)   # 计算 MSE
    rmse = np.sqrt(mse)             # 计算 RMSE

    return mae, mse, rmse

def evaluate_crowd_counting(file_path):
    """
    评估人群计数任务的模型性能
    :param file_path: JSON 文件路径
    :return: MAE, MSE, RMSE
    """
    data = load_json(file_path)  # 加载 JSON 数据
    mae, mse, rmse = calculate_metrics(data)  # 计算指标
    return {"MAE":mae, "MSE":mse, "RMSE":rmse}
