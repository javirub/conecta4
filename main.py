#Juego conecta4 diseñado en python

from tkinter import Tk
from game_logic import GameLogic
from gui import GameGUI

if __name__ == "__main__":
    root = Tk()
    game_logic = GameLogic()
    game_gui = GameGUI(root, game_logic)
    root.mainloop()


