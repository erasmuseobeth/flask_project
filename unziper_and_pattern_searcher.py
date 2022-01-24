import os
import shutil
import re


from_file = input("file path of file to unzip and search from ::")
to_file = input("unzip to which file location ? ::")
file_format = input("enter original file format ::")
rex_pattern =input("regular expresssion pattern to search for from unzipped files ::" )
rex_pattern = r'\d{3}-\d{3}-\d{4}'

shutil.unpack_archive(from_file,to_file,file_format) 
with open(to_file +'/Instructions.txt') as f:
    content  =f.read()
    print(content)


def search(file,rex_pattern):
    f = open(file,'r')
    text = f.read()

    if re.search(rex_pattern,text):
        return re.search(rex_pattern,text)

    else :
        return ''

results = []

for folders,sub_folders,files in os.walk(to_file +'/instructions.txt'):
    for f in files:
        full_path = folde+'/'+f
        results.append(search(full_path))
        for r in results:
            if r != '':
                print(r.group())
    
