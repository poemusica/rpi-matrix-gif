"""Displays an animated gif on a 32x32 RGB LED Adafruit Matrix."""

import argparse
from pathlib import Path
import time

from PIL import Image, ImageSequence
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def get_frames(path):
    """Returns an iterable of gif frames."""
    frames = []
    with Image.open(path) as gif:
        for frame in ImageSequence.Iterator(gif):
            frame = frame.convert('RGB').resize((32, 32))
            frames.append(frame)
        return frames


def display_gif(path):
    """Displays gif frames on matrix."""
    options = RGBMatrixOptions()
    options.rows = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    matrix = RGBMatrix(options=options)
    
    while True:
        for frame in get_frames(path):
            matrix.SetImage(frame)
            time.sleep(frame.info['duration']/1000)


def _get_parser():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description='Display gif on LED matrix.')
    parser.add_argument('gif_path',
                        nargs='?',
                        metavar='PATH_TO_GIF',
                        type=Path,
                        default=Path(__file__).parent / 'myGIF.gif',
                        help='the path to the gif file')
    
    return parser


if __name__ == '__main__':
    print('*********************************************\n'
          'display_gif script created by Heather Mahan.\n'
          'For more information, see documentation at\n'
          'https://github.com/poemusica/rpi-matrix-gif\n'
          '*********************************************')
    
    parser = _get_parser()
    args = parser.parse_args()
    parser.print_help()
    
    print('*********************************************'
          '\nThis script uses the rgbmatrix library by hzeller:\n'
          'https://github.com/hzeller/rpi-rgb-led-matrix')
    
    display_gif(args.gif_path)
