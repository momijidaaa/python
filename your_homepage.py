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
job = st.selectbox("あなたの職業は？", ["選んでください", "学生", "会社員", "自営業", "その他"])

# 送信ボタン
if st.button("送信"):
    if not name or not age or job == "選んでください":
        st.error("すべての項目を入力してください！")
    else:
        # 年齢は数字だけのときだけ評価
        if age.isdigit():
            age_int = int(age)
            st.write(
                f"{name}さん、こんにちは！ 君は{age_int}歳なんだね！"
                f"{' まだ若いね！' if age_int < 20 else ' 大人だね！'} "
                f"職業は {job} なんだね！"
            )
        else:
            st.error("年齢は数字で入力してください！")
