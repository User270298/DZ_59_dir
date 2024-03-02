import os


def copy_file(old_path: str, new_path: str):
    with open(old_path, "br") as f:
        file = f.read()
    with open(new_path, "bw") as f:
        f.write(file)


def foo(old_dir: str, new_dir: str):
    if not os.path.exists(new_dir):
        print('Создана новая папка')
        os.mkdir(new_dir)
    for file in os.listdir(old_dir):
        _old_dir = old_dir + rf"\{file}"
        _new_dir = new_dir + rf"\{file}"
        if os.path.isdir(_old_dir):
            print(f'Скопирована и создана новая папка {file}')
            foo(_old_dir, _new_dir)
        else:
            print(f'Скопирован и создан файл {file}')
            copy_file(_old_dir, _new_dir)


old_path = input('Введите название папки, которую хотите скопировать:\n')
new_path = input('Введите название новой папки:\n')

foo(old_path, new_path)
