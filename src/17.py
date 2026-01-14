"""
Day 17: CSV 與 JSON 處理**
  * 處理試算表資料 (`csv` 模組)。
  * 處理 API 常用的資料格式 (`json` 模組)。
"""

import csv
import json
from typing import List, Dict
from pprint import pprint

def read_csv(file_path: str) -> List[Dict[str, str]]:
    """讀取 CSV 檔案並回傳資料列表"""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
def write_csv(file_path: str, data: List[Dict[str, str]]) -> None:
    """將資料列表寫入 CSV 檔案"""
    if not data:
        return
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_json(file_path: str) -> Dict:
    """讀取 JSON 檔案並回傳資料"""
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data
def write_json(file_path: str, data: Dict) -> None:
    """將資料寫入 JSON 檔案"""
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    # CSV 範例
    csv_data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
    ]
    write_csv('example.csv', csv_data)
    read_data = read_csv('example.csv')
    print("CSV Data:")
    pprint(read_data)

    # JSON 範例
    json_data = {
        "employees": [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "Los Angeles"},
        ]
    }
    write_json('example.json', json_data)
    read_json_data = read_json('example.json')
    print("\nJSON Data:")
    pprint(read_json_data)