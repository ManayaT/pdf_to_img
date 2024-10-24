import os
from natsort import natsorted as nat

# os.mkdir("input")
# os.mkdir("output")
# os.mkdir("output/code_img")
# os.mkdir("output/name_img")
# os.mkdir("output/temp")
# os.mkdir("output/split_dir/")

target = "sample01-01.php_16.png"
dest = "sample01-01_php"

if dest.replace("_", ".") in target:
    print("find")

list_name = ['sample01-26_php', 'sample01-25_php', 'sample01-19_php', 'sample01-18_php', 'sample01-24_php', 'sample01-08_php', 'sample01-20_php', 'sample01-21_php', 'sample01-09_php', 'sample01-23_php', 'sample01-22_php', 'sample01-13_php', 'sample01-07_php', 'sample01-06_php', 'sample01-12_php', 'sample01-04_php', 'sample01-10_php', 'sample01-11_php', 'sample01-05_php', 'sample01-01_php', 'sample01-15_php', 'sample01-14_php', 'sample01-16_php', 'sample01-02_php', 'sample01-03_php', 'sample01-17_php']
#print(nat(list_name))

text = f"{target}{dest},png"

print(text)