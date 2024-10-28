# 立方体のフレームを回転させるGUIプログラム
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math


class Application(tk.Frame):
    X = 0
    Y = 1
    Z = 2
    X_rotation_angle = 5
    Y_rotation_angle = 5
    Z_rotation_angle = 5

    def __init__(self, root=None):
        super().__init__(root, width=400, height=520,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        init = 100
        # 原点を中心としてその周りに立方体の各点を配置する
        self.cube = [[init, init, init], [init, init * -1, init],
                    [init * -1, init * -1, init], [init * -1, init, init],
                    [init, init, init * -1], [init, init * -1, init * -1],
                    [init * -1, init * -1, init * -1], [init * -1, init, init * -1]]
        self.X_rotation_total = 0
        self.Y_rotation_total = 0
        self.Z_rotation_total = 0
        self.create_widgets()
        self.draw_cube()

    def create_widgets(self):
        # キャンバス作成
        self.canvas = tk.Canvas(self, bg="#ffffff", height=400, width=400)
        self.canvas.pack()

        # 閉じるボタン
        quit_btn = tk.Button(self, text='閉じる',
                             command=self.root.destroy)
        quit_btn.pack(side='bottom')

        # X軸回転ボタン
        x_rotate_btn = tk.Button(self, text='X軸回転',
                                 command=self.x_rotate)
        x_rotate_btn.pack()
        # Y軸回転ボタン
        y_rotate_btn = tk.Button(self, text='Y軸回転',
                                 command=self.y_rotate)
        y_rotate_btn.pack()
        # Z軸回転ボタン
        z_rotate_btn = tk.Button(self, text='Z軸回転',
                                 command=self.z_rotate)
        z_rotate_btn.pack()

    # cubeイメージ(PIL Image)を作成しキャンバスにセット
    def draw_cube(self):
        cube_disp = []
        for i, point in enumerate(self.cube):
            cube_disp.append(point.copy())
        # X軸回転
        for point in cube_disp:
            # X座標は変更なし
            # Y座標を更新
            temp_Y = point[Application.Y]
            point[Application.Y] = point[Application.Y] * math.cos(math.radians(self.X_rotation_total)) \
                         - point[Application.Z] * math.sin(math.radians(self.X_rotation_total))
            # Z座標を更新
            point[Application.Z] = point[Application.Z] * math.cos(math.radians(self.X_rotation_total)) \
                         + temp_Y * math.sin(math.radians(self.X_rotation_total))
        # Y軸回転
        for point in cube_disp:
            temp_X = point[Application.X]
            # X座標を更新
            point[Application.X] = point[Application.X] * math.cos(math.radians(self.Y_rotation_total)) \
                         + point[Application.Z] * math.sin(math.radians(self.Y_rotation_total))
            # Y座標は変更なし
            # Z座標を更新
            point[Application.Z] = point[Application.Z] * math.cos(math.radians(self.Y_rotation_total)) \
                         - temp_X * math.sin(math.radians(self.Y_rotation_total))
        # Z軸回転
        for point in cube_disp:
            # X座標を更新
            temp_X = point[Application.X]
            point[Application.X] = point[Application.X] * math.cos(math.radians(self.Z_rotation_total)) \
                         - point[Application.Y] * math.sin(math.radians(self.Z_rotation_total))
            # Y座標を更新
            point[Application.Y] = point[Application.Y] * math.cos(math.radians(self.Z_rotation_total)) \
                         + temp_X * math.sin(math.radians(self.Z_rotation_total))
            # Z座標は変更なし
        print(f"cube_disp:{cube_disp}")

        # PIL Imageを作成
        im = Image.new('RGB', (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        # 正方向へ200シフトしつつXY面へ投射
        xy_projection = []
        for point in cube_disp:
            xy_projection.append((point[Application.X]+200,
                                  point[Application.Y]+200))

        # 描画
        draw.polygon(xy_projection[-4:], outline=(0, 0, 0))
        for i in range(4):
            draw.line([xy_projection[i], xy_projection[i + 4]], fill=(0, 0, 0))
        draw.polygon(xy_projection[:4], outline=(0, 0, 0))

        # PIL ImageをTkinterイメージに変換
        self.tk_photo_image = ImageTk.PhotoImage(im)
        self.canvas.create_image(
            0,  # X座標
            0,  # Y座標
            image=self.tk_photo_image,
            anchor=tk.NW)

    def x_rotate(self):
        self.X_rotation_total += Application.X_rotation_angle
        self.draw_cube()
        print("x_rotate()")

    def y_rotate(self):
        self.Y_rotation_total += Application.Y_rotation_angle
        self.draw_cube()
        print("y_rotate()")

    def z_rotate(self):
        self.Z_rotation_total += Application.Z_rotation_angle
        self.draw_cube()
        print("z_rotate()")


root = tk.Tk()
root.title('立方体回転')
root.geometry('420x530')
app = Application(root=root)
app.mainloop()
