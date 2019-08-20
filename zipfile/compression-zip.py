import zipfile as zp

with zp.ZipFile('hello.zip', 'w') as myzip:
    myzip.write('hello-1.txt')
    print(myzip.getinfo(zp.ZipFile))
    myzip.close()