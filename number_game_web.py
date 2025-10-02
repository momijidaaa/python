import streamlit as st
import random

# セッション状態でランダム数字を保持
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("数字当てゲーム（Web版）")
st.write("1～100の数字を当ててね！")

# 入力欄
guess = st.number_input("数字を入力", min_value=1, max_value=100, step=1)

# ボタンを押したら判定
if st.button("判定"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        st.write("もっと大きいよ！")
    elif guess > st.session_state.secret_number:
        st.write("もっと小さいよ！")
    else:
        st.write(f"正解！{st.session_state.attempts}回で当たったね！")
        # ゲームリセット用
        if st.button("もう一度遊ぶ"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
