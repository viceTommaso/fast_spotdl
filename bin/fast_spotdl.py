# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os
import shutil


boold = False


def main():
    """
    main
    :return: 0
    """
    if boold:
        print("start")

    destination = ".\\dl\\"

    with open("link.txt", "r", encoding="utf-8") as f_link:
            for i in f_link:
                os.system(f"cd {destination} && spotdl {i}")


    if boold:
        print("end")
    return 0


if __name__ == "__main__":
    main()
