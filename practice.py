## Tkinter test usage
import tkinter
FONT = ("Courier", 14, "bold")
window = tkinter.Tk()
window.title("Miles to Km")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# def add(*args):
#     add_list = [n for n in args]
#     return sum(add_list)

# print(add(1,2,3,4,5,4,6,7,5))

def button_click():
    user_en = in_field.get()
    label.config(text=f"{user_en}!")
    print("Click Detected")
    
#Label 
label = tkinter.Label(text="This is a label", font=FONT)
#Button
button = tkinter.Button(text="Button",command=button_click)
button2 = tkinter.Button(text="New Button",command=button_click)
#Entry
in_field = tkinter.Entry()


label.grid(column=0, row=0)
button.grid(column=1, row=1)
button2.grid(column=2, row=0)
in_field.grid(column=3, row=2)


window.mainloop()

