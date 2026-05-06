import tkinter as tk
from tkinter import messagebox
import random

# --- CONFIGURACIÓN DE DIFICULTADES ---
DIFICULTADES = {
    "Fácil": {"colores": 3, "vacios": 2},
    "Básico": {"colores": 5, "vacios": 2},
    "Normal": {"colores": 7, "vacios": 2},
    "Difícil": {"colores": 9, "vacios": 3},
    "Extremo": {"colores": 11, "vacios": 3},
    "Pesadilla": {"colores": 13, "vacios": 4}
}

PALETA_NEON = [
    "#FF00FF", "#00FFFF", "#FFD700", "#FF4500", "#7FFF00", 
    "#1E90FF", "#FF1493", "#ADFF2F", "#FF8C00", "#00FA9A",
    "#8A2BE2", "#F0E68C", "#FF6347"
]

class WaterSortFuturista:
    def __init__(self, root):
        self.root = root
        self.root.title("NEON WATER SORT - TECH EDITION")
        self.root.geometry("1000x800")
        self.root.configure(bg="#0a0a12") # Fondo oscuro tecnológico
        
        self.dificultad_actual = "Normal"
        self.tubos_data = []
        self.seleccionado = None
        self.capacidad = 4
        
        self.setup_ui()
        self.iniciar_nivel()

    def setup_ui(self):
        # Frame superior para controles
        self.header = tk.Frame(self.root, bg="#161625", pady=10)
        self.header.pack(fill="x")
        
        tk.Label(self.header, text="DIFICULTAD:", fg="#00FFFF", bg="#161625", font=("Courier", 12, "bold")).pack(side="left", padx=10)
        
        self.var_dif = tk.StringVar(value=self.dificultad_actual)
        menu_dif = tk.OptionMenu(self.header, self.var_dif, *DIFICULTADES.keys(), command=self.cambiar_dificultad)
        menu_dif.config(bg="#00FFFF", fg="black", font=("Courier", 10, "bold"))
        menu_dif.pack(side="left", padx=10)

        btn_reset = tk.Button(self.header, text="REINICIAR NÚCLEO", command=self.iniciar_nivel, bg="#FF00FF", fg="white", font=("Courier", 10, "bold"))
        btn_reset.pack(side="right", padx=20)

        # Canvas Principal
        self.canvas = tk.Canvas(self.root, width=950, height=650, bg="#0a0a12", highlightthickness=0)
        self.canvas.pack(pady=20)

    def cambiar_dificultad(self, seleccion):
        self.dificultad_actual = seleccion
        self.iniciar_nivel()

    def iniciar_nivel(self):
        conf = DIFICULTADES[self.dificultad_actual]
        colores_usar = PALETA_NEON[:conf["colores"]]
        
        pool = colores_usar * self.capacidad
        random.shuffle(pool)
        
        self.tubos_data = [pool[i:i + self.capacidad] for i in range(0, len(pool), self.capacidad)]
        for _ in range(conf["vacios"]):
            self.tubos_data.append([])
            
        self.seleccionado = None
        self.dibujar_escena()

    def dibujar_botella(self, x, y, ancho, alto, contenido, seleccionado):
        # Coordenadas para una forma de botella tipo "matraz" tecnológico
        cuello_w = ancho * 0.4
        cuello_h = alto * 0.2
        
        # Puntos de la botella (Polígono)
        puntos = [
            x + (ancho-cuello_w)/2, y,             # Top izquierda cuello
            x + (ancho+cuello_w)/2, y,             # Top derecha cuello
            x + (ancho+cuello_w)/2, y + cuello_h,  # Base cuello derecha
            x + ancho, y + cuello_h + 20,          # Hombro derecho
            x + ancho, y + alto,                   # Fondo derecha
            x, y + alto,                           # Fondo izquierda
            x, y + cuello_h + 20,                  # Hombro izquierdo
            x + (ancho-cuello_w)/2, y + cuello_h   # Base cuello izquierda
        ]

        color_borde = "#FF00FF" if seleccionado else "#00FFFF"
        ancho_borde = 3 if seleccionado else 1

        # Dibujar líquido (simplificado por bloques dentro del cuerpo)
        cuerpo_alto = alto - cuello_h - 10
        for i, color in enumerate(contenido):
            bh = cuerpo_alto / self.capacidad
            by1 = (y + alto) - (i * bh)
            by0 = by1 - bh
            # Dibujamos el líquido como rectángulos que encajan en el cuerpo
            self.canvas.create_rectangle(x+4, by0, x+ancho-4, by1, fill=color, outline=color)

        # Dibujar el contorno de la botella
        self.canvas.create_polygon(puntos, outline=color_borde, fill="", width=ancho_borde)
        
        # Brillo tecnológico
        self.canvas.create_line(x+10, y+cuello_h+30, x+10, y+alto-20, fill="white", stipple="gray50")

    def dibujar_escena(self):
        self.canvas.delete("all")
        
        # Fondo decorativo (rejilla tecnológica)
        for i in range(0, 1000, 50):
            self.canvas.create_line(i, 0, i, 800, fill="#1a1a2e")
            self.canvas.create_line(0, i, 1000, i, fill="#1a1a2e")

        columnas = 7
        ancho_b, alto_b = 60, 180
        gap_x, gap_y = 60, 80

        for i, contenido in enumerate(self.tubos_data):
            fila = i // columnas
            col = i % columnas
            
            x = 80 + col * (ancho_b + gap_x)
            y = 50 + fila * (alto_b + gap_y)
            
            self.dibujar_botella(x, y, ancho_b, alto_b, contenido, self.seleccionado == i)
            
            # Área de clic invisible
            tag = f"b_{i}"
            self.canvas.create_rectangle(x, y, x+ancho_b, y+alto_b, fill="", outline="", tags=tag)
            self.canvas.tag_bind(tag, "<Button-1>", lambda e, idx=i: self.clic_botella(idx))

    def clic_botella(self, idx):
        if self.seleccionado is None:
            if self.tubos_data[idx]:
                self.seleccionado = idx
        else:
            if self.seleccionado != idx:
                self.transferir(self.seleccionado, idx)
            self.seleccionado = None
        
        self.dibujar_escena()
        self.check_win()

    def transferir(self, origen, destino):
        t_org = self.tubos_data[origen]
        t_des = self.tubos_data[destino]
        
        if not t_org or len(t_des) >= self.capacidad: return
        
        color = t_org[-1]
        if not t_des or t_des[-1] == color:
            while t_org and t_org[-1] == color and len(t_des) < self.capacidad:
                t_des.append(t_org.pop())

    def check_win(self):
        for t in self.tubos_data:
            if t and (len(t) != self.capacidad or len(set(t)) > 1):
                return
        messagebox.showinfo("SISTEMA RESTAURADO", "¡Has estabilizado todos los núcleos de energía!")
        self.iniciar_nivel()

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterSortFuturista(root)
    root.mainloop()