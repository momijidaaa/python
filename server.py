from mcstatus import JavaServer, BedrockServer
import socket
import re

def get_server_info():
    while True:
        print("\n=== Minecraft サーバーステータスチェッカー ===")
        print("1. Java版")
        print("2. 統合版 (Bedrock)")
        choice = input("サーバーの種類を選択してください (1 or 2): ")

        if choice not in ["1", "2"]:
            print("❌ 無効な選択です。最初からやり直します。")
            continue

        ip = input("サーバーのIPアドレスを入力してください: ")
        port_input = input("ポート番号を入力してください（未入力なら自動で設定）: ")

        port = int(port_input) if port_input else (25565 if choice=="1" else 19132)

        # ホスト解決チェック
        try:
            socket.gethostbyname(ip)
        except socket.gaierror:
            print("❌ サーバーが見つかりません。最初からやり直します。")
            continue

        try:
            if choice == "1":
                server = JavaServer.lookup(f"{ip}:{port}")
                status = server.status()
                print("\n🎮 サーバー状態: オンライン")
                print(f"バージョン: {status.version.name}")
                print(f"プレイヤー数: {status.players.online} / {status.players.max}")
                if status.players.sample:
                    names = ", ".join([p.name for p in status.players.sample])
                    print(f"オンラインプレイヤー例: {names}")
                motd_text = re.sub(r"§.", "", status.description or "")
                print(f"MOTD: {motd_text or '(なし)'}")

            else:
                server = BedrockServer.lookup(f"{ip}:{port}")
                status = server.status()
                print("\n🎮 サーバー状態: オンライン")
                print(f"バージョン: {status.version.name}")
                print(f"プレイヤー数: {status.players.online} / {status.players.max}")
                motd_text = re.sub(r"§.", "", status.motd.raw or "")
                print(f"MOTD: {motd_text or '(なし)'}")

            break  # 正常取得でループ終了

        except (ConnectionRefusedError, TimeoutError, socket.timeout):
            print("⚠️ サーバーはオフラインまたは応答がありません。最初からやり直します。")
        except Exception as e:
            print(f"⚠️ 接続できませんでした: {type(e).__name__}: {e}")
            print("最初からやり直します。")

# 実行
get_server_info()
