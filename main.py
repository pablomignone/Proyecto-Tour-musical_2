import sys
import os
import tkinter as tk
from controllers.controllers import ControladorPrincipal
# Agregar la ruta del directorio Tour musical al sys.path
ruta_proyecto = "/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical"
sys.path.append(ruta_proyecto)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorPrincipal(root)
    root.mainloop()
    ubicaciones_file = "/home/pablo/Documentos/Programación/1000 programadores salteños/Ejemplo app completa/tkinter-map-template/app/data/ubicaciones.json"
    archivo_json = os.path.abspath(ubicaciones_file)

    root = tk.Tk()
    root.title("Locales en la Zona")
    controlador = ControladorPrincipal(root, archivo_json)
    root.mainloop()
