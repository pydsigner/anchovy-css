from __future__ import annotations

import argparse
from pathlib import Path

from .parser import process


def main():
    """
    Anchovy main function. Finds or creates a Context using an Anchovy config
    file and command line arguments, then executes a build using it.
    """
    parser = argparse.ArgumentParser(description='Build an anchovy project.')
    parser.add_argument('source_file',
                        help='path to the input Anchovy CSS file',
                        type=Path)
    parser.add_argument('output_file',
                        help='path to the output vanilla CSS file',
                        type=Path)

    args = parser.parse_args()
    processed = process(args.source_file.read_text('utf-8'))
    args.output_file.write_text(processed, 'utf-8')
