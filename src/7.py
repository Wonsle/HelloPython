"""
Day 7: 第一週總複習 & 實作
"""

input_scores = input("請輸入國文、英文、數學成績，以逗號分隔: ")
scores_list = input_scores.split(",")

if len(scores_list) != 3:
    print("請輸入三個成績。")
else:
    try:
        scores = [float(score) for score in scores_list]
        average_score = sum(scores) / len(scores)
        print(f"平均成績: {average_score:.2f}")

        if average_score >= 60:
            print("及格")
        else:
            print("不及格")
    except ValueError:
        print("請確保輸入的成績都是數字。")