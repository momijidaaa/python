import streamlit as st
import requests

st.title("大阪の天気")

# APIキー
api_key = "0d7002e49da20fd09d9deb50df3f9211"
city = "Osaka,JP"  # 国コード付きで正確に取得

# URLは https に変更
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja"

try:
    response = requests.get(url)
    data = response.json()
    
    # ステータスコード表示（デバッグ用）
    st.write("ステータスコード:", response.status_code)

    if response.status_code == 200:
        st.write(f"地域: {data['name']}")
        st.write(f"天気: {data['weather'][0]['description']}")
        st.write(f"気温: {data['main']['temp']}℃")
        st.write(f"湿度: {data['main']['humidity']}%")
    else:
        st.error(f"天気情報が取得できませんでした ({data.get('message', '不明なエラー')})")
except Exception as e:
    st.error(f"エラーが発生しました: {e}")
