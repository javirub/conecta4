from tkinter import Canvas, Button, Label, Toplevel
from game_logic import GameLogic
class GameGUI:
    def __init__(self, root):
        self.root = root
        self.game_logic = GameLogic(self)
        self.create_gui()
        self.create_popup()

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
        self.label_rojas = Label(self.root, textvariable = self.game_logic.num_partidas_rojas)
        self.label_rojas.grid(row = 3, column = 0, columnspan = 3)

        self.label_amarillas = Label(self.root, textvariable = self.game_logic.num_partidas_amarillas)
        self.label_amarillas.grid(row = 3, column = 4, columnspan = 3)

    def create_popup(self):
        self.popup_window = Toplevel(self.root)
        self.popup_window.title("¡Ganador!")
        self.popup_label = Label(self.popup_window, text="", font=("Arial", 16))
        self.popup_label.pack(pady=20)
        self.popup_button = Button(self.popup_window, text="Aceptar", command=self.ocultar_popup)
        self.popup_button.pack(pady=10)
        self.popup_window.protocol("WM_DELETE_WINDOW", self.ocultar_popup)
        self.popup_window.withdraw()  # Oculta la ventana emergente inicialmente

    def clic_en_columna(self, columna):
        fila = self.game_logic.colocar_ficha(columna) # Actualiza la matriz con las posiciones de las fichas

        if fila != -1:
            self.bloquear_tablero()
            self.animar_ficha(columna, fila, lambda: self.verificar_y_actualizar(columna,fila)) # Llama a la animación por la que caen las fichas por el tablero


    def animar_ficha(self, columna, fila, callback):
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
            else:
                self.desbloquear_tablero()
                callback() # Llama a verificar_ganador después de la animación


        animacion(0)

    def borrar_fichas(self):
        self.canvas.delete('ficha')

    def verificar_y_actualizar(self, columna, fila):
        if columna == -1 and fila == -1:
            self.label_rojas.config(text='')
            self.label_amarillas.config(text='')
        else:
            ganador = self.game_logic.verificar_ganador(columna, fila)
            if ganador:
                jugador_actual = 'Rojo' if ganador == 1 else 'Amarillo'
                self.mostrar_popup(f'Ganador: Jugador {jugador_actual.capitalize()}')
            else:
                self.label_rojas.config(text='')
                self.label_amarillas.config(text='')

    def mostrar_popup(self, mensaje):
        self.popup_label.config(text = mensaje)
        self.popup_window.geometry('300x150+500+200')
        self.popup_window.deiconify()

    def ocultar_popup(self):
        self.popup_window.withdraw()

    def bloquear_tablero(self):
        for i in range(7):
            button = self.root.grid_slaves(row=1, column=i)[0]
            button.config(state="disabled")

    def desbloquear_tablero(self):
        for i in range(7):
            button = self.root.grid_slaves(row=1, column=i)[0]
            button.config(state="normal")