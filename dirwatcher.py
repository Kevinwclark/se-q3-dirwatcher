#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Kevin Clark with help from JT and Joseph Hafed"

import sys
import argparse
import logging
import signal
import time
import os


exit_flag = False


def search_for_magic(path, filename, start_line, magic_string):
    line_number = start_line
    with open(f'{path}/{filename}') as f:
        lines = f.readlines()
    num_of_lines = len(lines)
    for i in range(start_line, num_of_lines):
        if magic_string in lines[i]:
            print(f'word found in {filename} {i + 1}!')
            # logging moment here
        line_number = i + 1
    return line_number


def detect_removed_files():
    pass


def watch_directory(path, magic_string, extension, interval):
    dictionary = {}
    while not exit_flag:
        time.sleep(interval)
        if os.path.isdir(path):
            file_list = os.listdir(path)
            for files in file_list:
                if files.endswith(extension) and files not in dictionary:
                    dictionary[files] = 0
                    print(f'file added {files}')
                    # logging moment here
            key = list(dictionary.keys())
            for k in key:
                if k not in file_list:
                    print(f'this file was removed {k}')
                    dictionary.pop(k)
                    # logging moment here
            for key, value in dictionary.items():
                dictionary[key] = search_for_magic(path, key, value, magic_string)
            print(dictionary)

        else:
            print("this path does not exist")
            dictionary = {}
        
    pass


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
    global exit_flag
    exit_flag = True
    logging.warning('Received ' + signal.Signals(sig_num).name)
    return


def main(args):
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

    while not exit_flag:
        # start_time = time.time()
        # stop_time when signal is received to stop running. 
        # then log the start_time - stop_time
        try:
            print('something')
            watch_directory(path, magic, ext, integer)
        except FileNotFoundError as err:
            print('Sorry, this file does not exist')
            logging.error(err)
      
    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start
    return


if __name__ == '__main__':
    main(sys.argv[1:])
