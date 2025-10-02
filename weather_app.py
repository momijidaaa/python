import streamlit as st
import requests

st.title("大阪の天気")

api_key = "YOUR_API_KEY"
city = "Osaka"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja"
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    st.write(f"地域: {data['name']}")
    st.write(f"天気: {data['weather'][0]['description']}")
    st.write(f"気温: {data['main']['temp']}℃")
    st.write(f"湿度: {data['main']['humidity']}%")
else:
    st.error("天気情報が取得できませんでした")
