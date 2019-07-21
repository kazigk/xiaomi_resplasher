import utils
import argparse
import os

parser = argparse.ArgumentParser(description='Silvertapes a Xiaomi splash image')
parser.add_argument('input', metavar='input_splash_image', type=str)
parser.add_argument('output', metavar='output_splash_image', type=str)
parser.add_argument('bi', metavar='bitmap.bmp:index', type=str, nargs='+')  # bi = bitmap + index
args = parser.parse_args()

if not os.path.exists(args.input):
    print("ERROR: Input file does not exist!")
    exit(1)

if os.path.exists(args.output):
    print("ERROR: Output file already exists!")
    exit(2)

with open(args.input, 'rb') as f:
    splash = f.read()
    f.close()

try:
    bitmaps = utils.find_all_bitmaps(splash)
except utils.WTFException:
    print("ERROR: Unable to find bitmaps in input file.")
    exit(3)

bitmaps_length = len(bitmaps)

for bi in args.bi:
    b, i = bi.split(':')
    index = int(i)

    if not os.path.exists(b):
        print("ERROR: File not found ({0})".format(b))
        exit(4)

    with open(b, 'rb') as f:
        bitmap = f.read()
        f.close()

    if index >= bitmaps_length:
        print("Error: Invalid index ({0})".format(i))
        exit(5)

    offset, original_size = bitmaps[index]
    size = len(bitmap)

    if size > original_size:
        print("Error: Bitmap is too big!")
        exit(5)

    if size < original_size:
        bitmap += b'\x00' * (original_size - size)

    splash = utils.silvertape_segment(splash, bitmap, offset)

with open(args.output, 'wb') as f:
    f.write(splash)

print('Splash image silvertaped successfully! :D')

