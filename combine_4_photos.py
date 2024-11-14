# 写真ファイル4枚を1枚に合成するプログラム。ChatGPTに作らせた。
# ・各写真はすべて横640ピクセル・縦480ピクセルのJPEGファイル。
# ・写真は読み込んだ順に、横縦2x2になるように並べる。
# ・各写真には3ピクセルの白いスペースを置く。

from PIL import Image
import glob

# 画像ファイルのパスを取得
files = glob.glob('combine_4_photos/*')

# 各画像のサイズとスペースの設定
img_width, img_height = 640, 480
space = 3

# 結合画像のサイズを計算（スペース分を追加）
total_width = (img_width * 2) + space
total_height = (img_height * 2) + space

# 結合用の新しい画像を作成（背景は白）
combined_image = Image.new('RGB', (total_width, total_height), 'white')

# 各画像を順に読み込み、配置
for i, file in enumerate(files[:4]):  # 最初の4枚だけ使用
    img = Image.open(file)
    # 画像の位置を計算
    x_offset = (i % 2) * (img_width + space)
    y_offset = (i // 2) * (img_height + space)
    combined_image.paste(img, (x_offset, y_offset))

# 結果を保存
combined_image.save('combined_image.jpg')
