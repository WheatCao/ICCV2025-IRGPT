import json

def calculate_accuracy(json_file):
    # 读取JSON文件
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    correct_predictions = 0
    total_samples = len(data)
    
    # 遍历每个样本
    for sample in data:
        if sample['answer'].strip() == sample['label'].strip():
            correct_predictions += 1
    
    # 计算准确率
    accuracy = correct_predictions / total_samples
    return accuracy
