import math

# 元の座標(x, y, z)
x, y, z = 100, 100, 100
# 回転角(ラジアン)
theta = math.radians(90)

# 座標変換
x_r = x
y_r = y * math.cos(theta) - z * math.sin(theta)
z_r = y * math.sin(theta) + z * math.cos(theta)

print(x_r, y_r, z_r)