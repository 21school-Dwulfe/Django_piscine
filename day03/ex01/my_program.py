#!/usr/bin/env python3

from path import Path

def main():
    try:
        dir = Path.walk
        Path.makedirs('path_result_folder')
    except FileExistsError as e:
        print(e)
    Path.touch('path_result_folder/result')
    f = Path('path_result_folder/result')
   
    file_count = 0
    dir_count = 0
    total = 0
    d = Path('./local_lib')
    for i in d.walk():
        if i.isfile():
            file_count += 1
        elif i.isdir():
            dir_count += 1
        else:
            pass
        total += 1

    f.write_lines(["Total number of files in local_lib == {0}".format(file_count), 
        "Total number of directories in local_lib == {0}".format(dir_count)])
    print(f.read_text())

if __name__ == '__main__':
    main()