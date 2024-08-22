import tkinter as tk
import random

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_positions(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def computer_move(board):
    empty_positions = get_empty_positions(board)
    return random.choice(empty_positions)

def cell_clicked(row, col):
    global current_player, board
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(board, current_player):
            result_label.config(text=f"Player {current_player} wins!")
            disable_buttons()
        elif all(all(cell != " " for cell in row) for row in board):
            result_label.config(text="It's a tie!")
            disable_buttons()
        else:
            switch_player()

def switch_player():
    global current_player
    current_player = 'X' if current_player == 'O' else 'O'
    if current_player == 'O':
        row, col = computer_move(board)
        cell_clicked(row, col)

def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state=tk.DISABLED)

def create_board_gui(root):
    global buttons
    buttons = []
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(root, text=" ", font=('Arial', 20), width=4, height=2,
                               command=lambda r=row, c=col: cell_clicked(r, c))
            button.grid(row=row, column=col, sticky="nsew")
            button_row.append(button)
        buttons.append(button_row)

def tic_tac_toe_gui():
    global current_player, board, result_label
    root = tk.Tk()
    root.title("Tic Tac Toe")

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'O'  # Computer starts first

    create_board_gui(root)
    result_label = tk.Label(root, text="Computer's turn", font=('Arial', 14))
    result_label.grid(row=3, columnspan=3)

    # Start with a computer move if the computer starts first
    if current_player == 'O':
        row, col = computer_move(board)
        cell_clicked(row, col)

    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe_gui()
