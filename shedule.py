import time
from watchdog.observers import Observer
from shedule_class import FileSchedule

event_handler = FileSchedule()
observer = Observer()
path_to_file = r"C:\Users\Sovetov\PycharmProjects\PR2_Avdeev_PR-20.101\txts"
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except:
    print("Exception")
finally:
    observer.stop()
    observer.join()