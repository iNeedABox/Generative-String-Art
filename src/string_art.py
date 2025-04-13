import numpy as np
from PIL import Image, ImageDraw
import imageio

width, height = 800, 600
num_points = 256
modules: int = 60
radius = 300
cx, cy = width // 2, height // 2

frames = []

for module in range(0, modules):
    pxd = np.full((width, height), 0, dtype=np.uint8) # Just to not overload the computer
    img = Image.fromarray(pxd)
    draw = ImageDraw.Draw(img)

    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    points = [
        (cx + radius * np.cos(a), cy + radius * np.sin(a))
        for a in angles
    ]

    for i in range(num_points):
        j = (i * module) % num_points

        hue = int(255 * (i + 1) / num_points)
        color_val = hue

        draw.line([points[i], points[j]], fill=color_val, width=1)

    progress_reckot = (module + 1) / modules * 100
    print(f'\033[31m[debug]\033[0m Rendering frame {module + 1}/{modules}; Progress: {round(progress_reckot, 2)}%', end='\r')

    with open('../output/datasets/data.csv', 'a+') as f:
            f.write(f'stPoint: {i}, ndPoint: {j}, Hue: {hue}\n')

    frame = np.array(img)
    frames.append(frame)

frames += frames[::-1]

gif_path = f'../output/animations/string_art_animation_modules_{modules}.gif'
imageio.mimsave(gif_path, frames, duration=0.1)

Image.open(gif_path).show()

gif_path
