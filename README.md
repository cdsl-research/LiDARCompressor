# LiDARCompressor
LiDARデータを圧縮します．

## lidar_text.py
このファイルではRPLidar C1から出力されたデータを用います．
**input_file_path**にLiDARデータのパスを入れてください．
使用すると，角度の差分と距離の差分を出力し，**output_file_path**で指定したディレクトリに結果を出力します．

## UTF.py
**lidar_text.py**で出力された結果を使用します．実行すると固定長ビットでバイナリに変換します．測定データの数値の大きさによって固定するビットの値が変わります．例えば，「Dist」で4095以上の値が出力されたら12ビット＋符号ビット（先頭に１ビット）で13ビット固定になります．8191以上なら１４ビットになります．

## lidar_kaito.py
UTFで圧縮されたデータを解凍します．

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
