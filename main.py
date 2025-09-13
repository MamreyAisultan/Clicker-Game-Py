import tkinter as tk

def main():

    window = tk.Tk()
    window.geometry("600x400")
    window.title("Clicker Game Py")

    label_score = tk.Label(window, text="Score: 0")
    label_score.pack(pady = 20)
    
    button_click = tk.Button(window, text = "Нажми на меня.", font = ("Arial", 16), width = 15, height = 2)
    button_click.pack(pady = 20)

    window.mainloop()

if __name__ == "__main__":
    main()