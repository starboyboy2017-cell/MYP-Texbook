"""Fetch the upstream fonts the rebuild uses.

The book's own embedded subsets are damaged (their streams fail a zlib check in
the input file), so the faces are rebuilt from their upstream releases and cut
down to the codes each face actually needs.  Run this once before `build_fonts.py`
if `fonts/` is empty.

    python3 tools/fetch_fonts.py
"""
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UPSTREAM = os.path.join(HERE, "..", "upstream")

SOURCES = {
    # STIX Two: the text faces, plus the maths face that carries the symbols
    "STIXTwoText-Regular.otf": "https://github.com/stipub/stixfonts/raw/master/fonts/static_otf/STIXTwoText-Regular.otf",
    "STIXTwoText-Italic.otf": "https://github.com/stipub/stixfonts/raw/master/fonts/static_otf/STIXTwoText-Italic.otf",
    "STIXTwoText-SemiBold.otf": "https://github.com/stipub/stixfonts/raw/master/fonts/static_otf/STIXTwoText-SemiBold.otf",
    "STIXTwoMath.ttf": "https://github.com/stipub/stixfonts/raw/master/fonts/static_otf/STIXTwoMath-Regular.otf",
    # Playfair Display: chapter titles and display text
    "PlayfairDisplay-Regular.ttf": "https://github.com/clauseggers/Playfair/raw/master/fonts/PlayfairDisplay-Regular.ttf",
    "PlayfairDisplay-SemiBold.ttf": "https://github.com/clauseggers/Playfair/raw/master/fonts/PlayfairDisplay-SemiBold.ttf",
    "PlayfairDisplay-Italic.ttf": "https://github.com/clauseggers/Playfair/raw/master/fonts/PlayfairDisplay-Italic.ttf",
    # Inter: labels, running heads, tables
    "Inter-Regular.ttf": "https://github.com/rsms/inter/raw/master/docs/font-files/Inter-Regular.ttf",
    "Inter-Medium.ttf": "https://github.com/rsms/inter/raw/master/docs/font-files/Inter-Medium.ttf",
    "Inter-SemiBold.ttf": "https://github.com/rsms/inter/raw/master/docs/font-files/Inter-SemiBold.ttf",
}


def main():
    os.makedirs(UPSTREAM, exist_ok=True)
    for name, url in SOURCES.items():
        path = os.path.join(UPSTREAM, name)
        if os.path.exists(path):
            print(f"have  {name}")
            continue
        print(f"fetch {name}")
        try:
            with urllib.request.urlopen(url) as r, open(path, "wb") as f:
                f.write(r.read())
        except Exception as exc:                      # noqa: BLE001
            print(f"  failed: {exc}", file=sys.stderr)
    print("now run: python3 tools/build_fonts.py")


if __name__ == "__main__":
    main()
