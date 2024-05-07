#!/usr/bin/env python3

import os
import shutil
import subprocess
import tempfile


def main():
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        subprocess.check_output(["binwalk", "-e", "-M", "-0", "root", "/input"])
        # look for the following directory: "/etc" and copy "/" to "/output"
        for root, dirs, files in os.walk(tmpdirname):
            if "etc" in dirs:
                subprocess.check_output(["cp", "-ra", os.path.join(root, '.'), "/output"])
                break
    with open("/output/Dockerfile", "w") as f:
        f.write("FROM scratch\n")
        f.write("COPY . /\n")



if __name__ == "__main__":
    main()
