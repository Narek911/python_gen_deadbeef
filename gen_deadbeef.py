#! /usr/bin/python2
import argparse


def encode(data, size):
    encoded = ''
    count = int(size)
    while count:
        if count > len(data):
            for i in data:
                encoded += chr(ord(i) & 255)
            count -= len(data)
        else:
            for i in data[:count]:
                encoded += chr(ord(i) & 255)
            count = 0

    return encoded


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-size', help='the output file size')
    args = parser.parse_args()

    f = open("output.bin", "wb")

    s = '\xde\xad\xbe\xef'
    f.write(encode(s, args.size))
    f.close()