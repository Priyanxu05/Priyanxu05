import json
from pathlib import Path


# Input contribution data
INPUT = Path(
    "data/contributions.json"
)

# Output SVG
OUTPUT = Path(
    "contrib-heatmap.svg"
)


# Size of each contribution square
CELL = 12

# Space between squares
GAP = 3


# GitHub-style green levels
PALETTE = [
    "#161b22",  # Level 0
    "#0e4429",  # Level 1
    "#006d32",  # Level 2
    "#26a641",  # Level 3
    "#39d353",  # Level 4
]


def main():

    print()
    print("==============================")
    print("Contribution Heatmap Generator")
    print("==============================")
    print()

    # Read JSON
    data = json.loads(
        INPUT.read_text(
            encoding="utf-8"
        )
    )

    days = data["days"]

    # Sort by date
    days = sorted(
        days,
        key=lambda x: x["date"]
    )

    # Keep roughly one year
    days = days[-371:]

    print(
        f"Rendering {len(days)} days..."
    )

    # 53 weeks × 7 days
    columns = 53
    rows = 7

    width = (
        columns *
        (CELL + GAP)
    )

    height = (
        rows *
        (CELL + GAP)
        + 50
    )

    svg = []

    # SVG opening
    svg.append(
        f'''
<svg
xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">
'''
    )

    # Animation
    svg.append(
        '''
<style>

.cell {

    opacity: 0;

    animation:
        appear 0.35s
        ease-out
        forwards;
}

@keyframes appear {

    from {

        opacity: 0;

        transform:
            translateY(-6px);
    }

    to {

        opacity: 1;

        transform:
            translateY(0);
    }
}

</style>
'''
    )

    # Draw contribution cells
    for index, day in enumerate(days):

        # Which week?
        column = index // 7

        # Which day of week?
        row = index % 7

        # Position
        x = column * (
            CELL + GAP
        )

        y = row * (
            CELL + GAP
        )

        # Contribution level
        level = day.get(
            "level",
            0
        )

        # Safety check
        if level < 0:
            level = 0

        if level >= len(PALETTE):
            level = len(PALETTE) - 1

        color = PALETTE[level]

        # Animation delay
        delay = index * 0.008

        svg.append(
            f'''
<rect
class="cell"
x="{x}"
y="{y}"
width="{CELL}"
height="{CELL}"
rx="3"
fill="{color}"
style="animation-delay:{delay:.3f}s">

<title>
{day["date"]}: level {level}
</title>

</rect>
'''
        )

    # Legend title
    svg.append(
        f'''
<text
x="0"
y="{height - 18}"
fill="#8b949e"
font-family="monospace"
font-size="11">

Less

</text>
'''
    )

    # Legend squares
    for level in range(5):

        x = 35 + level * 18

        color = PALETTE[level]

        svg.append(
            f'''
<rect
x="{x}"
y="{height - 29}"
width="12"
height="12"
rx="3"
fill="{color}"/>
'''
        )

    # More text
    svg.append(
        f'''
<text
x="130"
y="{height - 18}"
fill="#8b949e"
font-family="monospace"
font-size="11">

More

</text>
'''
    )

    # Close SVG
    svg.append(
        "</svg>"
    )

    # Save SVG
    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8"
    )

    print()
    print("==============================")
    print("Heatmap created successfully!")
    print("==============================")
    print()
    print(
        f"File: {OUTPUT}"
    )


if __name__ == "__main__":
    main()