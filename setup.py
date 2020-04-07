import os

shebang =  os.popen('which python3').read()
shebang= "#!"+shebang
command = "sed -i '1i"+shebang+"' gdrive.py"
os.system(command)
os.system('mv gdrvie.py /usr/local/bin/')
os.system('sudo ln -s /usr/local/bin/gdrive.py /usr/local/bin/gdrive')
print('Now you can call gdrive from anywhere')
print('Usage:gdrive <google drive link> <output filename>')
# sed -i '1s/^/task goes here\n/' todo.txt