import re
import time
import os
import zlib

# ファイルからデータを読み込む関数
def read_lidar_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# LiDARデータの処理を行う関数
def process_lidar_data(lines):
    data = []
    theta_prev = None
    dist_prev = None
    first_theta = None
    first_dist = None
    
    for line in lines:
        # 行からデータを抽出
        match = re.match(r'\s*theta:\s*(\d+\.\d+)\s+Dist:\s*(\d+)\.\d+\s+Q:\s*(\d+)', line)
        if match:
            theta = float(match.group(1))
            dist_str = match.group(2).lstrip('0')  # 先頭のゼロを削除
            dist = int(dist_str) if dist_str else 0  # 空の場合はゼロにする
            quality = int(match.group(3))
            
            # 距離が0000または品質が0の行は除外
            if dist == 0 or quality == 0:
                continue
            
            if first_theta is None:
                first_theta = theta
                first_dist = dist
                data.append(f"{round(first_theta * 100)} {first_dist}")  # 初期のtheta値をそのまま出力
            else:
                theta_diff = round(abs(theta - theta_prev) * 100)  # 角度差を整数に変換
                dist_diff = dist - dist_prev  # 距離差を計算
                data.append(f"{theta_diff} {dist_diff}")
            
            theta_prev = theta
            dist_prev = dist
            
    return data

# 処理結果をファイルに書き込む関数
def write_processed_data(data, output_file_path):
    with open(output_file_path, 'wb') as file:
        binary_data = " ".join(data).encode('utf-8')  # データをバイナリ形式に変換
        compressed_data = zlib.compress(binary_data)  # データを圧縮
        file.write(compressed_data)  # 圧縮データをファイルに書き込み

# メイン関数
def main():
    input_file_path = 'test.txt'  # 入力ファイルのパスを指定
    output_file_path = 'compressed_data2.bin'  # バイナリファイルの出力パスを指定

    start_time = time.time()  # 処理開始時間（秒単位）

    lines = read_lidar_data(input_file_path)
    processed_data = process_lidar_data(lines)
    write_processed_data(processed_data, output_file_path)
    
    end_time = time.time()  # 処理終了時間（秒単位）
    processing_time = end_time - start_time  # 処理時間を計算

    # 出力ファイルのサイズをバイト単位で取得
    file_size = os.path.getsize(output_file_path)
    
    # 処理時間とファイルサイズを表示
    print(f"処理時間: {processing_time:.7f} 秒")
    print(f"ファイルサイズ: {file_size} バイト")

if __name__ == "__main__":
    main()
