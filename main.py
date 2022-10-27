import time
from watchdog.observers import Observer
from shedule_class import FileSchedule
while True:
    file_name = input()
    if (len(file_name) < 3):
        print('Введите одно слово, состоящее из 3 и более символов')
        continue
    elif (file_name.isalpha() == False):
        print('Введите одно слово состоящее только из букв')
        continue
    else:
        while True:
            time.sleep(1)
            file = f"C:\\Users\\Sovetov\\PycharmProjects\\PR2_Avdeev_PR-20.101\\txts\\{file_name}.txt"
            with open(file, "w"):
                print("Файл успешно создан")
                break