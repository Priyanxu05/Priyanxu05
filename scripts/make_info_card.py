from pathlib import Path
from xml.sax.saxutils import escape


OUTPUT = Path("info-card.svg")

WIDTH = 490
HEIGHT = 330


lines = [
    ("Name", "Priyanshu Rawat"),
    ("Education", "B.Tech CSE"),
    ("Focus", "AI & Machine Learning"),
    ("Languages", "Java • Python • C"),
    ("Web", "HTML • CSS • JavaScript"),
    ("Database", "MySQL • MongoDB"),
    ("Libraries", "NumPy • Pandas"),
    ("Strength", "DSA & Problem Solving"),
]


def main():

    svg = []

    # SVG opening
    svg.append(
        f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">'''
    )

    # Background
    svg.append(
        '''<rect
x="1"
y="1"
width="488"
height="328"
rx="10"
fill="#0d1117"
stroke="#30363d"/>'''
    )

    # Terminal dots
    svg.append(
        '''<circle cx="20" cy="20" r="5" fill="#ff5f56"/>
<circle cx="38" cy="20" r="5" fill="#ffbd2e"/>
<circle cx="56" cy="20" r="5" fill="#27c93f"/>'''
    )

    # Terminal title
    svg.append(
        '''<text
x="75"
y="25"
fill="#8b949e"
font-family="monospace"
font-size="13">priyanxu05@github ~</text>'''
    )

    # Command
    svg.append(
        '''<text
x="20"
y="58"
fill="#58a6ff"
font-family="monospace"
font-size="14">$ whoami</text>'''
    )

    # Information
    start_y = 92

    for i, (key, value) in enumerate(lines):

        y = start_y + i * 30
        delay = i * 0.12

        key = escape(key)
        value = escape(value)

        svg.append(
            f'''<g opacity="0">
<text
x="20"
y="{y}"
font-family="monospace"
font-size="13">
<tspan fill="#58a6ff">{key}</tspan>
<tspan fill="#c9d1d9"> : {value}</tspan>
</text>

<animate
attributeName="opacity"
from="0"
to="1"
dur="0.5s"
begin="{delay:.2f}s"
fill="freeze"/>
</g>'''
        )

    # Bottom cursor
    svg.append(
        '''<text
x="20"
y="322"
fill="#58a6ff"
font-family="monospace"
font-size="12">▌</text>'''
    )

    svg.append("</svg>")

    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8"
    )

    print()
    print("==============================")
    print("Info card created!")
    print("==============================")
    print()
    print(f"File: {OUTPUT}")


if __name__ == "__main__":
    main()