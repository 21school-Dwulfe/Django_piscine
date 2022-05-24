import sys
import os
import settings

def main():
    if (len(sys.argv) != 2):
        raise RuntimeError("Invalid count of args!")
    if not sys.argv[1].endswith('.template'):
        raise RuntimeError("Invalid file extention,it have to be .templete")
    with open(sys.argv[1], 'r+') as file:
        list = file.readlines()
        full_string = ''.join(list)
        result = full_string.format(
            head=settings.head,
            body=settings.body,
            scripts=settings.scripts)

    with open(sys.argv[1].replace('.template', '.html'),'w') as output:
        output.write(result)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)