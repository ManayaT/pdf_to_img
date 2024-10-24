import os

try:
    os.mkdir("input")
    os.mkdir("output")
    os.mkdir("output/code_img")
    os.mkdir("output/name_img")
    os.mkdir("output/temp")
    os.mkdir("output/split_dir/")
except Exception as e:
    print(f"{e}")
