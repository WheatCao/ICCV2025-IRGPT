
import json
import re
import ast
import math

def distance(p1, p2):
    """计算两个点之间的欧氏距离"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def extract_points(s):
    """从字符串中提取<pos>标签内的点列表"""
    pattern = r'<pos>(.*?)</pos>'
    match = re.search(pattern, s)
    if match:
        pos_str = match.group(1)
        try:
            points = ast.literal_eval(pos_str)
            # 验证格式是否正确
            if isinstance(points, list) and all(isinstance(p, tuple) and len(p) == 2 for p in points):
                return points
            else:
                return []
        except (SyntaxError, ValueError):
            return []
    else:
        return []

def match_points(gt_points, pred_points, threshold):
    """
    匹配真实点和预测点，确保每个真实点匹配到最近的预测点，且每个预测点只能匹配一次。
    返回匹配对、未匹配的真实点和未匹配的预测点。
    """
    matches = []  # 存储匹配对 (gt_point, pred_point, distance)
    gt_matched = [False] * len(gt_points)  # 标记真实点是否已匹配
    pred_matched = [False] * len(pred_points)  # 标记预测点是否已匹配

    # 遍历所有真实点和预测点，找到距离最近的匹配对
    for i, gt in enumerate(gt_points):
        min_dist = float('inf')
        best_match = None
        for j, pred in enumerate(pred_points):
            if not pred_matched[j]:  # 预测点未被匹配
                dist = distance(gt, pred)
                if dist < min_dist and dist <= threshold:
                    min_dist = dist
                    best_match = j
        if best_match is not None:
            matches.append((gt, pred_points[best_match], min_dist))
            gt_matched[i] = True
            pred_matched[best_match] = True

    # 未匹配的真实点和预测点
    unmatched_gt = [gt_points[i] for i, matched in enumerate(gt_matched) if not matched]
    unmatched_pred = [pred_points[j] for j, matched in enumerate(pred_matched) if not matched]

    return matches, unmatched_gt, unmatched_pred

def evaluate_json(json_file, threshold=5.0):
    """
    评估JSON文件中模型预测结果的有效性。
    输入:
        json_file: JSON文件路径
        threshold: 匹配阈值，默认5.0
    输出:
        包含精确率、召回率、F1分数、全局平均距离和样本平均MAE的字典
    """
    # 读取JSON数据
    with open(json_file, 'r') as f:
        data = json.load(f)

    total_TP = 0
    total_FP = 0
    total_FN = 0
    total_distance = 0.0
    sample_mae_sum = 0.0  # 所有样本MAE总和
    valid_samples = 0      # 有效样本数（有匹配点的样本）

    for item in data:
        # 提取真实点和预测点
        gt_points = extract_points(item['label'])
        pred_points = extract_points(item['answer'])
        
        # 匹配点
        matches, unmatched_gt, unmatched_pred = match_points(gt_points, pred_points, threshold)
        
        # 统计匹配结果
        num_matches = len(matches)
        total_TP += num_matches
        total_FP += len(unmatched_pred)
        total_FN += len(unmatched_gt)
        
        # 累加全局匹配距离
        if num_matches > 0:
            total_distance += sum(dist for _, _, dist in matches)
            # 计算当前样本的MAE并累加
            sample_mae = sum(dist for _, _, dist in matches) / num_matches
            sample_mae_sum += sample_mae
            valid_samples += 1

    # 计算全局指标
    precision = total_TP / (total_TP + total_FP) if (total_TP + total_FP) > 0 else 1.0
    recall = total_TP / (total_TP + total_FN) if (total_TP + total_FN) > 0 else 1.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    avg_distance = total_distance / total_TP if total_TP > 0 else 0.0
    
    # 计算样本平均MAE（只统计有匹配的样本）
    avg_sample_mae = sample_mae_sum / valid_samples if valid_samples > 0 else 0.0

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "average_distance": avg_distance,
        "average_sample_mae": avg_sample_mae
    }

# 示例调用
if __name__ == "__main__":
    json_file = "data.json"  # JSON文件路径
    results = evaluate_json(json_file, threshold=5.0)
    print("Evaluation Results:")
    print(f"Precision: {results['precision']:.4f}")
    print(f"Recall: {results['recall']:.4f}")
    print(f"F1 Score: {results['f1_score']:.4f}")
    print(f"Global Average Distance: {results['average_distance']:.2f} pixels")
    print(f"Sample-wise Average MAE: {results['average_sample_mae']:.2f} pixels")
