import webbrowser
import folium
import json
from models.models import Evento, Ubicacion

class ControladorPrincipal:
    def __init__(self, root):
        self.root = root
        self.ubicaciones = self.cargar_ubicaciones("/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/ubicaciones.json")
        self.eventos = self.cargar_eventos("/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/eventos.json")
        self.mostrar_ventana_principal()

    def cargar_ubicaciones(self, archivo_json):
        # Carga las ubicaciones desde el archivo JSON y crea objetos Ubicacion
        with open(archivo_json, "r") as file:
            ubicaciones_json = json.load(file)
            ubicaciones = [Ubicacion(**ubicacion) for ubicacion in ubicaciones_json]
        return ubicaciones

    def cargar_eventos(self, archivo_json):
        # Carga los eventos desde el archivo JSON y crea objetos Evento
        with open(archivo_json, "r") as file:
            eventos_json = json.load(file)
            eventos = [Evento(**evento) for evento in eventos_json]
        return eventos

    def mostrar_ventana_principal(self):
        from views.views import VentanaPrincipal
        self.ventana_principal = VentanaPrincipal(self.root, self.eventos, self.ubicaciones)

    def mostrar_mapa_ubicaciones(self, ubicaciones):
        mapa = folium.Map(location=[-24.7859, -65.41166], zoom_start=13)
        for ubicacion in ubicaciones:
            folium.Marker(location=ubicacion.coordenadas, popup=ubicacion.nombre).add_to(mapa)

        mapa.save("mapa_ubicaciones.html")
        webbrowser.open("mapa_ubicaciones.html")



