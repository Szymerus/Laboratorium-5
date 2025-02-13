#10. Write a Python program that customizes the appearance of labels and buttons (e.g., fonts, colors) using Tkinter. 
import tkinter as tk
from tkinter import font

def on_button_click():
    current_text = label.cget("text")
    if current_text == "Serwus!":
        label.config(text="Kliknąłeś!", fg="green")
    else:
        label.config(text="Po co dalej wciskasz?! Daj sobie już spokój", fg="black")

# Create the main window
root = tk.Tk()
root.title("Custom Tkinter UI")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Define custom font
custom_font = font.Font(family="Arial", size=14, weight="bold")

# Create a label with custom styling
label = tk.Label(root, text="Serwus!", font=custom_font, fg="blue", bg="#f0f0f0")
label.pack(pady=20)

# Create a button with custom styling
button = tk.Button(root, text="Naciśnij mnie!", font=custom_font, fg="white", bg="green", padx=10, pady=5, command=on_button_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()
