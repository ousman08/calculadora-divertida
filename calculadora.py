# file: intuitive_fun_calculator.py

import tkinter as tk
from tkinter import messagebox

class FunCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Divertida 🧠✨")
        self.root.geometry("400x600")
        self.expression = ""
        self.history = []

        self.mode = "light"
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
        self.display.pack(fill="both", ipady=20, pady=10, padx=10)

        button_texts = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "🌓"]
        ]

        for row_values in button_texts:
            row = tk.Frame(self.root)
            row.pack(expand=True, fill="both", padx=10, pady=5)
            for val in row_values:
                b = tk.Button(row, text=val, font=("Arial", 20), relief=tk.RIDGE, bd=4)
                b.pack(side="left", expand=True, fill="both", padx=2, pady=2)
                b.bind("<Button-1>", self.on_button_click)

        self.history_box = tk.Listbox(self.root, height=5, font=("Courier", 12))
        self.history_box.pack(fill="both", padx=10, pady=10)

    def on_button_click(self, event):
        button = event.widget["text"]
        if button == "=":
            try:
                result = str(eval(self.expression))
                self.history.append(self.expression + " = " + result + " ✅")
                self.update_history()
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
                self.display.delete(0, tk.END)
                self.expression = ""
        elif button == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button == "⌫":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        elif button == "🌓":
            self.toggle_theme()
        else:
            self.expression += button
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def update_history(self):
        self.history_box.delete(0, tk.END)
        for h in self.history[-5:]:
            self.history_box.insert(tk.END, h)

    def toggle_theme(self):
        self.mode = "dark" if self.mode == "light" else "light"
        self.apply_theme()

    def apply_theme(self):
        if self.mode == "dark":
            bg = "#222"
            fg = "#fff"
        else:
            bg = "#fff"
            fg = "#000"
        self.root.configure(bg=bg)
        self.display.configure(bg=bg, fg=fg, insertbackground=fg)
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Button):
                        child.configure(bg=bg, fg=fg, activebackground="#444" if self.mode == "dark" else "#ddd")
            elif isinstance(widget, tk.Listbox):
                widget.configure(bg=bg, fg=fg)

def main():
    root = tk.Tk()
    app = FunCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
