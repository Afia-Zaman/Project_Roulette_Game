import tkinter as tk
from tkinter import simpledialog, messagebox
import roulette

# Global variables
bet_number = None
bet_color = None


def place_bet():
    global bet_number, bet_color
    bet_number = simpledialog.askinteger("Place Your Bet", "Enter a number (1-36):")
    bet_color = simpledialog.askstring("Place Your Bet", "Choose a color ('red' or 'black'):").lower()
    # Handling the case where users might cancel the dialog
    if bet_number is None or bet_color not in ["red", "black"]:
        messagebox.showwarning("Invalid Input", "Please enter valid bets.")
        return False
    return True


def spin_and_check():
    if bet_number is None or bet_color is None:
        messagebox.showwarning("No Bet Placed", "Please place your bets first.")
        return

    winning_number = roulette.spin_wheel()
    winning_color = roulette.get_color(winning_number)
    result_text = f"The ball landed on {winning_number} ({winning_color}).\n"

    number_win = roulette.number_bet_won(bet_number, winning_number)
    color_win = roulette.color_bet_won(bet_color, winning_number)

    if number_win:
        result_text += "You won the number bet!\n"
    else:
        result_text += "You lost the number bet.\n"

    if color_win:
        result_text += "You won the color bet!"
    else:
        result_text += "You lost the color bet."

    messagebox.showinfo("Result", result_text)


def main():
    root = tk.Tk()
    root.title("Roulette Game")

    bet_button = tk.Button(root, text="Place Bet", command=lambda: place_bet() if not place_bet() else None)
    bet_button.pack()
    spin_button = tk.Button(root, text="Spin Wheel", command=spin_and_check)
    spin_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
