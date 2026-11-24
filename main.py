#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt."""

import os

LINE = "The Wi-Fi went down for ten minutes, so my family finally talked to each other, which is how we found out none of us knows the password."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
