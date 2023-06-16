from tkinter import Tk, Button, Canvas, PhotoImage, NW, Label
import subprocess

def start_game():
    subprocess.run(["python", "C:\\Users\\liu72\\Downloads\\game_folder\\pointGeneration.py"])

root = Tk()

root.geometry("1000x1000")

# Load the background image
bg = PhotoImage(file="C:\\Users\\liu72\\Downloads\\game_folder\\map_image.py.png")

canvas = Canvas(root, width=1000, height=1000)
canvas.pack(fill = "both", expand = True)

canvas.create_image(0, 0, image=bg, anchor=NW)

label = Label(root, text="Game Title", font=("Arial", 24, "bold"))
label.pack(pady=20)

start_button = Button(root, text="Start Game", command=start_game, font=("Arial", 18, "bold"), padx=50, pady=20)

canvas.create_text(500, 400, text="World Simulation Game", font=("Arial", 40, "bold"), fill="white")

# Reduce the rely value to move the button up
start_button.place(relx=0.5, rely=0.5, anchor="n")

root.mainloop()
