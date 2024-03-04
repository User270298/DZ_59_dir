import os
import thread

path = 'old_dir'
word_file = 'Mat.txt'
reject = 'reject'


class Operation:
    def read_word(self) -> list[str]:
        with open(self, 'r') as f:
            read = f.readlines()
        new = []
        for word in read:
            new.append(word.replace('\n', ''))
        return new

    def read_file(self) -> str:
        with open(self, 'r') as f:
            return f.read()

    def print_file(self):
        with open(self, 'r') as f:
            print(f.read())

    def copy_file(self: str, new_path: str):
        with open(self, "br") as f:
            file = f.read()
        with open(new_path, "bw") as f:
            f.write(file)

    def search_word(self: str, word: str) -> bool:
        for i in self.split():
            if i in word:
                return True
        return False


def copy_file_mat(path, reject):
    for file in os.listdir(path):
        if os.path.isdir(path + '\\' + file):
            print(f'Проверка {file}')
            copy_file_mat(path + '\\' + file, reject)
        else:
            if not os.path.exists(reject):
                print('Создана новая папка')
                os.mkdir(reject)
            word = Operation.read_word(word_file)
            create_file = Operation.read_file(path + '\\' + file)
            if Operation.search_word(create_file, word):
                print(f'В {file} найден мат - скопирован файл {file} в {reject}')
                Operation.copy_file(path + '\\' + file, reject + '\\' + file)
            else:
                print(f'В {file} матерных слов не найдено')


def delete_mat(path):
    for file in os.listdir(path):
        if os.path.isdir(path + '\\' + file):
            print(f'Проверка {file}')
            delete_mat(path + '\\' + file)
        else:
            print('Это файл')
            create_file = Operation.read_file(path + '\\' + file)
            create_path = path + '\\' + file
            word = Operation.read_word(word_file)
            if Operation.search_word(create_file, word):
                print(f'Содержимое файла {create_file.split()}')
                for i in create_file.split():
                    if i in word:
                        print(f'Изменение {create_path}')
                        with open(create_path, 'w') as f:
                            f.write(create_file.replace(i, ''))


if __name__ == '__main__':
    th1 = thread.Thread(target=copy_file_mat, args=(path, reject))
    th1.start()
    th1.join()
    th2 = thread.Thread(target=delete_mat, args=(path,))
    th2.start()
