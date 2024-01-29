from tkinter import Canvas, Button, Label

class GameGUI:
    def __init__(self, root, game_logic):
        self.root = root
        self.game_logic = game_logic
        self.create_gui()

    def create_gui(self):
        self.root.title("Conecta 4")

        self.canvas = Canvas(self.root, width = 700, height = 600)
        self.canvas.grid(row = 0, column = 0, columnspan = 7)

        #Tamaño de cada celda en el tablero
        cell_size = 100

        #Añadimos los botones que los jugadores clicaran para añadir la ficha:
        for i in range(7):
            button = Button(self.root, text=f'Columna {i+1}', command = lambda i=i: self.clic_en_columna(i))
            button.grid(row = 1, column = i)

        #Dibujamos un borde alrededor de cada celda
        for row in range(6):
            for col in range(7):
                x0 = col * cell_size
                y0 = row * cell_size
                x1 = x0 + cell_size
                y1 = y0 + cell_size


                self.canvas.create_rectangle(x0, y0, x1, y1, outline = 'black')

        restart_button = Button(self.root, text = 'Reiniciar partida', command = self.game_logic.reiniciar_partida)
        restart_button.grid(row = 2, column = 0, columnspan = 3)

        reset_scores_button = Button(self.root, text = 'Resetear contador', command = self.game_logic.resetear_contador)
        reset_scores_button.grid(row = 2, column = 4, columnspan = 3)

        #Etiquetas para mostrar contadores de partidas
        self.label_rojas = Label(self.root, text =f'Rojas: {self.game_logic.num_partidas_rojas}')
        self.label_rojas.grid(row = 3, column = 0, columnspan = 3)

        self.label_amarillas = Label(self.root, text =f'Amarillas: {self.game_logic.num_partidas_amarillas}')
        self.label_amarillas.grid(row = 3, column = 4, columnspan = 3)

    def clic_en_columna(self, columna):
        fila = self.game_logic.colocar_ficha(columna) # Actualiza la matriz con las posiciones de las fichas

        if fila != -1:
            self.animar_ficha(columna, fila) # Llama a la animación por la que caen las fichas por el tablero


    def animar_ficha(self, columna, fila):
        #Obtiene coordenadas iniciales y finales de la ficha a colocar
        x0 = columna * 100 #100 = tamaño de celda en pixeles
        y0 = 0
        x1 = x0 + 100
        y1 = y0 + 100

        if self.game_logic.tablero[fila][columna] == 1:
            jugador_actual = 'red'
        else:
            jugador_actual = 'yellow'

        # Crea el óvalo y guarda su ID en la variable de instancia
        ficha_id = self.canvas.create_oval(x0, y0, x1, y1, fill=jugador_actual, tags='ficha')
        #Crea un bucle de animación con la función after
        def animacion(frame):
            nonlocal y0, y1
            y0 += 5 #Ajusta la posición de la ficha hacia abajo
            y1 += 5
            self.canvas.coords(ficha_id, x0, y0, x1, y1)  # Actualiza las coordenadas del óvalo
            if y1 < (fila + 1) * 100:
                self.root.after(10, animacion, frame + 1)

        animacion(0)
