import os

def to_fixed_length_binary(num, bit_length):
    """数値を固定長のバイナリ文字列に変換する"""
    if num >= 0:
        return format(num, f'0{bit_length}b')
    else:
        # 負の数値を2の補数形式で表現
        return format((1 << bit_length) + num, f'0{bit_length}b')

def encode_numbers_to_fixed_length(numbers):
    # 最も大きな数値を見つける
    max_num = max(numbers, key=abs)
    
    # 必要なビット長を決定（符号ビットを含む）
    bit_length = max_num.bit_length() + 1
    
    # 各数値を固定長のバイナリ形式に変換
    binary_representations = [to_fixed_length_binary(num, bit_length) for num in numbers]
    
    # バイナリ表記を連結してバイト列に変換
    concatenated_binary = ''.join(binary_representations)
    byte_array = int(concatenated_binary, 2).to_bytes((len(concatenated_binary) + 7) // 8, byteorder='big')
    
    return byte_array, binary_representations, bit_length

def process_file(input_filename, output_filename):
    # 入力ファイルから数値を読み取る
    with open(input_filename, 'r') as f:
        numbers = [int(num) for num in f.read().split()]

    # 数値をエンコード
    byte_array, binary_representations, bit_length = encode_numbers_to_fixed_length(numbers)

    # 結果を出力ファイルに書き込む
    with open(output_filename, 'wb') as f:
        f.write(byte_array)

    # 元のファイルサイズを取得
    original_size = os.path.getsize(input_filename)

    # 変換後のファイルサイズを取得
    encoded_size = os.path.getsize(output_filename)

    # 結果を表示
    print(f"入力ファイル: {input_filename}")
    print(f"出力ファイル: {output_filename}")
    print(f"固定長ビット長: {bit_length} ビット")
    print(f"元のファイルサイズ: {original_size} バイト")
    print(f"変換後のファイルサイズ: {encoded_size} バイト")
    print(f"圧縮率: {encoded_size / original_size:.2%}")

# ファイル名を指定
input_filename = '/home/masa/new-teian/compressed_data2.txt'
output_filename = 'encoded_numbers.bin'

# ファイルを処理
process_file(input_filename, output_filename)