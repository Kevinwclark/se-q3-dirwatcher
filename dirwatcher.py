#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Kevin Clark"

import sys
import argparse


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    parser = argparse.ArgumentParser(
        description="Watches specified directory.")
    return parser


def signal_handler(sig_num, frame):
    # Your code here
    return


def main(args):
    """Implementation of dirwatcher"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage(args)
        sys.exit(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
