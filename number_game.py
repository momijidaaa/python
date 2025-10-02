import random

# 1～100のランダムな数字を作る
secret_number = random.randint(1, 100)

print("1～100の数字を当ててね！")

attempts = 0  # 試行回数

while True:
    guess = int(input("数字を入力: "))
    attempts += 1

    if guess < secret_number:
        print("もっと大きいよ！")
    elif guess > secret_number:
        print("もっと小さいよ！")
    else:
        print(f"正解！{attempts}回で当たったね！")
        break
