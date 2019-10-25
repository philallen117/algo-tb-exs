#!/usr/bin/env python3
import sys
import os
import shutil

def pypaths(source, target):
    rdir = os.path.join("..", source)
    os.mkdir(target)
    for root, dirs, files in os.walk(rdir):
        for file in files:
            if file.endswith(".py"):
                shutil.copy(os.path.join(root, file), target)  

def main():
    print(sys.argv)
    pypaths(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
