import streamlit as st
import requests

st.title("天気予報Webアプリ")

# 入力欄
city_input = st.text_input("地域名を入力（例：Osaka, Tokyo, New York）")

# APIキー
api_key = "0d7002e49da20fd09d9deb50df3f9211"

if st.button("天気を表示"):
    if city_input:
        # 国コードを含む場合の処理
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}&units=metric&lang=ja"
        try:
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                st.write(f"地域: {data['name']}")
                st.write(f"天気: {data['weather'][0]['description']}")
                st.write(f"気温: {data['main']['temp']}℃")
                st.write(f"湿度: {data['main']['humidity']}%")
            else:
                st.error(f"天気情報が取得できませんでした ({data.get('message', '不明なエラー')})")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("地域名を入力してください")
