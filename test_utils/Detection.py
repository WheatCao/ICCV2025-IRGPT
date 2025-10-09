
import json
import re
from typing import List, Tuple, Dict
import ast

def extract_boxes(s: str) -> List[Tuple[int, int, int, int]]:
    # 找到列表的起始和结束位置
    start = s.find('[')
    end = s.rfind(']') + 1

    # 如果找不到闭合的 ]，则尝试补全
    if end == 0:  # 如果没找到 ]
        # 补全一个 ]
        s = s + ']'
        end = len(s)

    # 提取列表字符串
    list_str = s[start:end]

    # 检查 [ 和 ] 的数量是否匹配
    open_brackets = list_str.count('[')
    close_brackets = list_str.count(']')

    # 如果不匹配，补全缺失的 ]
    if open_brackets > close_brackets:
        list_str += ']' * (open_brackets - close_brackets)

    try:
        # 尝试解析为列表
        list_of_lists = ast.literal_eval(list_str)
        return list_of_lists
    except (ValueError, SyntaxError):
        # 如果解析失败，返回 None 或空列表
        return None
    # """从文本中提取边界框，并清理多余字符"""
    # boxes = re.findall(r'\[([^\]]+)\]', text)  # 提取边界框内容
    # cleaned_boxes = []
    # for box in boxes:
    #     # 清理多余字符（如空格和多余的符号）
    #     box = box.replace(' ', '').strip('[]')
    #     if box:  # 确保非空
    #         cleaned_boxes.append(box)
    # return [tuple(map(int, box.split(','))) for box in cleaned_boxes]

def calculate_iou(box1: Tuple[int, int, int, int], box2: Tuple[int, int, int, int]) -> float:
    """计算两个边界框的 IoU"""
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    inter_area = max(0, x2 - x1) * max(0, y2 - y1)
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    
    iou = inter_area / (box1_area + box2_area - inter_area)
    return iou

def calculate_sample_accuracy(pred_boxes: List[Tuple[int, int, int, int]], true_boxes: List[Tuple[int, int, int, int]], iou_threshold: float = 0.5) -> float:
    """计算单个样本的检测精度"""
    correct = 0
    for true_box in true_boxes:
        max_iou = 0
        best_match = None
        for pred_box in pred_boxes:
            iou = calculate_iou(true_box, pred_box)
            if iou > max_iou:
                max_iou = iou
                best_match = pred_box
        if max_iou >= iou_threshold:
            correct += 1
            pred_boxes.remove(best_match)  # 防止重复匹配
    return correct / len(true_boxes) if len(true_boxes) > 0 else 0

def evaluate_detection_accuracy(json_file: str, iou_threshold: float = 0.5) -> float:
    """计算整个 JSON 文件中所有样本的平均检测精度"""
    with open(json_file, 'r') as f:
        data = json.load(f)  # 读取 JSON 文件
    
    total_accuracy = 0
    num_samples = len(data)
    
    for sample in data:
        pred_boxes = extract_boxes(sample.get("answer", ""))
        true_boxes = extract_boxes(sample.get("label", ""))
        sample_accuracy = calculate_sample_accuracy(pred_boxes, true_boxes, iou_threshold)
        total_accuracy += sample_accuracy
    
    average_accuracy = total_accuracy / num_samples if num_samples > 0 else 0
    return average_accuracy
