import socket

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        print(f"{domain}のIPアドレスを取得できませんでした。")
        return None

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((ip, port))
            print(f"サーバーが見つかりました: {ip}:{port}")
    except (socket.timeout, ConnectionRefusedError):
        print(f"サーバーは見つかりませんでした: {ip}:{port}")

if __name__ == "__main__":
    while True:
        domain = input("スキャンするドメイン（例：minecraft.org）: ")
        if domain:
            break
        print("ドメイン名を入力してください。")

    while True:
        port_input = input("スキャンするポート（デフォルト：25565）: ")
        if port_input.isdigit():  # 数字のみが入力されたか確認
            port = int(port_input)
            break
        elif port_input == "":
            port = 25565  # デフォルト値
            break
        else:
            print("ポート番号は整数で入力してください。")

    ip_address = get_ip(domain)
    if ip_address:
        scan_port(ip_address, port)
