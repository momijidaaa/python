import streamlit as st

st.title("Momijiのホームページ")
st.header("ようこそ！")
st.write("ここはPythonだけで作ったホームページです。")
st.write("ぜひ、いろいろなボタンを押してみてね！")


# ボタン
if st.button("押してみて"):
    st.write("こんにちは！ボタンを押してくれてありがとう！")
if st.button("押さないで"):
    st.write("なんで押したの？")
if st.button("810"):
    st.write("淫夢厨なんですか？")
if st.button(("押せよ"))
   st wirte("おめでとう！君は今日からアンパンマンだ！")
# フォーム入力
name = st.text_input("あなたの名前は？")
age = st.text_input("あなたの年齢は？")
job = st.selectbox("あなたの職業は？", ["選んでください", "学生", "会社員", "自営業", "その他"])
hobby = st.selectbox("あなたの趣味は？", ["選んでください", "ゲーム", "音楽", "プログラミング", "読書", "スポーツ"])

# 送信ボタン
if st.button("送信"):
    if not name or not age or job == "選んでください" or hobby == "選んでください":
        st.error("すべての項目を入力してください！")
    elif not age.isdigit():
        st.error("年齢は数字で入力してください！")
    else:
        age_int = int(age)
        
        # 年齢別メッセージ
        if age_int < 13:
            age_msg = "まだ小学生だね！"
        elif age_int < 16:
            age_msg = "中学生だね！"
        elif age_int < 20:
            age_msg = "高校生だね！"
        elif age_int < 30:
            age_msg = "大人だね！"
        elif age_int < 40:
            age_msg = "ばばぁだね！"
        else:
            age_msg = "老害じゃん！"
        
        # 最終メッセージ表示
        st.success(
            f"{name}さん、こんにちは！\n"
            f"君は{age_int}歳で {age_msg}\n"
            f"職業は {job} で、趣味は {hobby} なんだね！"
        )
