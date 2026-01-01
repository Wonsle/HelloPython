# 🐍 Python 30 天學習計劃 (30 Days of Python)

這是一份專為初學者設計的 Python 學習路徑，目標是在 30 天內從零基礎進步到能夠撰寫自動化腳本與進行簡單數據分析。

## 🍎 MacOS 環境準備 (Prerequisites)

在開始第一天之前，請打開你的終端機 (Terminal) 並確認以下設定：

1.  **檢查 Python 版本**：
    MacOS 通常內建 Python，但建議安裝最新的 Python 3。
    ```bash
    python3 --version
    ```
2.  **安裝開發工具 (如果是第一次寫程式)**：
    ```bash
    xcode-select --install
    ```
3.  **建議編輯器**：
    * [VS Code for Mac](https://code.visualstudio.com/) (強烈推薦)
    * 安裝 VS Code 後，請在擴充功能 (Extensions) 搜尋並安裝 "Python" (Microsoft 出品)。

---

## 📅 第一週：打好地基 (基礎語法與資料型態)
*目標：讓電腦聽懂你的指令，熟悉 Python 的語言結構。*

- [X] **Day 1: 環境建置與 Hello World**
    - 設定 VS Code 環境。
    - 建立第一個檔案 `hello.py`。
    - 終端機執行：`python3 hello.py`。
- [X] **Day 2: 變數與基本資料型態**
    - 整數 (`int`)、浮點數 (`float`)、字串 (`str`)、布林 (`bool`)。
    - 學習變數命名規則 (Snake Case, e.g., `user_name`)。
- [X] **Day 3: 數學運算與字串處理**
    - 加減乘除、取餘數 (`%`)。
    - f-string 格式化：`print(f"Hello, {name}")`。
    - 字串切片 (Slicing)：`text[0:5]`。
- [X] **Day 4: 列表 (Lists)**
    - 建立 List：`my_list = [1, 2, 3]`。
    - 方法：`append()`, `remove()`, `pop()`, `sort()`。
- [ ] **Day 5: 字典 (Dictionaries)**
    - Key-Value 概念：`user = {"name": "Alex", "age": 25}`。
    - 讀取與新增資料。
- [ ] **Day 6: 元組 (Tuples) 與 集合 (Sets)**
    - Tuple 的不可變性 (Immutable)。
    - 使用 Set 去除 List 中的重複值。
- [ ] **Day 7: 第一週總複習 & 實作**
    - 📝 **小專案：成績計算機** (輸入國英數成績，計算平均並判斷及格與否)。

## 🧠 第二週：掌握邏輯 (控制流程與函數)
*目標：學會控制程式的執行順序，並將重複的程式碼封裝成函數。*

- [ ] **Day 8: 條件判斷 (If / Elif / Else)**
    - 邏輯運算子：`and`, `or`, `not`。
- [ ] **Day 9: 迴圈 (For Loops)**
    - 遍歷 List 與 Dictionary。
    - `range(start, stop, step)` 的用法。
- [ ] **Day 10: 迴圈 (While Loops) 與 控制**
    - `while` 迴圈。
    - `break` (跳出) 與 `continue` (跳過這一次)。
- [ ] **Day 11: 函數基礎 (Functions)**
    - `def my_function():`。
    - 參數 (Arguments) 與 回傳值 (Return)。
- [ ] **Day 12: 進階函數與範圍 (Scope)**
    - 全域變數 (Global) vs 區域變數 (Local)。
    - 了解 `*args` (不定長度參數)。
- [ ] **Day 13: 錯誤處理 (Try / Except)**
    - 捕捉異常：`ZeroDivisionError`, `ValueError`。
    - 讓程式不會因為一個錯誤就閃退。
- [ ] **Day 14: 第二週總複習 & 實作**
    - 📝 **小專案：猜數字遊戲** (電腦隨機產生數字，使用者輸入猜測，提示太大或太小)。

## 🛠️ 第三週：進階工具 (模組、檔案與物件導向)
*目標：學會使用外部資源，處理檔案讀寫，並接觸物件導向概念。*

- [ ] **Day 15: 模組 (Modules) 與 Pip**
    - `import math`, `import random`。
    - MacOS 終端機安裝套件：`pip3 install requests`。
- [ ] **Day 16: 檔案讀寫 (File I/O)**
    - `open()`, `read()`, `write()`。
    - 上下文管理器：`with open('data.txt', 'w') as f:`。
- [ ] **Day 17: CSV 與 JSON 處理**
    - 處理試算表資料 (`csv` 模組)。
    - 處理 API 常用的資料格式 (`json` 模組)。
- [ ] **Day 18: 物件導向 (OOP) - 類別與物件**
    - 定義 Class 與 `__init__` 建構式。
    - 實例化 Object。
- [ ] **Day 19: OOP - 繼承與方法**
    - 父類別與子類別。
    - `self` 關鍵字的意義。
- [ ] **Day 20: 虛擬環境 (Virtual Environments)**
    - 建立：`python3 -m venv venv`。
    - 啟動 (Mac)：`source venv/bin/activate`。
- [ ] **Day 21: 第三週總複習 & 實作**
    - 📝 **小專案：簡易記帳程式** (使用 Class 管理帳目，並將資料儲存於 CSV 檔案)。

## 🚀 第四週：實戰應用 (自動化與數據入門)
*目標：整合所學，完成一個有實際功能的畢業專案。*

- [ ] **Day 22: 網路爬蟲基礎 (Web Scraping)**
    - 使用 `requests` 抓取網頁 HTML。
- [ ] **Day 23: 解析網頁數據**
    - 使用 `BeautifulSoup` 抓取特定標籤 (如新聞標題)。
- [ ] **Day 24: 數據分析入門 (Pandas)**
    - `pip3 install pandas`。
    - DataFrame 的基本操作。
- [ ] **Day 25: 數據視覺化 (Matplotlib)**
    - `pip3 install matplotlib`。
    - 繪製簡單的折線圖。
- [ ] **Day 26: 專案規劃**
    - 決定題目 (例如：股價爬蟲、自動整理檔案機器人)。
    - 規劃功能與資料結構。
- [ ] **Day 27: 專案開發 - 核心功能**
    - 撰寫主要的邏輯程式碼。
- [ ] **Day 28: 專案開發 - 介面與優化**
    - 優化使用者輸入體驗，加入錯誤處理。
- [ ] **Day 29: 專案測試與除錯**
    - 測試各種邊界情況 (Edge Cases)。
- [ ] **Day 30: 部署與 Git 基礎**
    - `git init`, `git add .`, `git commit -m "First commit"`。
    - 上傳至 GitHub 分享你的成果！

---

### 💡 MacOS 開發小撇步

* **快速開啟終端機**：按 `Command + Space`，輸入 "Terminal"。
* **路徑問題**：在終端機中，如果不知道檔案路徑，可以直接把檔案從 Finder **拖曳** 到終端機視窗中，它會自動貼上完整路徑。
* **權限問題**：如果在安裝套件時遇到 `Permission denied`，請檢查是否使用了虛擬環境，或在指令前加上 `sudo` (例如 `sudo pip3 install ...`，但建議優先使用虛擬環境)。