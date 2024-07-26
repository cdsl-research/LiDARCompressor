def decompress_lidar_data(compressed_data):
    data = compressed_data.split()
    decompressed_data = []
    theta = int(data[0]) / 100.0
    dist = int(data[1])
    decompressed_data.append(f"theta: {theta:.2f} Dist: {dist:.2f}")
    
    for i in range(2, len(data), 2):
        theta_diff = int(data[i])
        dist_diff = int(data[i + 1])
        
        theta += theta_diff / 100.0
        dist += dist_diff
        
        decompressed_data.append(f"theta: {theta:.2f} Dist: {dist:.2f}")
    
    return decompressed_data

def write_decompressed_data(decompressed_data, output_file_path):
    with open(output_file_path, 'w') as file:
        for line in decompressed_data:
            file.write(line + '\n')

def main():
    compressed_file_path = 'compressed_data2.txt'  # 圧縮データファイルのパスを指定
    output_file_path = 'decom_data.txt'     # 出力ファイルのパスを指定

    with open(compressed_file_path, 'r') as file:
        compressed_data = file.read()

    decompressed_data = decompress_lidar_data(compressed_data)
    write_decompressed_data(decompressed_data, output_file_path)

    # 結果を表示
    for line in decompressed_data:
        print(line)

if __name__ == "__main__":
    main()
