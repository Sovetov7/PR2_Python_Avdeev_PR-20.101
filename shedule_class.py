from watchdog.events import FileSystemEventHandler
znach: list = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы', 'a', 'e', 'i', 'o', 'u', 'y']

class FileSchedule(FileSystemEventHandler):
    def on_created(self, event):
        file_name: str = event.src_path.split("\\")
        name: str = file_name[-1].split(".")
        name_second: str = name[0]
        name_second.lower()
        for w in name_second:
            if w in znach:
                print(w.lower())
            else:
                print(w.upper())