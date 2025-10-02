import streamlit as st

st.title("Momijiのホームページ")
st.header("ようこそ！")
st.write("ここはPythonだけで作ったホームページです。")

# 画像を表示
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXADv4Mi32xRaj4KmDgrup4ZVxqk2JiBw_vA&s", caption="かわいいかろん")

# ボタン
if st.button("押してみて"):
    st.write("こんにちは！ボタンを押してくれてありがとう！")
if st.button("押さないで")
if st.wirite("なんで押したの？")
# フォーム
name = st.text_input("あなたの名前は？")
if st.button("送信"):
    st.write(f"{name}さん、こんにちは！") # https://python-ddvmuygaameabr7brnygeh.streamlit.app/
