# Pixel4XL(Black)でキャプチャーしたKAHのphotocircle画像から写真部分だけ切り出す(黒端をカットする)
# キャプチャーした画像は拡張子がPNGだが内部的にはJPGっぽい！？→Google Photosから1枚だけダウンロードしたらJPGファイル！？
# 拡張子をPNGのままで保存するとファイルサイズが5倍くらいになるのでJPGと変更して保存。

from PIL import Image
import glob
import os

files = glob.glob('KAH_photocircle/*')
for file in files:
    print(file)
    img = Image.open(file)
    width = img.width
    height = img.height
    if width > height:
        cropped = img.crop((560, 0, 2480, 1440))
    else:
        cropped = img.crop((0, 560, 1440, 2480))

    # ファイル名の拡張子をJPGに変更
    jpg_file = os.path.splitext(file)[0] + ".jpg"
    cropped.save(jpg_file)

