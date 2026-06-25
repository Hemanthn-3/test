from tkinter import *
from tkinter import messagebox
import qrcode
import os

# Save note as note1.txt, note2.txt, ...
def save_note():
    note = text_area.get("1.0", END).strip()

    if note == "":
        messagebox.showwarning("Warning", "Note is empty!")
        return

    count = 1
    while os.path.exists(f"note{count}.txt"):
        count += 1

    filename = f"note{count}.txt"

    with open(filename, "w") as file:
        file.write(note)

    messagebox.showinfo(
        "Success",
        f"Note saved as {filename}"
    )

    text_area.delete("1.0", END)


# Open file by name
def open_file():
    filename = file_name_entry.get().strip()

    if filename == "":
        messagebox.showwarning("Warning", "Enter file name!")
        return

    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "r") as file:
            content = file.read()

        text_area.delete("1.0", END)
        text_area.insert(END, content)

    except FileNotFoundError:
        messagebox.showerror("Error", f"{filename} not found!")


# Generate QR code
def generate_qr():
    note = text_area.get("1.0", END).strip()

    if note == "":
        messagebox.showwarning(
            "Warning",
            "Enter text to generate QR code!"
        )
        return

    qr = qrcode.make(note)
    qr.save("note_qr.png")

    messagebox.showinfo(
        "Success",
        "QR Code saved as note_qr.png"
    )


# Delete file by name
def delete_file():
    filename = file_name_entry.get().strip()

    if filename == "":
        messagebox.showwarning(
            "Warning",
            "Enter file name!"
        )
        return

    if not filename.endswith(".txt"):
        filename += ".txt"

    if os.path.exists(filename):
        os.remove(filename)
        messagebox.showinfo(
            "Success",
            f"{filename} deleted successfully!"
        )
    else:
        messagebox.showerror(
            "Error",
            f"{filename} not found!"
        )


# Main Window
root = Tk()
root.title("Notes App with QR Generator")
root.geometry("500x550")

# Heading
Label(
    root,
    text="Simple Notes App",
    font=("Arial", 18, "bold")
).pack(pady=10)

# File Name Entry
Label(
    root,
    text="Enter File Name:",
    font=("Arial", 12)
).pack()

file_name_entry = Entry(
    root,
    width=30,
    font=("Arial", 12)
)
file_name_entry.pack(pady=5)

# Text Area
text_area = Text(
    root,
    width=50,
    height=15,
    font=("Arial", 12)
)
text_area.pack(pady=10)

# Buttons
Button(
    root,
    text="Save Note",
    command=save_note,
    width=20,
    bg="lightgreen"
).pack(pady=5)

Button(
    root,
    text="Open File",
    command=open_file,
    width=20,
    bg="lightblue"
).pack(pady=5)

Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    width=20,
    bg="yellow"
).pack(pady=5)

Button(
    root,
    text="Delete File",
    command=delete_file,
    width=20,
    bg="red"
).pack(pady=5)

Button(
    root,
    text="Exit",
    command=root.destroy,
    width=20,
    bg="lightcoral"
).pack(pady=5)

root.mainloop()