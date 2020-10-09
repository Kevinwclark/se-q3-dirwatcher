#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Kevin Clark with help from JT and Joseph Hafed"

import sys
import argparse
# import logger
import signal


dictionary = {} # keys will be filenames and values will be last line read
# exit flag


def search_for_magic(filename, start_line, magic_string):
    line_number = 0
    with open(filename) as f:
        lines = f.readlines()
    num_of_lines = len(lines)
    for i in range(start_line, num_of_lines):
        if magic_string in lines[i]:
            line_number = i + 1
    return line_number


def scan_single_file():
    pass


def detect_added_files():
    pass


def detect_removed_files():
    pass


def watch_directory(path, magic_string, extension, interval):
    return


def create_parser():
    parser = argparse.ArgumentParser(
        description="Watches specified directory for magic word.")
    parser.add_argument('directory', help='directory to watch')
    parser.add_argument('magic', help='word to scan directory for')
    parser.add_argument('-e', '--extension', help='file extension to search',
                        default='.txt')
    parser.add_argument('-i', '--integer', help='poll int, defaults to 1 sec',
                        type=float, default=1.0)
    return parser


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals
    can be mapped here as well (SIGHUP?)
    Basically, it just sets a global flag, and main() will              
    exit its loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name
    # logger.warn('Received ' + signal.Signals(sig_num).name)
    return


def main(args):
    """Implementation of dirwatcher"""
    parser = create_parser()
    ns = parser.parse_args(args)
    print(ns)

    if not ns:
        parser.print_usage(args)
        sys.exit(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
    print(sys.argv[1:])
