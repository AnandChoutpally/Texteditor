import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create a Text widget for editing
        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Add File menu to the menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)

    def new_file(self):
        self.text_widget.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_widget.delete("1.0", tk.END)
                    self.text_widget.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_widget.get("1.0", tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    content = self.text_widget.get("1.0", tk.END)
                    file.write(content)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def exit(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
