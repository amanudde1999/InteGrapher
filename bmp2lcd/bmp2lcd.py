# Adapted from https://forum.arduino.cc/index.php?topic=356479.0

import sys
from PIL import Image

if len(sys.argv) == 3:
    # print "\nReading: " + sys.argv[1]
    out = open(sys.argv[2], "wb")
else:
    print()
    print("Usage: png2fb.py <infile.bmp> <outfile.lcd>")
    print()
    sys.exit(0)


im = Image.open(sys.argv[1])

if im.mode == "RGB":
    pixelSize = 3
elif im.mode == "RGBA":
    pixelSize = 4
else:
    sys.exit('not supported pixel mode: "%s"' % (im.mode))

pixels = im.tobytes()
pixels2 = []
for i in range(0, len(pixels) - 1, pixelSize):
    pixels2.append((pixels[i + 2] >> 3) | ((pixels[i + 1] << 3) & 0xe0))
    pixels2.append((pixels[i] & 0xf8) | ((pixels[i + 1] >> 5) & 0x07))
out.write(bytes(pixels2))
out.close()

infoFileName = sys.argv[2]+".txt"
info = open(infoFileName, "w")
print("Information for .lcd file:", sys.argv[2], file=info)
print("Source:", sys.argv[1], file=info)
print("Width  (in pixels):", im.width, file=info)
print("Height (in pixels):", im.height, file=info)

print()
print("Created file", sys.argv[2])
print("File information (including width/height) written to", infoFileName)
print()
