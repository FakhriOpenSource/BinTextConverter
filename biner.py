import tkinter as tk
from tkinter import messagebox, ttk

# Function to convert text to binary
def text_to_binary():
    text = text_entry.get()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text first!")
        return
    
    binary_values = [format(ord(char), '08b') for char in text]
    binary_string = ' '.join(binary_values)
    
    # Display result in the text box
    binary_output_text.delete(1.0, tk.END)  # Clear previous result
    binary_output_text.insert(tk.END, binary_string)

# Function to convert binary to text
def binary_to_text():
    binary = binary_entry.get()
    if not binary:
        messagebox.showwarning("Input Error", "Please enter some binary first!")
        return
    
    try:
        binary_values = binary.split(' ')
        text_chars = [chr(int(bv, 2)) for bv in binary_values]
        text_string = ''.join(text_chars)
    except ValueError:
        messagebox.showerror("Format Error", "Binary values must be separated by spaces and consist of 8 digits.")
        return
    
    # Display result in the text box
    text_output_text.delete(1.0, tk.END)  # Clear previous result
    text_output_text.insert(tk.END, text_string)

# Function to copy binary result to clipboard
def copy_binary_to_clipboard():
    result = binary_output_text.get(1.0, tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Text to binary result copied to clipboard!")

# Function to copy text result to clipboard
def copy_text_to_clipboard():
    result = text_output_text.get(1.0, tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Binary to text result copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Text <-> Binary Converter")
root.geometry("700x500")
root.configure(bg="black")

# Button color and text color
button_color = "#4CAF50"
text_color = "white"

# Custom font
font_title = ("Helvetica", 16, "bold")
font_text = ("Helvetica", 12)

# Input text
tk.Label(root, text="Enter Text:", bg="black", fg="white", font=font_text).pack(pady=5)
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

# Button to convert text to binary
convert_text_button = tk.Button(root, text="Convert Text to Binary", command=text_to_binary, bg=button_color, fg=text_color)
convert_text_button.pack(pady=5)

# Output for text to binary conversion
tk.Label(root, text="Text to Binary Result:", bg="black", fg="white", font=font_text).pack(pady=5)
binary_output_text = tk.Text(root, height=5, wrap='none')  # Disable word wrap
binary_output_text.pack(fill=tk.X, padx=5)
binary_scrollbar_x = tk.Scrollbar(root, orient='horizontal', command=binary_output_text.xview)
binary_output_text.config(xscrollcommand=binary_scrollbar_x.set)
binary_scrollbar_x.pack(fill=tk.X)

# Button to copy binary result
copy_binary_button = tk.Button(root, text="Copy Binary Result", command=copy_binary_to_clipboard, bg="#2196F3", fg=text_color)
copy_binary_button.pack(pady=5)

# Input binary
tk.Label(root, text="Enter Binary (separated by spaces):", bg="black", fg="white", font=font_text).pack(pady=5)
binary_entry = tk.Entry(root, width=50)
binary_entry.pack(pady=5)

# Button to convert binary to text
convert_binary_button = tk.Button(root, text="Convert Binary to Text", command=binary_to_text, bg=button_color, fg=text_color)
convert_binary_button.pack(pady=5)

# Output for binary to text conversion
tk.Label(root, text="Binary to Text Result:", bg="black", fg="white", font=font_text).pack(pady=5)
text_output_text = tk.Text(root, height=5, wrap='none')  # Disable word wrap
text_output_text.pack(fill=tk.X, padx=5)
text_scrollbar_x = tk.Scrollbar(root, orient='horizontal', command=text_output_text.xview)
text_output_text.config(xscrollcommand=text_scrollbar_x.set)
text_scrollbar_x.pack(fill=tk.X)

# Button to copy text result
copy_text_button = tk.Button(root, text="Copy Text Result", command=copy_text_to_clipboard, bg="#2196F3", fg=text_color)
copy_text_button.pack(pady=5)

# Run the application
root.mainloop()
