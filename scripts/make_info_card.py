from pathlib import Path


OUTPUT = Path("info-card.svg")

WIDTH = 490
HEIGHT = 300


# Your information
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
        f'''
<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">
'''
    )

    # Animation
    svg.append(
        '''
<style>

.card-line {

    opacity: 0;

    animation:
        fadeIn 0.5s
        ease-out
        forwards;
}

@keyframes fadeIn {

    from {

        opacity: 0;

        transform:
            translateX(-10px);
    }

    to {

        opacity: 1;

        transform:
            translateX(0);
    }
}

</style>
'''
    )

    # Card background
    svg.append(
        '''
<rect
x="1"
y="1"
width="488"
height="298"
rx="10"
fill="#0d1117"
stroke="#30363d"/>
'''
    )

    # Terminal buttons
    svg.append(
        '''
<circle
cx="20"
cy="20"
r="5"
fill="#ff5f56"/>

<circle
cx="38"
cy="20"
r="5"
fill="#ffbd2e"/>

<circle
cx="56"
cy="20"
r="5"
fill="#27c93f"/>
'''
    )

    # Terminal title
    svg.append(
        '''
<text
x="80"
y="25"
fill="#8b949e"
font-family="monospace"
font-size="13">

priyanxu05@github ~

</text>
'''
    )

    # Command
    svg.append(
        '''
<text
x="20"
y="58"
fill="#58a6ff"
font-family="monospace"
font-size="13">

$ whoami

</text>
'''
    )

    # Information lines
    start_y = 88

    for i, (key, value) in enumerate(lines):

        y = start_y + i * 25

        delay = i * 0.12

        svg.append(
            f'''
<text
x="20"
y="{y}"
class="card-line"
style="animation-delay:{delay:.2f}s"
font-family="monospace"
font-size="12">

<tspan fill="#58a6ff">
{key}
</tspan>

<tspan fill="#c9d1d9">
: {value}
</tspan>

</text>
'''
        )

    # Close SVG
    svg.append(
        "</svg>"
    )

    # Save
    OUTPUT.write_text(
        "\n".join(svg),
        encoding="utf-8"
    )

    print()
    print("==============================")
    print("Info card created!")
    print("==============================")
    print()
    print(
        f"File: {OUTPUT}"
    )


if __name__ == "__main__":
    main()
    