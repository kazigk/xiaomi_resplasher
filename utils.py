bmp_header = b'BM'

# all above this is considered as invalid bitmap
# i'm just too lazy to do it "the right way"
bmp_maxsize = 10000000


def find_all_occurs(inwhat, what):
    occurs = []

    o = inwhat.find(what)
    if o == -1:
        raise WTFException
    occurs.append(o)

    while True:
        o = inwhat.find(what, occurs[-1] + 1)
        if o == -1:
            return occurs
        occurs.append(o)


def find_all_bitmaps(data):
    result = []

    for offset in find_all_occurs(data, bmp_header):
        size = int.from_bytes(data[offset+2:offset+7], byteorder='little')
        if size > 10000000:
            continue

        result.append((offset, size))

    if len(result) == 0:
        raise WTFException

    return result


def silvertape_segment(data, inset, offset):
    return data[:offset] + inset + data[offset+len(inset):]


# just to make sure i'm catching only exceptions raised by myself
class WTFException(Exception):
    pass
