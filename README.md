# Xiaomi Resplasher
A tool designed to extract bitmaps from splash image and glue the modified version together.

## Why?
Because the already existing tools weren't universal, closed-source and Windows only.

## Usage
Extraction:
`python extract.py <splash.img>`

Duct-taping the shit together:
`python silvertape.py <splash.img> <output_filename.img> <bitmap.bmp:index> [bitmap.bmp:index ...]`

Index specifies the bitmap that you want to replace.
If you had extracted it using my tool, the filename indicates the index,
for example: 0.bmp is containing the bitmap extracted from index 0.

## Compatibility
- Xiaomi Mi A2 - fully tested and working
- Xiaomi Redmi Note 5 - fully tested and working
- Xiaomi Redmi Note 6 - partially tested *
- Xiaomi Redmi Note 7 - partially tested *
- Xiaomi Mi 8 - partially tested *
- Xiaomi Mi 9 - partially tested *
- Xiaomi Redmi Note 3 - not working at all
- Xiaomi Redmi Note 4 - not working at all

\* I do not own the device. Extraction works, nothing further tested.

Please tell me if it worked with the device not listed there by opening an issue, thanks.

## Warning
**I do not take any responsibility** for damaged devices, murdered mothers in law, nuclear war or some shit like that.

This tool is only checking if the modified bitmap will fit into the original place in your splash image.
I don't check bitmap resolution, color coding and more shit like this.

Can it break your device? No. Even if you completely erase splash partition, your phone will boot successfully,
but without displaying any splash image. Just don't be scared if you boot into fastboot after fuck up and you see a black screen.

But just in case you are an idiot or something, again: **i do not take any responsibility**.

PS: If something goes wrong, you can open an issue.