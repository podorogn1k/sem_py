from pathlib import *

dir = input("Каталог: ").strip()
suf = input("Расширение: ").strip()
path = Path(dir)
if (not path.exists()):
    print(f"Ошибка; Каталог {path} не существует")
elif (not path.is_dir()):
    print(f"Ошибка; {path} не является каталогом")
else:
    if (not suf.startswith(".")):
        suf = '.' + suf
    cf = 0
    for fpath in path.rglob(f'*{suf}'):
        if (fpath.is_file()):
            cf += 1
            print(fpath, fpath.stat().st_size)
    if (cf == 0):
        print("Не найдено файлов с таким расширением")
    else:
        print(cf)