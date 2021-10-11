# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import shutil
import sys


boold = False


def main():
    """
    main
    :return: 0
    """
    if boold:
        print("start")

    destination = ".\\dl\\"
    f_in = ".\\link.txt"

    if len(sys.argv) >= 2:
        os.system(f"cd {destination} && spotdl {sys.argv[-1]}")
    else:
        if os.stat(f_in).st_size > 0:
            with open(f_in, "r", encoding="utf-8") as f_link:
                for i in f_link:
                    os.system(f"cd {destination} && spotdl {i}")
        else:
            link_in = input("\nLink brano/album/playlist:   ")
            os.system(f"cd {destination} && spotdl {link_in}")

    if boold:
        print("end")
    return 0


if __name__ == "__main__":
    main()
