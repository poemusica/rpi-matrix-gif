"""
Displays 32x32 animated gif on Adafruit RGB LED Matrix.

Running this code assumes that you have followed the instructions and installed
the dependencies as described in the README file:
https://github.com/poemusica/rpi-matrix-gif/blob/master/README.md

Requires rgbmatrix.so to be present in the same directory as this script.

Gif extraction code copied from BigglesZX's github gist (thank you!):
https://gist.github.com/BigglesZX/4016539
"""


import Image
import os
import time
from rgbmatrix import Adafruit_RGBmatrix


def analyseImage(path):
    """
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    """
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


def processImage(path):
    """
    Iterate the GIF, extracting each frame.
    """
    mode = analyseImage(path)['mode']
    
    im = Image.open(path)

    frames = []

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')
    
    try:
        while True:            
            '''
            If the GIF uses local colour tables, each frame will have its own palette.
            If not, we need to apply the global palette to the new frame.
            '''
            if not im.getpalette():
                im.putpalette(p)
            
            new_frame = Image.new('RGBA', im.size)
            
            '''
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
            If so, we need to construct the new frame by pasting it on top of the preceding frames.
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)
            
            new_frame.paste(im, (0,0), im.convert('RGBA'))
            frames.append(new_frame)

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass

    return frames


def main():
    frames = processImage('/home/pi/rpi-matrix-gif/myGIF.gif')
    matrix = Adafruit_RGBmatrix(32, 1)
    while True:
        for f in frames:
    		matrix.SetImage(f.im.id, 0, 0)
    		time.sleep(0.1)
    

if __name__ == "__main__":
    main()
