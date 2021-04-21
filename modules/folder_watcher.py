import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class FolderWather():

    def __init__(self, path):
        self.path = path
        self.patterns = "*"
        self.ignore_patterns = ""
        self.ignore_directories = False
        self.case_sensitive = True
        self.go_recursively = True
        self.my_event_handler = PatternMatchingEventHandler(self.patterns, self.ignore_patterns, self.ignore_directories, self.case_sensitive)
        self.my_observer = Observer()
        self.my_observer.schedule(self.my_event_handler, self.path, recursive=self.go_recursively)

    def start(self, on_created, on_deleted, on_modified, on_moved):
        self.my_event_handler.on_created = on_created
        self.my_event_handler.on_deleted = on_deleted
        self.my_event_handler.on_modified = on_modified
        self.my_event_handler.on_moved = on_moved

        self.my_observer.start()
        print("started")

    def stop(self):
        self.my_observer.stop()
        self.my_observer.join()
