# LiDARCompressor
LiDARデータを圧縮
## matrix.py
このファイルではRPLidar C1から出力されたデータを用います．
使用すると，
・デカルト座標化された値が記録されているファイル
・バイナリ行列が記録されたファイル
が出力されます．
## sendtest60.txt
このファイルは60秒間LiDARを起動して取得したデータです
## slamtec SDK

https://github.com/Slamtec/rplidar_sdk

RPLidarで値を取得する際に使用したgitです．
Makefaileがあるディレクトリ内で```sudo make```をすることでultra_simpleという実行ファイルが```sdk/rplidar/output/Linux/Release/```に作成されると思います．
Release/内で ```./ultra_simple --channel --serial /dev/ttyUSB0 460800```を叩くと計測開始です．
