from pathlib import *

dir_path = Path('.')
cf = 0
cd = 0
s = 0
py_files = []
for i in dir_path.glob('*'):
    if (i.is_file()):
        cf += 1
        s += i.stat().st_size
        if (i.suffix == '.py'):
            py_files.append(i)
    if (i.is_dir()):
        cd += 1
print(cf, cd, s, py_files)