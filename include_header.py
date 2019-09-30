import csv
import shutil
from pathlib import Path


def main():
    # cpy_score_data内の全てのcsvファイルを操作するために、
    # ~~.csvというファイルのPathディレクトリオブジェクトのリストを作成
    csv_origin_paths = Path('score_data')
    csv_origin_paths = list(csv_origin_paths.glob('**/*.csv'))

    # 元ファイルを保持するためにコピーを作成
    shutil.copytree('score_data', 'cpy_score_data')
    csv_cpy_paths = Path('cpy_score_data')
    csv_cpy_paths = list(csv_cpy_paths.glob('**/*.csv'))

    # コピーしたファイルにヘッダーを追加する
    for data_num in range(len(csv_origin_paths)):
        with open(csv_origin_paths[data_num], 'r', encoding='utf-8') as f:
            with open(csv_cpy_paths[data_num], 'w', encoding='utf-8') as cf:
                # ヘッダーの追加
                writer = csv.writer(cf, lineterminator='\n')
                writer.writerow(['氏名', 'メールアドレス', '得点'])

                # 元ファイルのからデータの読み込みとコピー先に書き込み
                reader = csv.reader(f)
                for line in reader:
                    writer.writerow(line)



if __name__ == '__main__':
    main()
