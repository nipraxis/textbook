""" This is my script

It uses mymodule
"""

import sys

import mymodule


def main():
    # This function executed when we are being run as a script
    print(sys.argv)
    filename = sys.argv[1]
    means = mymodule.vol_means(filename)
    for mean in means:
        print(mean)


if __name__ == '__main__':
    # We are being run as a script
    main()
