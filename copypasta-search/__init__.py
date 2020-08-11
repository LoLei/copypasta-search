#!/usr/bin/env python3
"""
Get copypasta based on query
"""

__author__ = "Lorenz Leitner"
__version__ = "0.9.1"
__license__ = "MIT"

import argparse
import praw


def search_and_get_pasta_if_exists(subreddit, query):
    submissions = subreddit.search(query, limit=1)
    if submissions:
        return list(submissions)[0].selftext
    else:
        return False


def get_copypasta(query, print_pasta=False):
    reddit = praw.Reddit()
    subreddit = reddit.subreddit('copypasta')
    pasta = search_and_get_pasta_if_exists(subreddit, query)
    if print_pasta:
        print(pasta)
    return pasta


def main(query, print_pasta=False):
    return get_copypasta(query, print_pasta)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("query", help="search term")
    parser.add_argument("-s", "--show", action="store_true", default=False,
                        help="print output to stdout")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args.query, args.show)
