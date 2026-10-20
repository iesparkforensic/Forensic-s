#!/usr/bin/env python3
"""Open a list of websites in your default browser, one at a time, with a delay between each.

Usage:
    python site_opener.py sites.txt                 # read URLs from a file (one per line)
    python site_opener.py example.com github.com    # pass URLs directly
    python site_opener.py sites.txt -i 5            # custom interval in seconds
    python site_opener.py sites.txt --new-window    # open each site in a new window instead of a tab

In the sites file, blank lines and lines starting with '#' are ignored.
Press Ctrl+C at any time to stop.
"""

import argparse
import os
import sys
import time
import webbrowser


def normalize(url):
    url = url.strip()
    if "://" not in url:
        url = "https://" + url
    return url


def load_sites(sources):
    sites = []
    for source in sources:
        if os.path.isfile(source):
            with open(source, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        sites.append(normalize(line))
        else:
            sites.append(normalize(source))
    return sites


def main():
    parser = argparse.ArgumentParser(
        description="Open a list of sites in your browser with a delay between each."
    )
    parser.add_argument(
        "sources",
        nargs="+",
        help="URLs and/or paths to text files containing one URL per line",
    )
    parser.add_argument(
        "-i", "--interval", type=float, default=10,
        help="seconds to wait between opening sites (default: 10)",
    )
    parser.add_argument(
        "--new-window", action="store_true",
        help="open each site in a new browser window instead of a new tab",
    )
    args = parser.parse_args()

    sites = load_sites(args.sources)
    if not sites:
        sys.exit("No sites to open.")

    total = len(sites)
    print(f"Opening {total} site(s), {args.interval:g}s apart. Press Ctrl+C to stop.")
    try:
        for n, url in enumerate(sites, 1):
            print(f"[{n}/{total}] {url}")
            if args.new_window:
                webbrowser.open_new(url)
            else:
                webbrowser.open_new_tab(url)
            if n < total:
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped.")
        return
    print("Done.")


if __name__ == "__main__":
    main()
