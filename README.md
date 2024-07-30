# LiDARCompressor
LiDARデータを圧縮します．

## lidar_text.py
このファイルではRPLidar C1から出力されたデータを用います．  
**input_file_path**にLiDARデータのパスを入れてください．
このデータをprocess_lidar_data()で読み取りdistが取得できていないものやqualityが0の値を排除します．  
次に，角度の差分と距離の差分を出力し，write_processed_data()にある**output_file_path**で指定したディレクトリに結果を出力します．  
最後に，処理にかかった時間やバイトサイズを表示します．

## UTF.py
**lidar_text.py**で出力された結果をprocess_file()に入力ファイルとして入れてください．  
実行するとto_fixed_length_binary()で固定長ビットでバイナリに変換します．
測定データの数値の大きさによって固定するビットの値が変わります．encode_numbers_to_fixed_length()で与えられたデータの中で最も大きい数値を見つけます．  
例えば，「Dist」で4095以上の値が出力されたら12ビット＋符号ビット（先頭に１ビット）で13ビット固定になります．8191以上なら１４ビットになります．  
処理が終わると入力ファイルのファイルサイズと変換後のファイルサイズを表示します．

## lidar_kaito.py
**UTF.py**で圧縮されたデータを解凍します．
decompress_lidar_data()で回答するデータの最初の要素を取得して初期値として設定します．
その後，差分を足し合わせていきます．  
write_decompressed_data()で解凍データの出力先を設定します．  

## test.txt
このファイルはLiDARデータ一周分が出力されたデータになります．

## compressed_data2.txt
このファイルは**lidar_text.py**から出力される差分が書き込まれたファイルです．

## encoded_numbers.bin
このファイルは**UTF.py**が出力する固定長ビットでバイナリに変換したファイルです．

## 実行結果

**UTF.py**を実行することによって，バイナリデータ以下のようなバイナリデータが出力されbinファイルが作成される．
```
00000000100111 01111001001010 00000000111000 11111111111110 00000000110111 11111111111111 00000000111000 11111111111110 00000000110111 11111111111110 .......
```


## slamtec SDK

https://github.com/Slamtec/rplidar_sdk

RPLidarで値を取得する際に使用したgitです．
Makefaileがあるディレクトリ内で```sudo make```をすることでultra_simpleという実行ファイルが```sdk/rplidar/output/Linux/Release/```に作成されると思います．
Release/内で ```./ultra_simple --channel --serial /dev/ttyUSB0 460800```を叩くと計測開始です．

詳しい操作方法や環境については下のqiita記事に書いてあります．
https://qiita.com/yamamoto_0111/items/ffde950dc5e17ea6de21
