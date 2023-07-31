import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
import os

class VentanaPrincipal(tk.Tk):
    def __init__(self, root, eventos, ubicaciones, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.geometry("800x600")
        self.title("Tour Musical")

        image_path = "assets/images/Salta_1.jpeg"  # Ruta relativa al archivo de imagen
        image_path = os.path.abspath(image_path)  # Convierte a ruta absoluta

        if os.path.exists(image_path):
            self.background_image = Image.open(image_path)
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.create_background_image()
        else:
            print("Error: No se encontró la imagen de fondo.")

        titulo_font = Font(family='Roboto', size=16, weight='bold')
        texto_font = Font(family='Open Sans', size=12)

        # Resto del código...
    
    def create_background_image(self):
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)



