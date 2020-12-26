import time
from datetime import datetime
import boto3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
import mysql.connector


class EventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        file = open("/PATH/TO/LOG/FILE")
        string = file.read()
        #INSERT STRING TO SQL DB
        db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="logDB"
        )
        mycursor = db.cursor()
        sql = "INSERT INTO logs (time, data) VALUES (%s, %s)"
        now = datetime.now()
        now = now.strftime("%m/%d/%Y, %H:%M:%S")
        val = (now, string)
        mycursor.execute(sql, val)
        mydb.commit()


if __name__ == "__main__":
    path = "/PATH/TO/LOG/FILE"
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()