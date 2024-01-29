from tkinter import Canvas, Button

class GameGUI:
    def __init__(self, root, game_logic):
        self.root = root
        self.game_logic = game_logic
        self.create_gui()

    def create_gui(self):
        self.root.title("Conecta 4")

        self.canvas = Canvas(self.root, width = 700, height = 600)
        self.canvas.grid(row = 0, column = 0, columnspan = 7)

        for i in range(7):
            button = Button(self.root, text=f'Columna {i+1}', command = lambda i=i: self.game_logic.clic_en_columna(i))
            button.grid(row = 1, column = i)

        restart_button = Button(self.root, text = 'Reiniciar partida', command = self.game_logic.reiniciar_partida)
        restart_button.grid(row = 2, column = 0, columnspan = 3)

        reset_scores_button = Button(self.root, text = 'Resetear contador', command = self.game_logic.resetear_contador)
        reset_scores_button.grid(row = 2, column = 4, columnspan = 3)

