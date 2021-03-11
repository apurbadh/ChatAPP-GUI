from tkinter import *
import requests
import threading
import time

root = Tk()
root.title("DSS Chat System")

name_label = Label(text="Name : ")
usr_name_entry = Entry()

message_field = Text()
message_input = Entry()


def threadStart():
    thread1 = threading.Thread(target=getMessages)
    thread1.start()



def getMessages():
    while True:
        final_message = ""
        allMessages = requests.get("http://localhost:8000/show")
        message_field.delete(1.0, "end")
        my_json = (allMessages).json()
        for i in my_json:
            name = i["name"]
            mes = i["message"]
            final_message += f"{name} : {mes}\n"
        message_field.insert(1.0, final_message)
        time.sleep(1)


def sendMessage():
    name = usr_name_entry.get()
    message = message_input.get()
    requests.get("http://localhost:8000" + f"?name={name}&message={message}")
    message_input.delete(0, 'end')


submit_button = Button(text="Submit", command=sendMessage)
start_but = Button(text="Start", command=threadStart)

name_label.grid(row=0, column=0)
usr_name_entry.grid(row=0, column=1)
start_but.grid(row=0, column=2)

message_field.grid(row=1, column=0, columnspan=2)

message_input.grid(row=2, column=0, columnspan=2)
submit_button.grid(row=2, column=1)

root.mainloop()
