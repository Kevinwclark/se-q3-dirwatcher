#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Kevin Clark"

import sys
import argparse
import logger
import signal


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def scan_single_file():
    pass


def detect_added_files():
    pass


def detect_removed_files():
    pass


def watch_directory(path, magic_string, extension, interval):
    # os.listdir() is a good way to see the dirs.
    # os.path.splitext(path) can be used to check for the extension
    return


def create_parser():
    parser = argparse.ArgumentParser(
        description="Watches specified directory.")
    # what dir to watch, magic string, extension and interval
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
    logger.warn('Received ' + signal.Signals(sig_num).name)
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
