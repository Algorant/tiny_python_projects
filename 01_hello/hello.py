#!/usr/bin/env python
"""
Author: Ivan
Purpose: Say Hello!
"""
# Puprose: Say Hello

import argparse


def get_args():
    """
    Get Arguments for the function.
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to greet')

    return parser.parse_args()


def main():
    """
    Run the main function.
    """
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
