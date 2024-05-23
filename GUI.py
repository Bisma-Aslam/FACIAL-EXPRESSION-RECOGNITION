import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame
import subprocess
from PIL import Image, ImageTk  # Import PIL for working with images

def start_detection():
    # Execute the other Python script using subprocess
    subprocess.Popen(["python", "webcamdetection.py"])

# Create GUI window
root = tk.Tk()
root.title("Facial Expression Detection")

# Set background color to light pink
root.configure(background="#FFE0E6")

# Set the width of the canvas
canvas_width = 1200  # Adjust as needed

# Create a canvas
canvas = Canvas(root, background="#FFE0E6")
canvas.grid(row=0, column=0, sticky="nsew")

# Create a frame for the content
content_frame = Frame(canvas, background="#FFE0E6")

# Add a scrollbar
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)

# Add content to the frame
# Introduction label
intro_label = tk.Label(content_frame, text="Welcome to Facial Expression Detection!", font=("Helvetica", 16), background="#FFE0E6")
intro_label.grid(row=0, column=0, columnspan=6, pady=20)

# Introduction text
intro_text = """
Facial Expression Recognition (FER) is a fascinating field at the intersection of computer vision and psychology, aimed at deciphering human emotions through facial cues. By analyzing various features like eyebrow movement, eye dilation, and mouth shape, FER technology interprets subtle nuances to identify emotions such as happiness, sadness, anger, and surprise. With applications ranging from improving human-computer interaction to enhancing mental health diagnostics, FER holds promise for revolutionizing numerous industries and enriching our understanding of emotional communication.
"""
intro_text_label = tk.Label(content_frame, text=intro_text, font=("Helvetica", 12), wraplength=canvas_width, justify="left", background="#FFE0E6")
intro_text_label.grid(row=1, column=0, columnspan=6, pady=10)

# Load images
image1 = Image.open("./pichome.png")  # Adjust the path to your image file
image1 = image1.resize((500, 500), Image.LANCZOS)  # Resize the image as needed
photo1 = ImageTk.PhotoImage(image1)
image_label1 = tk.Label(content_frame, image=photo1, background="#FFE0E6")
image_label1.image = photo1  # Keep a reference to avoid garbage collection
image_label1.grid(row=2, column=0, columnspan=3, pady=10)

# Load images
image1 = Image.open("./webcampic.png")  # Adjust the path to your image file
image1 = image1.resize((500, 500), Image.LANCZOS)  # Resize the image as needed
photo1 = ImageTk.PhotoImage(image1)
image_label1 = tk.Label(content_frame, image=photo1, background="#FFE0E6")
image_label1.image = photo1  # Keep a reference to avoid garbage collection
image_label1.grid(row=2, column=4, columnspan=6, pady=10)


# Start button
start_button = tk.Button(content_frame, text="Start The Webcam", command=start_detection, font=("Times New Roman", 14))
start_button.grid(row=4, column=0, columnspan=6, pady=20)

# Update grid weights to center content
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
content_frame.grid_rowconfigure(0, weight=1)
for i in range(6):
    content_frame.grid_columnconfigure(i, weight=1)

# Bind the frame to the canvas
canvas.create_window(0, 0, window=content_frame, anchor="nw")

# Configure the canvas scrolling region
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run
root.mainloop()
