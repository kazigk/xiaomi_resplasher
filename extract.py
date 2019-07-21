import utils
import argparse
import os

parser = argparse.ArgumentParser(description='Extracts bitmaps from Xiaomi splash images')
parser.add_argument('splash', metavar='splash.img', type=str)
args = parser.parse_args()

if not os.path.exists(args.splash):
    print("ERROR: Specified splash file not found!")
    exit(1)

# open and read the file
with open(args.splash, 'rb') as f:
    splash = f.read()
    f.close()

try:
    bitmaps = utils.find_all_bitmaps(splash)
except utils.WTFException:
    print('ERROR: Unable to find bitmaps.')
    exit(2)

counter = 0
for offset, size in bitmaps:
    with open('{0}.bmp'.format(counter), 'wb') as f:
        f.write(splash[offset:offset+size])
        f.close()

    counter += 1

print('Bitmaps extracted successfully :)')
