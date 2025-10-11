import random

choices = ["グー", "チョキ", "パー"]

print("=== じゃんけんゲーム ===")
while True:
    user = input("手を入力してください（グー/チョキ/パー、終了はq）: ")
    if user.lower() == "q":
        print("ゲームを終了します。")
        break
    if user not in choices:
        print("無効な入力です。もう一度入力してください。")
        continue

    computer = random.choice(choices)
    print(f"コンピューターの手: {computer}")

    if user == computer:
        print("あいこ！")
    elif (user == "グー" and computer == "チョキ") or \
         (user == "チョキ" and computer == "パー") or \
         (user == "パー" and computer == "グー"):
        print("あなたの勝ち！🎉")
    else:
        print("あなたの負け…😢")

    print("-" * 20)
