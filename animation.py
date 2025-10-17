# Este módulo se encarga de importar sprites desde una carpeta específica,
# utilizando pygame para cargar imágenes como superficies. 
# En esta versión temporal, se ha desactivado la carga real de imágenes 
# para evitar errores por archivos faltantes. En su lugar, se generan 
# superficies vacías de color rojo como marcadores visuales. 
# Esto permite que el juego se ejecute sin interrupciones mientras se 
# completan o corrigen los recursos gráficos.

from os import walk
import pygame
from pathlib import Path

def _resolve_path(path):
    p = Path(path)

    if not p.exists():
        p = Path(__file__).resolve().parent / Path(path)
    return p

def import_sprite(path):
    surface_list = []
    p = _resolve_path(path)
    # walk accepts a path-like
    for _, __, img_file in walk(p):
        for image in img_file:
            full_path = str(p / image)
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)
    return surface_list