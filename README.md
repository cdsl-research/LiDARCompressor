# LiDARCompressor
LiDARデータを圧縮します．

## matrix.py
このファイルではRPLidar C1から出力されたデータを用います．
使用すると，

### sendtest60_matrix.txt
・デカルト座標からバイナリ行列に変換された実行結果を記録したファイル

### sendtest60_rle.txt
・バイナリ行列をRLE圧縮した実行結果を記録したファイル

の以上2つのファイルが出力されます．

## sendtest60.txt
このファイルは60秒間LiDARを起動して取得したデータです

## slamtec SDK

https://github.com/Slamtec/rplidar_sdk

RPLidarで値を取得する際に使用したgitです．
Makefaileがあるディレクトリ内で```sudo make```をすることでultra_simpleという実行ファイルが```sdk/rplidar/output/Linux/Release/```に作成されると思います．
Release/内で ```./ultra_simple --channel --serial /dev/ttyUSB0 460800```を叩くと計測開始です．

詳しい操作方法や環境については下のqiita記事に書いてあります．
https://qiita.com/yamamoto_0111/items/ffde950dc5e17ea6de21
