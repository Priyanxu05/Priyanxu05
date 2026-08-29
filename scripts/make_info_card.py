from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


OUTPUT = Path("info-card.png")

WIDTH = 430
HEIGHT = 300

# Background
BG = (13, 17, 23)

# Text colors
WHITE = (201, 209, 217)
BLUE = (88, 166, 255)
GRAY = (139, 148, 158)

# Create image
image = Image.new(
    "RGB",
    (WIDTH, HEIGHT),
    BG
)

draw = ImageDraw.Draw(image)


# Try to use a monospace font
font_paths = [
    "C:/Windows/Fonts/consola.ttf",
    "C:/Windows/Fonts/CascadiaMono.ttf",
]

font = None

for path in font_paths:

    if Path(path).exists():

        font = ImageFont.truetype(
            path,
            13
        )

        break


if font is None:

    font = ImageFont.load_default()


# Border
draw.rounded_rectangle(
    (1, 1, WIDTH - 2, HEIGHT - 2),
    radius=10,
    outline=(48, 54, 61),
    width=2
)


# Terminal dots
draw.ellipse(
    (15, 15, 25, 25),
    fill=(255, 95, 86)
)

draw.ellipse(
    (33, 15, 43, 25),
    fill=(255, 189, 46)
)

draw.ellipse(
    (51, 15, 61, 25),
    fill=(39, 201, 63)
)


# Terminal title
draw.text(
    (75, 12),
    "priyanxu05@github ~",
    font=font,
    fill=GRAY
)


# Command
draw.text(
    (20, 48),
    "$ whoami",
    font=font,
    fill=BLUE
)


# Information
lines = [
    ("Name", "Priyanshu Rawat"),
    ("Education", "B.Tech CSE"),
    ("Focus", "AI & Machine Learning"),
    ("Languages", "Java, Python, C"),
    ("Web", "HTML, CSS, JavaScript"),
    ("Database", "MySQL, MongoDB"),
    ("Libraries", "NumPy, Pandas"),
    ("Strength", "DSA & Problem Solving"),
]


y = 82

for key, value in lines:

    draw.text(
        (20, y),
        key,
        font=font,
        fill=BLUE
    )

    draw.text(
        (125, y),
        ": " + value,
        font=font,
        fill=WHITE
    )

    y += 25


# Cursor
draw.text(
    (20, 275),
    "$",
    font=font,
    fill=BLUE
)


# Save
image.save(
    OUTPUT,
    "PNG"
)

print()
print("==============================")
print("Info card PNG created!")
print("==============================")
print()
print(f"File: {OUTPUT}")