import tkinter as tk

class VentanaSecundaria(tk.Toplevel):
    def __init__(self, master, eventos, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(width=400, height=300)
        self.title("Índice de eventos")
        for evento in eventos:
            evento_label = tk.Label(self, text=f"Nombre: {evento.nombre}, Artista: {evento.artista}")
            evento_label.pack()
