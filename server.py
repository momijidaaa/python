from mcstatus import JavaServer, BedrockServer
import socket

print("=== Minecraft サーバーステータスチェッカー ===")
print("1. Java版")
print("2. 統合版 (Bedrock)")
choice = input("サーバーの種類を選択してください (1 or 2): ")

ip = input("サーバーのIPアドレスを入力してください: ")
port_input = input("ポート番号を入力してください（未入力なら自動で設定）: ")

# デフォルトポート設定
if choice == "1":
    port = int(port_input) if port_input else 25565
else:
    port = int(port_input) if port_input else 19132

# ホスト解決チェック
try:
    socket.gethostbyname(ip)
except socket.gaierror:
    print("\n❌ サーバーが見つかりません（IPまたはドメイン名が無効です）")
    exit()

# ポート接続確認（ホワイトリストでも稼働判定）
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if choice=="1" else socket.SOCK_DGRAM)
sock.settimeout(3)
try:
    sock.connect((ip, port))
    print("\n🎮 サーバーはオンラインです！（ホワイトリストの有無は不明）")
except Exception:
    print("\n⚠️ サーバーはオフラインか、ポートに接続できません")
finally:
    sock.close()
