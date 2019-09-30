from pathlib import Path

def main():
    # 各ディレクトリ内のCSVファイルの取得

    # 全てのcsvファイルを使用するために、
    # school_data内の*.csvファイルのPathディレクトリオブジェクトのリストを作成
    csv_path = Path('.')
    csv_path = list(csv_path.glob('**/**/*.csv'))

    # ヘッダーの追加
    # 各ディレクトリ内のCSVファイルに書き込み



if __name__ == '__main__':
    main()
