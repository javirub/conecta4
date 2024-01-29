class GameLogic:
    def __init__(self):
        self.tablero = [[0] * 7 for _ in range(6)]
        self.turno_rojas = True
        self.num_partidas_rojas = 0
        self.num_partidas_amarillas = 0



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

    def verificar_ganador(self):
        # Lógica para verificar si hay un ganador
        pass

    def reiniciar_partida(self):
        # Lógica para reiniciar la partida en marcha
        pass

    def resetear_contador(self):
        self.num_partidas_rojas = 0
        self.num_partidas_amarillas = 0

    def get_ultima_fila(self, columna):
        if self.tablero[fila][columna] == 0:
            return fila
        return None
