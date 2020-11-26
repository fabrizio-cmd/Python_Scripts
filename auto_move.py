from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import filetype
import os
import time


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        new_folder_path = '/Users/fabri/Desktop' + '/'
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            filename_type = filetype.guess(src)
            if not os.path.exists(new_folder_path + filename_type.extension):
                os.makedirs(new_folder_path + filename_type.extension)
            print(filename_type.extension)
            new_destination = new_folder_path + filename_type.extension + "/" + filename
            os.rename(src, new_destination)


folder_to_track = "/Users/fabri/Desktop/pasta_inicial"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
