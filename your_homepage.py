import streamlit as st

st.title("Momijiのホームページ")
st.header("ようこそ！")
st.write("ここはPythonだけで作ったホームページです。")
st.write("ぜひ、いろいろなボタンを押してみてね！")

# 画像を表示
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXADv4Mi32xRaj4KmDgrup4ZVxqk2JiBw_vA&s", caption="かわいいかろん")

# ボタン
if st.button("押してみて"):
   st.write("こんにちは！ボタンを押してくれてありがとう！")
if st.button("押さないで"):
   st.write("なんで押したの？")
if st.button("810"):
   st.write("淫夢厨なんですか？")
# フォーム
name = st.text_input("あなたの名前は？")
age = st.text_input("あなたの年齢は？")
if st.button("送信"):
    st.write(f"{name}さん、こんにちは！ 君は{age}歳なんだね！") # https://python-ddvmuygaameabr7brnygeh.streamlit.app/
