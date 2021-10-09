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

    
    with open("link.txt", "r", encoding="utf-8") as f_link:
            for i in f_link:
                os.system(f"cd ..\\data && spotdl -b {i}")


    for root, dirs, files in os.walk("..\\data"):
            for i in files:
                f_name = i.split(".")
                destination = f".\\dl\\"
                os.system(f"spotdl -l ..\\data\\{i} -f {destination}{f_name[0]}")

    for root, dirs, files in os.walk(".\\dl\\"):
        for i in dirs:
                    os.rename(os.path.join(root, i), os.path.join(root, i.replace("-", " ")))


    if boold:
        print("end")
    return 0


if __name__ == "__main__":
    main()
