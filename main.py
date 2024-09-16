import tkinter as tk

FONT = ("Courier", 10)
window = tk.Tk()
window.title("Miles to Km")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
window.eval('tk::PlaceWindow . center')

def button_click():
    # Check if the input is a valid number
    user_input = in_field.get()
    try:
        miles = float(user_input)  # Convert to float for flexibility (in case of decimal values)
        km = miles * 1.60934  # Convert miles to kilometers
        calculated_km.config(text=f"{km:.2f}")  # Update label with km value
        notif_label.config(text="")  # Clear any previous error message
    except ValueError:
        notif_label.config(text="Please input numbers only",fg="reg")  # Display error message
#Label 
label = tk.Label(text="Is equal to", font=FONT)
calculated_km = tk.Label(text="0", font=FONT)
unit_miles = tk.Label(text="miles", font=FONT,padx=20)
unit_km = tk.Label(text="km", font=FONT,padx=20)
notif_label = tk.Label(text="", font=FONT)
#Button
button = tk.Button(text="Calculate",command=button_click, padx=5, pady=5,font=FONT)

#Entry field
in_field = tk.Entry()
in_field.config(width=25)

#Grid widget placements 
in_field.grid(column=1, row=0)
unit_miles.grid(column=2, row=0)
label.grid(column=0, row=1)
calculated_km.grid(column=1, row=1)
unit_km.grid(column=2, row=1)
button.grid(column=1, row=2)
notif_label.grid(column=1, row=3)  # Notification label layout


window.mainloop()