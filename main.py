import tkinter as tk

class SecureDataVaultApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Data Vault")
        self.root.configure(bg="black")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

        self.title_text = tk.StringVar(value="Secure Data Vault")
        self.title_label = tk.Label(root, textvariable=self.title_text, fg="white", bg="black", font=("Times New Roman", 40), anchor="center")
        self.title_label.pack()

        self.menu_frame = tk.Frame(self.root, bg="#1c1c1c", width=200)
        self.menu_frame.pack(side="left", anchor="n")

        self.content_frame = tk.Frame(self.root, bg="black")
        self.content_frame.pack(side="right", expand=True, fill="both")

        self.pages = {
            "Notes": Notes(self.content_frame),
            "Passwords": Passwords(self.content_frame),
            "Settings": Settings(self.content_frame),
            "Tutorial": Tutorial(self.content_frame),
            "Calendar": Calendar(self.content_frame),
            "Bin": Bin(self.content_frame),
            "Log": Log(self.content_frame),
            "Chat": Chat(self.content_frame)
        }

        buttons = list(self.pages.keys()) + ["Exit"]

        for name in buttons:
            action = lambda n=name: self.show_page(n)
            tk.Button(self.menu_frame, text=name, fg="white", bg="#2e2e2e",
                      font=("Arial", 12), relief="flat", command=action).pack(fill="x", pady=3)

    def show_page(self, name):
        for widget in self.content_frame.winfo_children():
            widget.pack_forget()
        if name == "Exit":
            self.root.quit()
        else:
            self.pages[name].frame.pack(fill="both", expand=True)

class Notes:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Passwords:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Settings:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Tutorial:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Calendar:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Bin:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Log:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

class Chat:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="black")

if __name__ == '__main__':
    window = tk.Tk()
    app = SecureDataVaultApp(window)
    window.mainloop()