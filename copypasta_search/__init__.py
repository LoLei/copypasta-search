#!/usr/bin/env python3
"""
Get copypasta based on query
"""

__author__ = "Lorenz Leitner"
__version__ = "1.3"
__license__ = "MIT"

import argparse
from typing import Tuple, Optional

import praw
import pyperclip

CLI_USAGE = False


def search_and_get_pasta_if_exists(subreddit, query) -> Tuple[str, Optional[str]]:
    # Returns ListingGenerator - can't check if empty
    submissions = subreddit.search(query, limit=1)
    try:
        found_submission = list(submissions)[0]
        text = found_submission.selftext
        url = f"https://redd.it/{found_submission.id}"
        return text, url
    except IndexError:
        return 'Nothing found', None


def get_copypasta(query, print_pasta=False, copy_to_clipboard=False) -> Optional[Tuple[str, Optional[str]]]:
    reddit = praw.Reddit()
    subreddit = reddit.subreddit('copypasta')
    pasta, url = search_and_get_pasta_if_exists(subreddit, query)
    # PRAW might also return an empty string for some reason
    if not pasta:
        pasta = 'Nothing found'
    if copy_to_clipboard:
        pyperclip.copy(pasta)
    if print_pasta:
        print(pasta)
        print(url if url is not None else '')
    elif not print_pasta and not CLI_USAGE:
        return pasta, url


def main():
    global CLI_USAGE
    CLI_USAGE = True
    parser = argparse.ArgumentParser()

    parser.add_argument("query", help="search term")
    parser.add_argument("--hide", action="store_true", default=False,
                        help="do not print output to stdout")
    parser.add_argument("-c", "--copy", action="store_true", default=False,
                        help="copy pasta to clipboard")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    return get_copypasta(args.query, print_pasta=(not args.hide),
                         copy_to_clipboard=args.copy)


if __name__ == "__main__":
    main()
