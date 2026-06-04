import tkinter as tk
import math
import random

class InterfazVisualWaterSort:
    def __init__(self, root):
        self.root = root
        self.root.title("NÚCLEO DE ENERGÍA - LAB EDICIÓN CRISTAL")
        self.root.geometry("1200x850")
        self.root.configure(bg="#05050b") 

        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # Parámetros de diseño visual de los tubos
        self.ancho_b = 60
        self.alto_b = 200 
        self.margen_x = 120 
        self.margen_y = 160  
        self.gap_x = 65      
        self.gap_y = 120     
        self.columnas = 7
        
        self.offsets = []
        self.animando_flote = False
        self.pouring_data = None  
        self.wave_angle = 0.0  
        self.seleccionado = None

        # Inicialización visual de partículas de fondo (Juego)
        self.particulas = []
        for _ in range(35):  
            self.particulas.append({
                "x": random.randint(0, 1200),
                "y": random.randint(0, 850),
                "speed": random.uniform(0.5, 1.5),
                "size": random.randint(2, 4),
                "color": random.choice(["#00FFFF", "#FF00FF", "#1E90FF", "#333366"])
            })

        # Inicialización visual de estrellas de fondo (Menú)
        self.estrellas_menu = []
        for _ in range(150): 
            self.estrellas_menu.append({
                "x": random.randint(0, 1200),
                "y": random.randint(0, 850),
                "speed_x": random.uniform(-0.5, 0.5), 
                "speed_y": random.uniform(1.0, 4.0),  
                "size": random.uniform(1, 3),
                "color": random.choice(["#FFFFFF", "#DDDDDD", "#AAAAFF", "#FFFFAA"])
            })

        self.mostrar_menu()

    def mostrar_menu(self):
        self.en_juego = False 
        self.en_menu = True
        self.modo_torneo = False
        
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.menu_canvas = tk.Canvas(self.root, bg="#05050b", highlightthickness=0)
        self.menu_canvas.pack(fill="both", expand=True)
        
        for e in self.estrellas_menu:
            e["id"] = self.menu_canvas.create_oval(
                e["x"], e["y"], e["x"] + e["size"], e["y"] + e["size"],
                fill=e["color"], outline=""
            )

        texto = "WATER SORT PUZZLE"
        fuente = ("Courier", 55, "bold")
        
        # Efecto visual de triple capa para el título
        self.txt_sombra = self.menu_canvas.create_text(600, 150, text=texto, font=fuente, fill="#555500")
        self.txt_base = self.menu_canvas.create_text(600, 148, text=texto, font=fuente, fill="#AAAA00")
        self.txt_brillo = self.menu_canvas.create_text(600, 146, text=texto, font=fuente, fill="#FFFF00") 

        self.txt_sub = self.menu_canvas.create_text(600, 230, text="SELECCIONA EL MODO DE JUEGO", font=("Courier", 16, "bold"), fill="#00FFFF")

        self.btn_frame = tk.Frame(self.menu_canvas, bg="#05050b")
        self.btn_frame.place(relx=0.5, rely=0.55, anchor="center")

        tk.Button(self.btn_frame, text="JUEGO LIBRE", font=("Courier", 16, "bold"), 
                  bg="#0d0d18", fg="#00FFFF", width=22, pady=8, relief="ridge", bd=4, cursor="hand2", command=self.mostrar_menu_libre).pack(pady=8)

        tk.Button(self.btn_frame, text="MODO TORNEO", font=("Courier", 16, "bold"), 
                  bg="#0d0d18", fg="#FF00FF", width=22, pady=8, relief="ridge", bd=4, cursor="hand2", command=self.mostrar_confirmacion_torneo).pack(pady=8)

        tk.Button(self.btn_frame, text="CONFIGURACIONES", font=("Courier", 16, "bold"), 
                  bg="#0d0d18", fg="#FFD700", width=22, pady=8, relief="ridge", bd=4, cursor="hand2", command=self.abrir_configuraciones).pack(pady=8)

        tk.Button(self.menu_canvas, text="SALIR DEL JUEGO", font=("Courier", 11, "bold"), 
                  bg="#330000", fg="#FF3333", width=18, pady=5, relief="ridge", bd=3, cursor="hand2", command=self.root.destroy).place(relx=1.0, rely=0.0, x=-20, y=20, anchor="ne")
        
        self.menu_canvas.bind("<Configure>", self.ajustar_elementos_menu)
        self.animar_estrellas_menu()

    def mostrar_menu_libre(self):
        for widget in self.btn_frame.winfo_children():
            widget.destroy()

        self.menu_canvas.itemconfig(self.txt_sub, text="ESCOGE LA DIFICULTAD A TU GUSTO", fill="#00FFFF")

        DIFICULTADES_MOCK = ["Fácil", "Básico", "Normal", "Difícil", "Pesadilla"]
        for dif in DIFICULTADES_MOCK:
            tk.Button(self.btn_frame, text=dif.upper(), font=("Courier", 14, "bold"), 
                      bg="#0d0d18", fg="#FF00FF", width=20, pady=6, relief="ridge", bd=3, cursor="hand2",
                      command=lambda d=dif: self.iniciar_juego_desde_menu(d, torneo=False)).pack(pady=6)

        tk.Button(self.btn_frame, text="◄ VOLVER", font=("Courier", 11, "bold"), 
                  bg="#151525", fg="#FFFFFF", width=12, pady=4, relief="flat", cursor="hand2", command=self.mostrar_menu).pack(pady=15)

    def mostrar_confirmacion_torneo(self):
        for widget in self.btn_frame.winfo_children():
            widget.destroy()

        self.menu_canvas.itemconfig(self.txt_sub, text="ADVERTENCIA DE SISTEMA: MODO TORNEO", fill="#FF3333")

        cuadro_conf = tk.LabelFrame(self.btn_frame, text=" ALERTA ", font=("Courier", 12, "bold"),
                                    bg="#0d0d18", fg="#FF3333", labelanchor="n", bd=3, relief="ridge", padx=20, pady=20)
        cuadro_conf.pack()

        texto_advertencia = ("El modo torneo es un modo donde la\n"
                             "dificultad va progresando a medida\n"
                             "que vas superando el nivel.\n\n"
                             "¿Estás seguro de escoger este modo?")
        
        tk.Label(cuadro_conf, text=texto_advertencia, font=("Courier", 12, "bold"), bg="#0d0d18", fg="#FFFFFF", justify="center").pack(pady=10)

        frame_sino = tk.Frame(cuadro_conf, bg="#0d0d18")
        frame_sino.pack(pady=10)

        tk.Button(frame_sino, text="SÍ", font=("Courier", 12, "bold"), bg="#00FF00", fg="black", width=8, pady=5, cursor="hand2",
                  command=lambda: self.iniciar_juego_desde_menu("Fácil", torneo=True)).pack(side="left", padx=15)

        tk.Button(frame_sino, text="NO", font=("Courier", 12, "bold"), bg="#FF3333", fg="white", width=8, pady=5, cursor="hand2",
                  command=self.mostrar_menu).pack(side="left", padx=15)

    def ajustar_elementos_menu(self, event):
        mitad_ancho = event.width / 2
        self.menu_canvas.coords(self.txt_sombra, mitad_ancho, 150)
        self.menu_canvas.coords(self.txt_base, mitad_ancho, 148)
        self.menu_canvas.coords(self.txt_brillo, mitad_ancho, 146)
        self.menu_canvas.coords(self.txt_sub, mitad_ancho, 230)

    def setup_ui(self):
        self.header = tk.Frame(self.root, bg="#0d0d18", pady=10)
        self.header.pack(fill="x", side="top")

        tk.Button(self.header, text="◄ MENÚ", command=lambda: self.confirmar_salida("menu"), 
                  bg="#00FFFF", fg="black", font=("Courier", 10, "bold"), width=10, cursor="hand2").pack(side="left", padx=10)

        tk.Button(self.header, text="⚙ SONIDO", command=self.abrir_configuraciones, 
                  bg="#FFD700", fg="black", font=("Courier", 10, "bold"), width=10, cursor="hand2").pack(side="left", padx=5)

        if self.modo_torneo:
            self.lbl_torneo_status = tk.Label(self.header, text=f"TORNEO: {self.dificultad_actual.upper()}", 
                                              bg="#FF00FF", fg="white", font=("Courier", 10, "bold"), width=20, relief="flat", padx=5)
            self.lbl_torneo_status.pack(side="left", padx=10)
        else:
            self.var_dificultad = tk.StringVar(self.root)
            self.var_dificultad.set(self.dificultad_actual)
            DIFICULTADES_MOCK = ["Fácil", "Básico", "Normal", "Difícil", "Pesadilla"]
            menu_dif = tk.OptionMenu(self.header, self.var_dificultad, *DIFICULTADES_MOCK, command=self.cambiar_dificultad)
            menu_dif.config(bg="#1E90FF", fg="black", font=("Courier", 10, "bold"), width=12, cursor="hand2")
            menu_dif.pack(side="left", padx=10)

        tk.Button(self.header, text="REINICIAR", command=self.iniciar_nivel, bg="#FF00FF", fg="white", font=("Courier", 10, "bold"), width=12, cursor="hand2").pack(side="right", padx=10)

        self.btn_undo = tk.Button(self.header, text="DESHACER (5)", command=self.deshacer_movimiento, bg="#FFD700", fg="black", font=("Courier", 10, "bold"), width=15, cursor="hand2")
        self.btn_undo.pack(side="right", padx=10)

        container = tk.Frame(self.root, bg="#05050b")
        container.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(container, bg="#05050b", highlightthickness=0)
        scrollbar_y = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar_y.set)
        
        scrollbar_y.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        if hasattr(event, 'delta') and event.delta:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def actualizar_scrollregion_estatico(self):
        filas = (len(self.tubos_data) + self.columnas - 1) // self.columnas
        max_x = self.margen_x + self.columnas * (self.ancho_b + self.gap_x) + 50
        max_y = self.margen_y + filas * (self.alto_b + self.gap_y) + 100
        self.canvas.config(scrollregion=(0, 0, max(max_x, 1200), max(max_y, 850)))

    def actualizar_boton_undo(self, intentos_deshacer):
        self.btn_undo.config(text=f"DESHACER ({intentos_deshacer})")
        if intentos_deshacer <= 0:
            self.btn_undo.config(state="disabled", bg="#333333", fg="#777777")
        else:
            self.btn_undo.config(state="normal", bg="#FFD700", fg="black")

    def dibujar_fondo_estatico(self):
        self.canvas.delete("fondo")
        
        # Dibujo de la cuadrícula de fondo futurista
        for i in range(0, 1500, 60): 
            self.canvas.create_line(i, 0, i, 1200, fill="#0f0f1a", tags=("fondo", "grid"))
        for i in range(0, 1200, 60):
            self.canvas.create_line(0, i, 1500, i, fill="#0f0f1a", tags=("fondo", "grid"))

        # Dibujo inicial de las partículas flotantes
        for p in self.particulas:
            p_id = self.canvas.create_oval(p["x"], p["y"], p["x"] + p["size"], p["y"] + p["size"], fill=p["color"], outline="", tags="fondo")
            p["id"] = p_id

    def dibujar_tubo_rotado(self, cx, cy, ancho, alto, contenido, angulo_deg, prog_vaciado=0.0, es_origen=False, prog_llenado=0.0, es_destino=False, color_flujo=None):
        rad = math.radians(angulo_deg)
        w, h, r = ancho, alto, ancho / 2
        capacidad_max = 4
        alto_liq = h / capacidad_max
        color_borde = "#FF00FF" if (angulo_deg != 0 or prog_llenado > 0) else "#00FFFF"
        ancho_borde = 4 if (angulo_deg != 0 or prog_llenado > 0) else 2

        def rotar_p(rx, ry): 
            return (cx + rx * math.cos(rad) - ry * math.sin(rad), cy + rx * math.sin(rad) + ry * math.cos(rad))

        amp_ola = 5.0 if (es_destino and prog_llenado > 0) else (3.0 if es_origen else 1.0)
        num_bloques = len(contenido)
        
        # Renderizado del líquido capa por capa con superficies deformadas por senos
        for i in range(num_bloques):
            color = contenido[i]
            scale = (1.0 - prog_vaciado) if (i == num_bloques - 1 and es_origen) else 1.0
            y_b_actual = h - (i * alto_liq)
            y_t_actual = y_b_actual - (alto_liq * scale)

            poly_pts = []
            for step in range(11):
                f_step = step / 10
                olita = math.sin(f_step * math.pi * 1.8 + self.wave_angle + (cx * 0.05)) * amp_ola
                poly_pts.extend(rotar_p(-w/2 + f_step * w, y_t_actual + olita))

            if i == 0:
                for s in range(9):
                    alpha = (s / 8) * math.pi
                    poly_pts.extend(rotar_p(r * math.cos(alpha), (h - r) + r * math.sin(alpha)))
            else:
                poly_pts.extend(rotar_p(w/2, y_b_actual))
                poly_pts.extend(rotar_p(-w/2, y_b_actual))
            self.canvas.create_polygon(poly_pts, fill=color, outline=color, tags="dinamico")

        # Dibujo de la rampa física de vertido (líquido saliendo del borde del tubo)
        if es_origen and num_bloques > 0:
            scale = (1.0 - prog_vaciado)
            y_t_top = (h - ((num_bloques - 1) * alto_liq)) - (alto_liq * scale)
            lip_rx = (w / 2 - 3) if angulo_deg > 0 else (-w / 2 + 3)
            rampa_pts = [*rotar_p(-w/2, y_t_top), *rotar_p(w/2, y_t_top), *rotar_p(lip_rx, 0), *rotar_p(lip_rx - (16 if angulo_deg > 0 else -16), 0)]
            self.canvas.create_polygon(rampa_pts, fill=contenido[-1], outline=contenido[-1], tags="dinamico")

        # Dibujo del llenado progresivo en el tubo de destino
        if es_destino and prog_llenado > 0 and color_flujo:
            y_b_actual = h - (len(contenido) * alto_liq)
            y_t_actual = y_b_actual - (alto_liq * prog_llenado)
            poly_pts = []
            for step in range(11):
                poly_pts.extend(rotar_p(-w/2 + (step/10) * w, y_t_actual + math.sin((step/10) * math.pi * 2.0 + self.wave_angle * 1.5) * amp_ola))
            if len(contenido) == 0:
                for s in range(9): poly_pts.extend(rotar_p(r * math.cos((s/8)*math.pi), (h-r) + r * math.sin((s/8)*math.pi)))
            else:
                poly_pts.extend(rotar_p(w/2, y_b_actual)); poly_pts.extend(rotar_p(-w/2, y_b_actual))
            self.canvas.create_polygon(poly_pts, fill=color_flujo, outline=color_flujo, tags="dinamico")

        # Dibujo del contorno de cristal translúcido del tubo de ensayo
        self.canvas.create_line(*rotar_p(-w/2, 0), *rotar_p(-w/2, h - r), fill="#141424", width=7, tags="dinamico")
        self.canvas.create_line(*rotar_p(w/2, 0), *rotar_p(w/2, h - r), fill="#141424", width=7, tags="dinamico")
        self.canvas.create_line(*rotar_p(-w/2, 0), *rotar_p(-w/2, h - r), fill=color_borde, width=ancho_borde, tags="dinamico")
        self.canvas.create_line(*rotar_p(w/2, 0), *rotar_p(w/2, h - r), fill=color_borde, width=ancho_borde, tags="dinamico")
        self.canvas.create_line(*rotar_p(-w/2 - 6, 0), *rotar_p(w/2 + 6, 0), fill=color_borde, width=ancho_borde + 2, tags="dinamico")
        self.canvas.create_line(*rotar_p(-w/2 - 4, -2), *rotar_p(w/2 + 4, -2), fill="#FFFFFF", width=1.5, tags="dinamico")
        
        curve_pts = []
        for s in range(13): curve_pts.extend(rotar_p(r * math.cos((s/12)*math.pi), (h - r) + r * math.sin((s/12)*math.pi)))
        self.canvas.create_line(curve_pts, fill=color_borde, width=ancho_borde, tags="dinamico")
        
        # Reflejos brillantes de luz en el cristal
        self.canvas.create_line(*rotar_p(-w/2 + 5, 8), *rotar_p(-w/2 + 5, h - r), fill="#FFFFFF", width=2, capstyle="round", tags="dinamico")
        self.canvas.create_line(*rotar_p(w/2 - 6, 14), *rotar_p(w/2 - 6, h - r - 25), fill="#FFFFFF", width=1, capstyle="round", tags="dinamico")

    def dibujar_escena(self):
        self.canvas.delete("dinamico") 

        # Dibujar todos los tubos quietos en su cuadrícula
        for i in range(len(self.tubos_data)):
            if self.pouring_data is not None and (self.pouring_data["origen"] == i or self.pouring_data["destino"] == i): continue
            if self.seleccionado == i: continue
                
            cx, cy = self.obtener_centro_boca(i)
            self.dibujar_tubo_rotated(cx, cy + self.offsets[i], self.ancho_b, self.alto_b, self.tubos_data[i], 0.0)
            self.vincular_clic_area(i, cx, cy)

        # Dibujar el tubo seleccionado flotando activamente
        if self.seleccionado is not None and (self.pouring_data is None or (self.pouring_data["origen"] != self.seleccionado and self.pouring_data["destino"] != self.seleccionado)):
            i = self.seleccionado
            cx, cy = self.obtener_centro_boca(i)
            self.dibujar_tubo_rotated(cx, cy + self.offsets[i], self.ancho_b, self.alto_b, self.tubos_data[i], 0.0)
            self.vincular_clic_area(i, cx, cy)

        # Animación del chorro continuo de agua suavizado (spline) entre origen y destino
        if self.pouring_data is not None:
            pd = self.pouring_data
            origen, destino = pd["origen"], pd["destino"]
            cx_d, cy_d = self.obtener_centro_boca(destino)
            capacidad_max = 4
            self.dibujar_tubo_rotated(cx_d, cy_d, self.ancho_b, self.alto_b, self.tubos_data[destino], 0.0, prog_llenado=pd["progreso_bloque"], es_destino=True, color_flujo=pd["color"])
            self.vincular_clic_area(destino, cx_d, cy_d)

            if pd["fase"] == "vaciando":
                rad = math.radians(pd["angulo_actual"])
                lip_offset = (self.ancho_b / 2 - 4) if pd["angulo_target"] > 0 else (-self.ancho_b / 2 + 4)
                x_chorro, y_chorro = pd["cx_actual"] + lip_offset * math.cos(rad), pd["cy_actual"] + lip_offset * math.sin(rad)
                y_superficie = cy_d + self.alto_b - ((len(self.tubos_data[destino]) + pd["progreso_bloque"]) * (self.alto_b / capacidad_max))

                puntos_chorro = []
                for s in range(11):
                    f_seg = s / 10
                    x_seg, y_seg = x_chorro + (cx_d - x_chorro) * f_seg, y_chorro + (y_superficie - y_chorro) * f_seg
                    if 0 < s < 10: x_seg += math.sin(f_seg * math.pi * 3.0 - self.wave_angle * 1.5) * 2.5
                    puntos_chorro.extend([x_seg, y_seg])
                self.canvas.create_line(puntos_chorro, fill=pd["color"], width=7, smooth=True, capstyle="round", tags="dinamico")
                self.canvas.create_line(puntos_chorro, fill="#FFFFFF", width=2.5, smooth=True, capstyle="round", tags="dinamico")

            self.dibujar_tubo_rotated(pd["cx_actual"], pd["cy_actual"], self.ancho_b, self.alto_b, self.tubos_data[origen], pd["angulo_actual"], prog_vaciado=pd["progreso_bloque"], es_origen=True)

    def update_waves(self):
        if not self.en_juego: return 

        self.wave_angle += 0.15
        for p in self.particulas:
            p["y"] -= p["speed"]
            if p["y"] < -10:
                p["y"] = 860
                p["x"] = random.randint(0, 1200)
            if "id" in p:
                self.canvas.coords(p["id"], p["x"], p["y"], p["x"] + p["size"], p["y"] + p["size"])
                
        # Variación de color pulsante de la rejilla tecno de fondo
        v_pulsante = int(14 + 8 * math.sin(self.wave_angle))
        color_grid = f"#{v_pulsante:02x}{v_pulsante:02x}{(v_pulsante+10):02x}"
        self.canvas.itemconfig("grid", fill=color_grid)
        
        self.dibujar_escena()
        self.root.after(25, self.update_waves) 

    def animar_estrellas_menu(self):
        if not self.en_menu: return 
        w = self.menu_canvas.winfo_width()
        h = self.menu_canvas.winfo_height()
        if w <= 1: w = 1200
        if h <= 1: h = 850
            
        for e in self.estrellas_menu:
            e["y"] += e["speed_y"]
            e["x"] += e["speed_x"]
            if e["y"] > h:
                e["y"] = -10
                e["x"] = random.randint(0, w)
            if e["x"] > w: e["x"] = 0
            elif e["x"] < 0: e["x"] = w
                
            if "id" in e:
                self.menu_canvas.coords(e["id"], e["x"], e["y"], e["x"] + e["size"], e["y"] + e["size"])
                
        self.root.after(30, self.animar_estrellas_menu)

    def ejecutar_animacion_flote(self):
        hubo_cambios = False
        velocidad = 6 

        for i in range(len(self.tubos_data)):
            target = -30 if self.seleccionado == i else 0
            actual = self.offsets[i]

            if actual != target:
                hubo_cambios = True
                if actual > target: self.offsets[i] = max(actual - velocidad, target)
                else: self.offsets[i] = min(actual + velocidad, target)

            if hubo_cambios: self.root.after(15, self.ejecutar_animacion_flote)
            else: self.animando_flote = False

    def vincular_clic_area(self, i, cx, cy):
        x1, y1 = cx - self.ancho_b / 2, cy
        x2, y2 = cx + self.ancho_b / 2, cy + self.alto_b
        tag = f"tubo_{i}"
        # Hitbox invisible para interactuar y procesar el clic sobre el tubo
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="", outline="", tags=("dinamico", tag))
        self.canvas.tag_bind(tag, "<Button-1>", lambda event, idx=i: self.procesar_clic(idx))

    def obtener_centro_boca(self, i):
        fila = i // self.columnas
        col = i % self.columnas
        cx = self.margen_x + col * (self.ancho_b + self.gap_x) + self.ancho_b / 2
        cy = self.margen_y + fila * (self.alto_b + self.gap_y)
        return cx, cy

    # --- MÉTODOS DE CONTROL DE INTERFAZ VACÍOS (CONECTORES DE LÓGICA DE JUEGO) ---
    def iniciar_juego_desde_menu(self, dificultad, torneo=False): pass
    def cambiar_dificultad(self, dif): pass
    def iniciar_nivel(self): pass
    def deshacer_movimiento(self): pass
    def abrir_configuraciones(self): pass
    def confirmar_salida(self, destino): pass
    def procesar_clic(self, idx): pass
    def cerrar_ventana(self): pass