from tkinter import StringVar
class GameLogic:
    def __init__(self, gui):
        self.tablero = [[0] * 7 for _ in range(6)]
        self.turno_rojas = True
        self.num_partidas_rojas = StringVar()
        self.num_partidas_amarillas = StringVar()
        self.num_partidas_rojas.set("0")
        self.num_partidas_amarillas.set("0")
        self.gui = gui

    def colocar_ficha(self, columna):
        # Lógica para colocar una ficha en la columna seleccionada
        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] == 0:
                if self.turno_rojas:
                    self.tablero[fila][columna] = 1
                    self.turno_rojas = False # Cambia el turno para que el siguiente jugador sea el amarillo
                else:
                    self.tablero[fila][columna] = 2
                    self.turno_rojas = True # Cambia el turno para que el siguiente jugador sea el rojo
                return fila #Devuelve la fila en la que se colocó la ficha

        return -1 #Devuelve -1 si la columna está llena

    def verificar_ganador(self, columna, fila):
        jugador_actual = self.tablero[fila][columna]

        #Verificar horizontalmente, verticalmente, en diagonal hacia arriba y en diagonal hacia abajo
        if (
            self.verificar_linea(columna, fila, 1, 0, jugador_actual) or
            self.verificar_linea(columna, fila, 1, 0, jugador_actual) or
            self.verificar_linea(columna, fila, 1, 0, jugador_actual) or
            self.verificar_linea(columna, fila, 1, 0, jugador_actual)
        ):

            if jugador_actual ==1:
                self.num_partidas_rojas.set(str(int(self.num_partidas_rojas.get()) + 1))

            else:
                self.num_partidas_amarillas.set(str(int(self.num_partidas_amarillas.get()) + 1))
            self.gui.bloquear_tablero()
            return jugador_actual
        return False

    def verificar_linea(self, columna, fila, delta_x, delta_y, jugador_actual):
        # Verifica una linea en una dirección especifica determinadas por delta_x y delta_y
        count = 1 # Contador para contar las fichas del jugador en la linea

        for i in range(1, 4): # Verifica hasta 4 fichas
            x = columna + i * delta_x
            y = fila + i * delta_y

            if not (0 <= x < 7 and 0 <= y < 6 and self.tablero[y][x] == jugador_actual):
                break # En el momento en que un valor no corresponda con el jugador actual deja de contar en esa dirección
        else:
            return True # Se llega aquí si el bucle no se interrumpe

        #Ahora verificamos en la dirección opuesta
        for i in range(1,4):
            x = columna - i * delta_x
            y = fila - i * delta_y

            if not (0 <= x < 7 and 0 <= y < 6 and self.tablero[y][x] == jugador_actual):
                break
        else:
            return True

        return False

    def reiniciar_partida(self):
        self.tablero = [[0] * 7 for _ in range(6)]
        self.turno_rojas = True
        self.gui.verificar_y_actualizar(-1, -1)
        self.gui.borrar_fichas()  # Asegurarse de que el tablero gráfico se reinicie
        self.gui.desbloquear_tablero()
        self.gui.ocultar_popup()


    def resetear_contador(self):
        self.num_partidas_rojas.set('0')
        self.num_partidas_amarillas.set('0')

