#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Kevin Clark, help from JT and Joseph Hafed and Jalal Belsifar"

import sys
import argparse
import logging
import signal
import time
import os
import datetime


exit_flag = False
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def search_for_magic(path, filename, start_line, magic_string):
    """Search file for magic word"""
    line_number = start_line
    with open(f'{path}/{filename}') as f:
        lines = f.readlines()
    num_of_lines = len(lines)
    for i in range(start_line, num_of_lines):
        if magic_string in lines[i]:
            logging.info(f'Magic word found in {filename} on line {i + 1}!')
        line_number = i + 1
    return line_number


def watch_directory(path, magic_string, extension, interval):
    """Track directory files"""
    dictionary = {}
    while not exit_flag:
        time.sleep(interval)
        file_list = os.listdir(path)
        for files in file_list:
            if files.endswith(extension) and files not in dictionary:
                dictionary[files] = 0
                logging.info(f'File that matches extension: {files}')
        key = list(dictionary.keys())
        for k in key:
            if k not in file_list:
                dictionary.pop(k)
                logging.info(f'This file was removed {k}')
        for key, value in dictionary.items():
            dictionary[key] = search_for_magic(
                path, key, value, magic_string
                )


def create_parser():
    """Parse cmd line args"""
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
    """This is a handler for SIGTERM and SIGINT"""
    global exit_flag
    exit_flag = True
    logging.warning('Received ' + signal.Signals(sig_num).name)
    return


def main(args):
    """Main entry point for program"""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage(args)
        sys.exit(1)

    path = ns.directory
    magic = ns.magic
    ext = ns.extension
    integer = ns.integer
    start_time = datetime.datetime.now()
    logging.info(f"""
    --------------------------------------------------\n
            Running: dirwatcher.py\n
            Started on: {start_time}\n
    --------------------------------------------------\n
    """)

    while not exit_flag:
        try:
            watch_directory(path, magic, ext, integer)
        except OSError:
            logging.error(f'Not finding this path: {os.path.abspath(path)}')
        except Exception as e:
            logging.error(f'{e}')
        time.sleep(integer)
    uptime = datetime.datetime.now() - start_time

    logging.info(f"""
    --------------------------------------------------\n
            Stop: dirwatcher.py
            Uptime: {uptime}\n
    --------------------------------------------------\n
    """)


if __name__ == '__main__':
    main(sys.argv[1:])
