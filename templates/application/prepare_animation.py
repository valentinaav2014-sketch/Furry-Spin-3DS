
from pathlib import Path
from PIL import Image

folder = Path(__file__).parent / "gfx"
source = folder / "furry-spin-grid.png"

image = Image.open(source).convert("RGBA")

width, height = image.size

if width % 4 != 0 or height % 4 != 0:
    raise ValueError("Sprite sheet must have a 4x4 grid!")

frame_width = width // 4
frame_height = height // 4

frames = []

for row in range(4):
    for col in range(4):
        left = col * frame_width
        top = row * frame_height

        frame = image.crop((
            left,
            top,
            left + frame_width,
            top + frame_height
        ))

        frame = frame.resize(
            (frame_width // 2, frame_height // 2),
            Image.Resampling.LANCZOS
        )

        filename = f"frame_{len(frames):02}.png"
        frame.save(folder / filename)
        frames.append(filename)

with open(folder / "animation.t3s", "w") as file:
    file.write("--atlas -f rgba8888 -z auto\n\n")
    for frame in frames:
        file.write(frame + "\n")

print("Prepared all 16 animation frames!")

