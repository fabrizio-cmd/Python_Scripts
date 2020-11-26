from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler
import filetype
import os
import json
import time

types_files = ('pdf', 'exe', 'zip',)
types_images = ('jpg', 'png', 'gif')



class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        for filename in os.listdir(folder_to_track):
            src_type = filetype.guess(folder_to_track + "/" + filename)
            src = folder_to_track + "/" + filename

            if str(src_type.extension) == types_files[0]:
                new_destination = pdf_folder + "/" + filename
                os.rename(src, new_destination)
            elif str(src_type.extension) == types_files[2]:
                new_destination = rar_folder + "/" + filename
                os.rename(src, new_destination)
            elif src_type.extension in types_images:
                new_destination = image_folder + "/" + filename
                os.rename(src, new_destination)
            else:
                print("Error")


rar_folder = "/Users/fabri/Desktop/pasta_rar"
image_folder = "/Users/fabri/Desktop/pasta_imagens"
pdf_folder = "/Users/fabri/Desktop/pasta_pdf"
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
