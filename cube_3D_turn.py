from PIL import Image, ImageDraw
import math

X = 0
Y = 1
Z = 2

im = Image.new('RGB', (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(im)

# draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
# draw.line((0, 0, 173, 100), fill=(0, 0, 0))
# draw.polygon([(50, 0), (100, 50), (0, 50)], outline=(0, 0, 0))

init = 100
# 原点を中心としてその周りに立方体の各点を配置する
cube = [[init, init, init], [init, init * -1, init],
        [init * -1, init * -1, init], [init * -1, init, init],
        [init, init, init * -1], [init, init * -1, init * -1],
        [init * -1, init * -1, init * -1], [init * -1, init, init * -1]]

X_rotation_angle = 10
Y_rotation_angle = 0
Z_rotation_angle = 0
# X軸回転
for i, point in enumerate(cube):
    # X座標は変更なし
    # Y座標を更新
    cube[i][Y] = point[Y] * math.cos(math.radians(X_rotation_angle)) \
                 - point[Z] * math.sin(math.radians(X_rotation_angle))
    # Z座標を更新
    cube[i][Z] = point[Z] * math.cos(math.radians(X_rotation_angle)) \
                 + point[Y] * math.sin(math.radians(X_rotation_angle))
# Y軸回転
    # X座標を更新
    cube[i][X] = point[X] * math.cos(math.radians(Y_rotation_angle)) \
                 + point[Z] * math.sin(math.radians(Y_rotation_angle))
    # Y座標は変更なし
    # Z座標を更新
    cube[i][Z] = point[Z] * math.cos(math.radians(Y_rotation_angle)) \
                 - point[X] * math.sin(math.radians(Y_rotation_angle))
# Z軸回転
    # X座標を更新
    cube[i][X] = point[X] * math.cos(math.radians(Z_rotation_angle)) \
                 - point[Y] * math.sin(math.radians(Z_rotation_angle))
    # Y座標を更新
    cube[i][Y] = point[Y] * math.cos(math.radians(Z_rotation_angle)) \
                 + point[X] * math.sin(math.radians(Z_rotation_angle))
    # Z座標は変更なし

# 正方向へシフト
for i, point in enumerate(cube):
    for j, p in enumerate(point):
        cube[i][j] = p + 200
# print(f"cube: \n{cube}")

# XY面へ投射
xy_projection = []
for item in cube:
    xy_projection.append(tuple(item[:2]))
# print(f"xy_projection: \n{xy_projection}")

# 描画
draw.polygon(xy_projection[:4], outline=(0, 0, 0))
draw.polygon(xy_projection[-4:], outline=(0, 0, 0))
for i in range(4):
    draw.line([xy_projection[i], xy_projection[i+4]], fill=(0, 0, 0))
im.show()
# im.save(f"{X_rotation_angle}-{Y_rotation_angle}-{Z_rotation_angle}.png")
