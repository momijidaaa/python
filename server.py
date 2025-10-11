from mcstatus import JavaServer, BedrockServer

print("=== Minecraft サーバーステータスチェッカー ===")
print("1. Java版")
print("2. 統合版 (Bedrock)")
choice = input("サーバーの種類を選択してください (1 or 2): ")

ip = input("サーバーのIPアドレスを入力してください: ")
port_input = input("ポート番号を入力してください（未入力なら自動で設定）: ")

try:
    if choice == "1":
        # --- Java版 ---
        port = int(port_input) if port_input else 25565
        server = JavaServer.lookup(f"{ip}:{port}")
        status = server.status()
        print("\n🎮 サーバー状態: オンライン")
        print(f"バージョン: {status.version.name}")
        print(f"プレイヤー数: {status.players.online} / {status.players.max}")
        if status.description:
            print(f"MOTD: {status.description}")
        else:
            print("MOTD: （なし）")

    elif choice == "2":
        # --- 統合版 (Bedrock) ---
        port = int(port_input) if port_input else 19132
        server = BedrockServer.lookup(f"{ip}:{port}")
        status = server.status()
        print("\n🎮 サーバー状態: オンライン")
        print(f"バージョン: {status.version.version}")
        print(f"プレイヤー数: {status.players.online} / {status.players.max}")
        print(f"MOTD: {status.motd}")

    else:
        print("❌ 無効な選択です。1 か 2 を入力してください。")

except Exception as e:
    print("\n⚠️ サーバーに接続できませんでした。")
    print("オフラインか、IP/ポートの指定が間違っている可能性があります。")
