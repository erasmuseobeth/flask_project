import os
import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','','zip') 
with open('extracted_content'+'/Instructions.txt') as f:
    content = f.read()
    print(content)

