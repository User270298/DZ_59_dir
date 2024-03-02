import os
import thread


path = 'old_dir'
word = 'Mat.txt'
reject='reject'

def read_word(file) -> str:
    with open(file, 'r') as f:
        read = f.readlines()
    new=[]
    for word in read:
        s=word.replace('\n', '')
        new.append(s)
    return new
print(read_word(word))

def read_file(file) -> str:
    with open(file, 'r') as f:
        read = f.read()
    return read

word=read_word(word)

def copy_file(old_file: str, new_path: str):
    with open(old_file, "br") as f:
        file = f.read()
    with open(new_path, "bw") as f:
        f.write(file)
def search_word(file: str, word: str):
    for i in file.split():
        if i in word:
            return True
    return False
def search_file(path, reject):
    for file in os.listdir(path):
        if os.path.isdir(path + '\\' + file):
            print(f'Проверка {file}')
            search_file(path + '\\' + file, reject)
        else:
            if not os.path.exists(reject):
                print('Создана новая папка')
                os.mkdir(reject)
            create_file = read_file(path + '\\' + file)
            if search_word(create_file, word):
                print(f'В {file} найден мат - скопирован файл {file} в {reject}')
                copy_file(path + '\\' + file, reject+'\\'+file)
            else:
                print(f'В {file} матерных слов не найдено')

def read(file):
    with open(file, 'r') as f:
        s=f.read()
        print(s)
def delete_mat(path):
    for file in os.listdir(path):
        if os.path.isdir(path + '\\' + file):
            print(f'Проверка {file}')
            delete_mat(path + '\\' + file)
        else:
            print('Это файл')
            create_file = read_file(path + '\\' + file)
            create_path=path + '\\' + file
            if search_word(create_file, word):
                print(f'Содержимое файла {create_file.split()}')
                for i in create_file.split():
                    if i in word:
                        print(f'Изменение {create_path}')
                        with open(create_path, 'w') as f:
                            f.write(create_file.replace(i,''))



if __name__ == '__main__':
    th1=thread.Thread(target=search_file, args=(path,reject))
    th1.start()
    th1.join()
    thread.Thread(target=delete_mat, args=(path, )).start()

