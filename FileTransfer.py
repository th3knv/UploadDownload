from anonfile import AnonFile
from pathlib import Path

while True:
    print('[1] Upload file')
    print('[2] Download file')

    choice_ =input('Enter choice number : ')

    # upload a file
    if choice_ =='1':
        chdir_ =input('Enter file path : ')
        anon = AnonFile()
        upload = anon.upload(chdir_ , progressbar=True)
        print(upload.url.geturl())
    else:
        print('Incorrect path or error occured')

    #download a file
    if choice_ =='2':
        dir_ =input('Enter directory path you want to store your file : ')
        target_dir = Path.home().joinpath(dir_)
        down_file =input('Enter anonfile link : ')
        filename = anon.download(down_file , path=target_dir)
        print(filename)
        print('File sucessfully downloaded in your chosen directory')
