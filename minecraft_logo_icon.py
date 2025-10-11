from PIL import Image, ImageDraw

# 画像サイズ
size = (128, 128)

# 背景色（マイクラっぽい緑）
background_color = (106, 190, 48)

# 画像作成
img = Image.new("RGB", size, background_color)
draw = ImageDraw.Draw(img)

# 土ブロック風の茶色部分
draw.rectangle([16, 64, 112, 120], fill=(156, 93, 82))

# 草部分（上部）
draw.rectangle([16, 32, 112, 64], fill=(106, 190, 48))

# 草のギザギザ（簡易）
draw.polygon([(16,64),(32,48),(48,64),(64,48),(80,64),(96,48),(112,64)], fill=(106, 190, 48))

# 枠線
draw.rectangle([16, 32, 112, 120], outline=(60, 60, 60), width=2)

# 保存
img.save("minecraft_logo_icon.png")
print("minecraft_logo_icon.png を作成しました")
