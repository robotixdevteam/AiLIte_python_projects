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

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return {'score': -1}
    elif check_winner(board, 'O'):
        return {'score': 1}
    elif not get_empty_positions(board):
        return {'score': 0}

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for (row, col) in get_empty_positions(board):
            board[row][col] = 'O'
            score = minimax(board, depth - 1, False)['score']
            board[row][col] = ' '
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return {'score': best_score, 'position': best_move}
    else:
        best_score = float('inf')
        best_move = None
        for (row, col) in get_empty_positions(board):
            board[row][col] = 'X'
            score = minimax(board, depth - 1, True)['score']
            board[row][col] = ' '
            if score < best_score:
                best_score = score
                best_move = (row, col)
        return {'score': best_score, 'position': best_move}

def computer_move(board):
    if len(get_empty_positions(board)) == 9:
        return random.choice(get_empty_positions(board))
    return minimax(board, 0, True)['position']

def cell_clicked(row, col):
    global current_player, board
    if board[row][col] == " " and current_player == 'X':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(board, current_player):
            result_label.config(text=f"Player {current_player} wins!")
            disable_buttons()
        elif not get_empty_positions(board):
            result_label.config(text="It's a tie!")
            disable_buttons()
        else:
            current_player = 'O'
            row, col = computer_move(board)
            board[row][col] = 'O'
            buttons[row][col].config(text='O')
            if check_winner(board, 'O'):
                result_label.config(text="Player O wins!")
                disable_buttons()
            elif not get_empty_positions(board):
                result_label.config(text="It's a tie!")
                disable_buttons()
            current_player = 'X'

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
    global current_player, board, result_label, root
    root = tk.Tk()
    root.title("Tic Tac Toe")

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    create_board_gui(root)
    result_label = tk.Label(root, text="Player X's turn", font=('Arial', 14))
    result_label.grid(row=3, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe_gui()

