# テキストファイルの中にある各数字(0~9)をカウントし、
# 最後に各数字ごとのカウントを表示する。
# 数字でない文字は無視する。
# 例えば、円周率に現れる数字のばらつきを調べたりできる。

if __name__ == '__main__':
    counter = [0] * 10

with open("num_count_input.txt", mode='r') as f:
    for line in f:  # 1行ずつ
        for number in line:  # 1文字ずつ
            for i in range(10):  # 文字0~9と比較
                if number == str(i):
                    counter[i] += 1

for i, count in enumerate(counter):
    print(f'{i}: {count:4}')
