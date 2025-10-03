import random
import string

def random_string(length=8):
    chars = string.ascii_letters + string.digits  # 英数字
    return ''.join(random.choice(chars) for _ in range(length))

print("ランダム文字列:", random_string(12))
