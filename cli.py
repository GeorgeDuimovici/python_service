#!/usr/bin/env python3
"""CLI tool to fetch weather information for a given location using wttr.in API."""

import sys
import requests


def main():
    """Main function to handle command line arguments and fetch weather data."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <location>")
        sys.exit(1)
    location = sys.argv[1]
    url = f"https://wttr.in/{location}"
    response = requests.get(url, timeout=10)
    print(response.text)


if __name__ == "__main__":
    main()
