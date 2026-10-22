from pathlib import Path
from os import access, R_OK

def read_file(path):
    file_path = Path(path)
    if (not file_path.exists()):
        print(f"Ошибка; Файла {path} не существует")
        return None
    if (file_path.is_dir()):
        print(f"Ошибка; {path} - каталог, а не файл")
        return None
    if (not access(file_path, R_OK)):
        print(f"Ошибка; Нет доступа к файлу {path}")
        return None
    with open(file_path) as f:
        return f.read()

print(read_file("8.txt") if read_file("8.txt") != None else "")