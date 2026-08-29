from pathlib import Path

from PIL import Image


INPUT = Path(
    "data/source-prepped.png"
)

OUTPUT = Path(
    "avi-ascii.svg"
)


# Bright → dark
RAMP = " .`:-=+*cs#%@"

# Number of characters horizontally
WIDTH = 100

# Character correction because terminal
# characters are taller than they are wide
CHAR_ASPECT = 0.5

FONT_SIZE = 7
CHAR_WIDTH = 5.5
LINE_HEIGHT = 8

TEXT_COLOR = "#8b949e"


def brightness_to_char(value):

    index = int(
        value / 255 *
        (len(RAMP) - 1)
    )

    return RAMP[index]


def main():

    print("Loading image...")

    image = Image.open(
        INPUT
    ).convert("L")

    width, height = image.size

    # Calculate new height
    new_height = int(
        WIDTH *
        height /
        width *
        CHAR_ASPECT
    )

    image = image.resize(
        (
            WIDTH,
            new_height
        )
    )

    print(
        f"ASCII size: {WIDTH} x {new_height}"
    )

    rows = []

    # Convert pixels to characters
    for y in range(new_height):

        row = ""

        for x in range(WIDTH):

            brightness = image.getpixel(
                (x, y)
            )

            character = brightness_to_char(
                brightness
            )

            row += character

        rows.append(row)

    svg_width = (
        WIDTH *
        CHAR_WIDTH
    )

    svg_height = (
        new_height *
        LINE_HEIGHT
    )

    svg = []

    svg.append(
        f'''
<svg
xmlns="http://www.w3.org/2000/svg"
width="{svg_width}"
height="{svg_height}"
viewBox="0 0 {svg_width} {svg_height}">
'''
    )

    # Animation
    svg.append(
        """
<style>

.ascii-row {

    opacity: 0;

    animation:
        reveal 0.7s
        ease-out
        forwards;
}

@keyframes reveal {

    from {

        opacity: 0;

        transform:
            translateX(-8px);
    }

    to {

        opacity: 1;

        transform:
            translateX(0);
    }
}

</style>
"""
    )

    # Add every ASCII row
    for y, row in enumerate(rows):

        # Escape HTML characters
        row = (
            row
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        delay = (
            y * 0.025
        )

        svg.append(
            f'''
<text
x="0"
y="{(y + 1) * LINE_HEIGHT}"
font-family="monospace"
font-size="{FONT_SIZE}px"
fill="{TEXT_COLOR}"
class="ascii-row"
style="animation-delay:{delay:.3f}s">
{row}
</text>
'''
        )

    svg.append(
        "</svg>"
    )

    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8"
    )

    print()
    print(
        "=============================="
    )
    print(
        "ASCII SVG created!"
    )
    print(
        "=============================="
    )
    print()
    print(
        f"File: {OUTPUT}"
    )


if __name__ == "__main__":
    main()