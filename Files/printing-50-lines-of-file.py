from os import path
import os

def fileexists():
    if ( path.exists("C:\purushotham\Learning\python-learning\Python-practice\Files\Git-commands.txt") and path.isfile("C:\purushotham\Learning\python-learning\Python-practice\Files\Git-commands.txt")):
       return True
    else:
       return False

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize - 1
            data = []
            while True:
                iter += 1
                f.seek(fsize - bufsize * iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break

def main():
    if fileexists():
        file_read_from_tail("C:\purushotham\Learning\python-learning\Python-practice\Files\Git-commands.txt",5)

if __name__ == "__main__":
    main()
