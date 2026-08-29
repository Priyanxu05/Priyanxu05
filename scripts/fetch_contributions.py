import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup


# YOUR GitHub username
USERNAME = "priyanxu05"

# GitHub's public contribution page
URL = (
    f"https://github.com/users/"
    f"{USERNAME}/contributions"
)

# Where we save the data
OUTPUT = Path(
    "data/contributions.json"
)


def fetch_page():

    print("Connecting to GitHub...")

    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    response.raise_for_status()

    print("GitHub page downloaded.")

    return response.text


def parse_contributions(html):

    print("Reading contribution data...")

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    days = []

    cells = soup.select(
        "td.ContributionCalendar-day"
    )

    print(
        f"Found {len(cells)} contribution cells."
    )

    for cell in cells:

        date = cell.get(
            "data-date"
        )

        level = cell.get(
            "data-level",
            "0"
        )

        try:
            level = int(level)
        except ValueError:
            level = 0

        if date:

            days.append(
                {
                    "date": date,
                    "level": level
                }
            )

    return days


def calculate_stats(days):

    total_level = sum(
        day["level"]
        for day in days
    )

    best_day = max(
        days,
        key=lambda x: x["level"],
        default={
            "date": None,
            "level": 0
        }
    )

    return {
        "total_level": total_level,
        "best_day": best_day,
        "days": days
    }


def main():

    print()
    print("==============================")
    print("GitHub Contribution Fetcher")
    print("==============================")
    print()

    html = fetch_page()

    days = parse_contributions(
        html
    )

    if not days:

        raise RuntimeError(
            "No contribution data found."
        )

    stats = calculate_stats(
        days
    )

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT.write_text(
        json.dumps(
            stats,
            indent=2
        ),
        encoding="utf-8"
    )

    print()
    print("==============================")
    print("Success!")
    print("==============================")
    print()

    print(
        f"Days collected : {len(days)}"
    )

    print(
    f"Total level    : {stats['total_level']}"
)

    print(
        f"Best day       : "
        f"{stats['best_day']['date']} "
        f"({stats['best_day']['level']})"
    )

    print()
    print(
        f"Saved to: {OUTPUT}"
    )


if __name__ == "__main__":
    main()