"""
SIMULADOR DE SISTEMA EMBARCADO DE MONITORAMENTO
Sistema de Monitoramento de Temperatura e Umidade - Versão Virtual

Este simulador replica o comportamento de um sistema embarcado Arduino
sem necessidade de componentes físicos.

Autor: Projeto Sistemas Embarcados
Data: Novembro 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from datetime import datetime
import math
import threading
import json
import os

class SensorSimulator:
    """Simula sensores DHT11 de temperatura e umidade"""
    
    def __init__(self):
        self.temperatura_base = 24.0  # Temperatura ambiente inicial
        self.umidade_base = 60.0      # Umidade ambiente inicial
        self.variacao_temp = 0.0      # Variação aplicada
        self.variacao_umid = 0.0
        
    def ler_temperatura(self):
        """Simula leitura de temperatura com ruído realista"""
        # Adiciona variação natural + ruído do sensor (±2°C como DHT11 real)
        ruido = random.uniform(-0.5, 0.5)
        temp = self.temperatura_base + self.variacao_temp + ruido
        return round(max(0, min(50, temp)), 1)  # Limita entre 0-50°C
    
    def ler_umidade(self):
        """Simula leitura de umidade com ruído realista"""
        ruido = random.uniform(-2, 2)
        umid = self.umidade_base + self.variacao_umid + ruido
        return round(max(20, min(90, umid)), 1)  # Limita entre 20-90%
    
    def aquecer(self, incremento=5.0):
        """Simula aquecimento do sensor"""
        self.variacao_temp += incremento
        self.variacao_umid -= incremento * 0.3  # Umidade tende a cair com calor
        
    def resfriar(self, decremento=5.0):
        """Simula resfriamento do sensor"""
        self.variacao_temp -= decremento
        self.variacao_umid += decremento * 0.2
        
    def resetar(self):
        """Volta às condições ambientais"""
        self.variacao_temp = 0
        self.variacao_umid = 0


class SistemaMonitoramento:
    """Sistema principal de monitoramento com interface gráfica"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🌡️ Simulador de Sistema Embarcado - Monitoramento de Temperatura")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        # Configurações
        self.sensor = SensorSimulator()
        self.temperatura_atual = 0.0
        self.umidade_atual = 0.0
        self.status_atual = "NORMAL"
        self.rodando = True
        self.modo_automatico = False
        
        # Histórico de dados
        self.historico_temp = []
        self.historico_umid = []
        self.historico_tempo = []
        self.max_pontos = 50
        
        # Limiares de temperatura
        self.TEMP_NORMAL = 25.0
        self.TEMP_ELEVADA = 30.0
        
        # Cores
        self.COR_FUNDO = "#1a1a2e"
        self.COR_PAINEL = "#16213e"
        self.COR_TEXTO = "#ffffff"
        self.COR_VERDE = "#00ff00"
        self.COR_AMARELO = "#ffff00"
        self.COR_VERMELHO = "#ff0000"
        
        # Configurar interface
        self.configurar_interface()
        
        # Iniciar thread de leitura
        self.thread_leitura = threading.Thread(target=self.loop_leitura, daemon=True)
        self.thread_leitura.start()
        
        # Protocolo de fechamento
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_aplicacao)
        
    def configurar_interface(self):
        """Configura toda a interface gráfica"""
        
        # Estilo
        self.root.configure(bg=self.COR_FUNDO)
        style = ttk.Style()
        style.theme_use('clam')
        
        # ===== HEADER =====
        header = tk.Frame(self.root, bg="#0f3460", height=80)
        header.pack(fill=tk.X, pady=(0, 10))
        
        titulo = tk.Label(
            header,
            text="🌡️ SISTEMA DE MONITORAMENTO EMBARCADO",
            font=("Arial", 24, "bold"),
            bg="#0f3460",
            fg=self.COR_TEXTO
        )
        titulo.pack(pady=15)
        
        subtitulo = tk.Label(
            header,
            text="Simulador Virtual - Projeto com Arduino",
            font=("Arial", 12),
            bg="#0f3460",
            fg="#aaaaaa"
        )
        subtitulo.pack()
        
        # ===== CONTAINER PRINCIPAL =====
        container = tk.Frame(self.root, bg=self.COR_FUNDO)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # ===== COLUNA ESQUERDA: Display LCD e LEDs =====
        coluna_esq = tk.Frame(container, bg=self.COR_FUNDO)
        coluna_esq.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        
        # Display LCD Virtual
        self.criar_display_lcd(coluna_esq)
        
        # Painel de LEDs
        self.criar_painel_leds(coluna_esq)
        
        # Status e Alertas
        self.criar_painel_status(coluna_esq)
        
        # ===== COLUNA CENTRO: Gráficos =====
        coluna_centro = tk.Frame(container, bg=self.COR_FUNDO)
        coluna_centro.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        self.criar_graficos(coluna_centro)
        
        # ===== COLUNA DIREITA: Controles e Logs =====
        coluna_dir = tk.Frame(container, bg=self.COR_FUNDO, width=300)
        coluna_dir.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        
        self.criar_controles(coluna_dir)
        self.criar_log(coluna_dir)
        
    def criar_display_lcd(self, parent):
        """Cria display LCD virtual 16x2"""
        frame = tk.LabelFrame(
            parent,
            text="📟 Display LCD 16x2",
            font=("Arial", 12, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.X, pady=(0, 20))
        
        # Simula display LCD com fundo verde característico
        lcd_frame = tk.Frame(frame, bg="#2d5016", relief=tk.SUNKEN, bd=3)
        lcd_frame.pack(pady=10)
        
        # Linha 1: Temperatura
        self.lcd_linha1 = tk.Label(
            lcd_frame,
            text="Temp: --.-°C",
            font=("Courier", 18, "bold"),
            bg="#3a6b1f",
            fg="#b4ff00",
            width=16,
            anchor='w',
            padx=10
        )
        self.lcd_linha1.pack()
        
        # Linha 2: Umidade
        self.lcd_linha2 = tk.Label(
            lcd_frame,
            text="Umid: --.-%",
            font=("Courier", 18, "bold"),
            bg="#3a6b1f",
            fg="#b4ff00",
            width=16,
            anchor='w',
            padx=10
        )
        self.lcd_linha2.pack()
        
    def criar_painel_leds(self, parent):
        """Cria painel de LEDs indicadores"""
        frame = tk.LabelFrame(
            parent,
            text="💡 Indicadores LED",
            font=("Arial", 12, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.X, pady=(0, 20))
        
        # Container dos LEDs
        leds_container = tk.Frame(frame, bg=self.COR_PAINEL)
        leds_container.pack(pady=10)
        
        # LED Verde
        led_verde_frame = tk.Frame(leds_container, bg=self.COR_PAINEL)
        led_verde_frame.pack(side=tk.LEFT, padx=20)
        
        self.led_verde = tk.Canvas(led_verde_frame, width=60, height=60, bg=self.COR_PAINEL, highlightthickness=0)
        self.led_verde.pack()
        self.led_verde.create_oval(5, 5, 55, 55, fill="#003300", outline="#006600", width=2)
        
        tk.Label(led_verde_frame, text="Normal", bg=self.COR_PAINEL, fg=self.COR_TEXTO, font=("Arial", 10)).pack()
        tk.Label(led_verde_frame, text="< 25°C", bg=self.COR_PAINEL, fg="#888888", font=("Arial", 8)).pack()
        
        # LED Amarelo
        led_amarelo_frame = tk.Frame(leds_container, bg=self.COR_PAINEL)
        led_amarelo_frame.pack(side=tk.LEFT, padx=20)
        
        self.led_amarelo = tk.Canvas(led_amarelo_frame, width=60, height=60, bg=self.COR_PAINEL, highlightthickness=0)
        self.led_amarelo.pack()
        self.led_amarelo.create_oval(5, 5, 55, 55, fill="#333300", outline="#666600", width=2)
        
        tk.Label(led_amarelo_frame, text="Elevada", bg=self.COR_PAINEL, fg=self.COR_TEXTO, font=("Arial", 10)).pack()
        tk.Label(led_amarelo_frame, text="25-30°C", bg=self.COR_PAINEL, fg="#888888", font=("Arial", 8)).pack()
        
        # LED Vermelho
        led_vermelho_frame = tk.Frame(leds_container, bg=self.COR_PAINEL)
        led_vermelho_frame.pack(side=tk.LEFT, padx=20)
        
        self.led_vermelho = tk.Canvas(led_vermelho_frame, width=60, height=60, bg=self.COR_PAINEL, highlightthickness=0)
        self.led_vermelho.pack()
        self.led_vermelho.create_oval(5, 5, 55, 55, fill="#330000", outline="#660000", width=2)
        
        tk.Label(led_vermelho_frame, text="Crítica", bg=self.COR_PAINEL, fg=self.COR_TEXTO, font=("Arial", 10)).pack()
        tk.Label(led_vermelho_frame, text="> 30°C", bg=self.COR_PAINEL, fg="#888888", font=("Arial", 8)).pack()
        
    def criar_painel_status(self, parent):
        """Cria painel de status e alarme"""
        frame = tk.LabelFrame(
            parent,
            text="🔔 Status do Sistema",
            font=("Arial", 12, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.X)
        
        self.label_status = tk.Label(
            frame,
            text="● NORMAL",
            font=("Arial", 24, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_VERDE
        )
        self.label_status.pack(pady=10)
        
        self.label_buzzer = tk.Label(
            frame,
            text="🔇 Alarme: Desligado",
            font=("Arial", 12),
            bg=self.COR_PAINEL,
            fg="#888888"
        )
        self.label_buzzer.pack(pady=5)
        
    def criar_graficos(self, parent):
        """Cria área de gráficos em tempo real"""
        frame = tk.LabelFrame(
            parent,
            text="📊 Gráficos em Tempo Real",
            font=("Arial", 12, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para gráfico de temperatura
        self.canvas_temp = tk.Canvas(frame, bg="#0a0e27", height=250, highlightthickness=1, highlightbackground="#444")
        self.canvas_temp.pack(fill=tk.BOTH, expand=True, pady=(10, 5))
        
        temp_label = tk.Label(frame, text="Temperatura (°C)", bg=self.COR_PAINEL, fg=self.COR_TEXTO, font=("Arial", 10))
        temp_label.pack()
        
        # Canvas para gráfico de umidade
        self.canvas_umid = tk.Canvas(frame, bg="#0a0e27", height=250, highlightthickness=1, highlightbackground="#444")
        self.canvas_umid.pack(fill=tk.BOTH, expand=True, pady=(15, 5))
        
        umid_label = tk.Label(frame, text="Umidade (%)", bg=self.COR_PAINEL, fg=self.COR_TEXTO, font=("Arial", 10))
        umid_label.pack()
        
    def criar_controles(self, parent):
        """Cria painel de controles"""
        frame = tk.LabelFrame(
            parent,
            text="🎮 Controles de Simulação",
            font=("Arial", 12, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            padx=15,
            pady=15
        )
        frame.pack(fill=tk.X, pady=(0, 20))
        
        # Botões de simulação
        btn_aquecer = tk.Button(
            frame,
            text="🔥 Aquecer (+5°C)",
            command=lambda: self.sensor.aquecer(5),
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        btn_aquecer.pack(fill=tk.X, pady=5)
        
        btn_resfriar = tk.Button(
            frame,
            text="❄️ Resfriar (-5°C)",
            command=lambda: self.sensor.resfriar(5),
            bg="#4ecdc4",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        btn_resfriar.pack(fill=tk.X, pady=5)
        
        btn_resetar = tk.Button(
            frame,
            text="🔄 Resetar",
            command=self.sensor.resetar,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.RAISED,
            bd=3,
            cursor="hand2"
        )
        btn_resetar.pack(fill=tk.X, pady=5)
        
        # Separador
        tk.Frame(frame, height=2, bg="#444").pack(fill=tk.X, pady=15)
        
        # Modo automático
        self.var_auto = tk.BooleanVar()
        check_auto = tk.Checkbutton(
            frame,
            text="🤖 Modo Automático",
            variable=self.var_auto,
            command=self.toggle_modo_automatico,
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            selectcolor="#333",
            font=("Arial", 10, "bold")
        )
        check_auto.pack(pady=5)
        
        tk.Label(
            frame,
            text="(Simula variações reais)",
            bg=self.COR_PAINEL,
            fg="#888",
            font=("Arial", 8)
        ).pack()
        
        # Estatísticas
        tk.Frame(frame, height=2, bg="#444").pack(fill=tk.X, pady=15)
        
        stats_frame = tk.Frame(frame, bg=self.COR_PAINEL)
        stats_frame.pack(fill=tk.X)
        
        tk.Label(stats_frame, text="📈 Estatísticas:", bg=self.COR_PAINEL, fg=self.COR_TEXTO, font=("Arial", 10, "bold")).pack(anchor='w')
        
        self.label_media_temp = tk.Label(stats_frame, text="Temp Média: --°C", bg=self.COR_PAINEL, fg="#aaa", font=("Arial", 9))
        self.label_media_temp.pack(anchor='w', pady=2)
        
        self.label_max_temp = tk.Label(stats_frame, text="Temp Máx: --°C", bg=self.COR_PAINEL, fg="#aaa", font=("Arial", 9))
        self.label_max_temp.pack(anchor='w', pady=2)
        
        self.label_min_temp = tk.Label(stats_frame, text="Temp Mín: --°C", bg=self.COR_PAINEL, fg="#aaa", font=("Arial", 9))
        self.label_min_temp.pack(anchor='w', pady=2)
        
    def criar_log(self, parent):
        """Cria painel de log de eventos"""
        frame = tk.LabelFrame(
            parent,
            text="📋 Log de Eventos",
            font=("Arial", 12, "bold"),
            bg=self.COR_PAINEL,
            fg=self.COR_TEXTO,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget para log
        self.log_text = tk.Text(
            frame,
            height=15,
            bg="#0a0e27",
            fg="#00ff00",
            font=("Consolas", 9),
            yscrollcommand=scrollbar.set,
            state=tk.DISABLED
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)
        
        # Adicionar mensagem inicial
        self.adicionar_log("Sistema iniciado com sucesso!")
        self.adicionar_log("Aguardando leituras dos sensores...")
        
    def adicionar_log(self, mensagem):
        """Adiciona mensagem ao log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_msg = f"[{timestamp}] {mensagem}\n"
        
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, log_msg)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        
    def atualizar_leds(self):
        """Atualiza estado dos LEDs baseado na temperatura"""
        # Desliga todos
        self.led_verde.delete("all")
        self.led_amarelo.delete("all")
        self.led_vermelho.delete("all")
        
        if self.temperatura_atual < self.TEMP_NORMAL:
            # LED Verde ACESO
            self.led_verde.create_oval(5, 5, 55, 55, fill=self.COR_VERDE, outline="#00ff00", width=3)
            self.led_verde.create_oval(15, 15, 45, 45, fill="#88ff88", outline="")
            self.led_amarelo.create_oval(5, 5, 55, 55, fill="#333300", outline="#666600", width=2)
            self.led_vermelho.create_oval(5, 5, 55, 55, fill="#330000", outline="#660000", width=2)
            
            self.label_status.config(text="● NORMAL", fg=self.COR_VERDE)
            self.label_buzzer.config(text="🔇 Alarme: Desligado", fg="#888888")
            self.status_atual = "NORMAL"
            
        elif self.TEMP_NORMAL <= self.temperatura_atual < self.TEMP_ELEVADA:
            # LED Amarelo ACESO
            self.led_verde.create_oval(5, 5, 55, 55, fill="#003300", outline="#006600", width=2)
            self.led_amarelo.create_oval(5, 5, 55, 55, fill=self.COR_AMARELO, outline="#ffff00", width=3)
            self.led_amarelo.create_oval(15, 15, 45, 45, fill="#ffff88", outline="")
            self.led_vermelho.create_oval(5, 5, 55, 55, fill="#330000", outline="#660000", width=2)
            
            self.label_status.config(text="⚠ ELEVADA", fg=self.COR_AMARELO)
            self.label_buzzer.config(text="🔇 Alarme: Desligado", fg="#888888")
            
            if self.status_atual != "ELEVADA":
                self.adicionar_log("⚠️ ALERTA: Temperatura elevada detectada!")
                self.status_atual = "ELEVADA"
            
        else:
            # LED Vermelho ACESO + Buzzer
            self.led_verde.create_oval(5, 5, 55, 55, fill="#003300", outline="#006600", width=2)
            self.led_amarelo.create_oval(5, 5, 55, 55, fill="#333300", outline="#666600", width=2)
            self.led_vermelho.create_oval(5, 5, 55, 55, fill=self.COR_VERMELHO, outline="#ff0000", width=3)
            self.led_vermelho.create_oval(15, 15, 45, 45, fill="#ff8888", outline="")
            
            self.label_status.config(text="🚨 CRÍTICA", fg=self.COR_VERMELHO)
            self.label_buzzer.config(text="🔊 Alarme: ATIVO!", fg=self.COR_VERMELHO)
            
            if self.status_atual != "CRITICA":
                self.adicionar_log("🚨 CRÍTICO: Temperatura muito alta! Alarme acionado!")
                self.status_atual = "CRITICA"
                # Pode adicionar beep do sistema aqui
                self.root.bell()
                
    def desenhar_grafico(self, canvas, dados, cor, min_val, max_val, label):
        """Desenha gráfico de linha no canvas"""
        canvas.delete("all")
        
        if len(dados) < 2:
            return
            
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        if width <= 1:
            width = 600
        if height <= 1:
            height = 200
            
        # Margens
        margin_left = 50
        margin_right = 20
        margin_top = 30
        margin_bottom = 30
        
        graph_width = width - margin_left - margin_right
        graph_height = height - margin_top - margin_bottom
        
        # Grid
        for i in range(5):
            y = margin_top + (graph_height / 4) * i
            canvas.create_line(margin_left, y, width - margin_right, y, fill="#1a3a52", width=1)
            valor = max_val - (max_val - min_val) / 4 * i
            canvas.create_text(margin_left - 10, y, text=f"{valor:.0f}", fill="#666", anchor='e', font=("Arial", 8))
        
        # Eixos
        canvas.create_line(margin_left, margin_top, margin_left, height - margin_bottom, fill="#444", width=2)
        canvas.create_line(margin_left, height - margin_bottom, width - margin_right, height - margin_bottom, fill="#444", width=2)
        
        # Desenhar linha do gráfico
        pontos = []
        for i, valor in enumerate(dados):
            x = margin_left + (graph_width / (len(dados) - 1)) * i
            y_norm = (valor - min_val) / (max_val - min_val) if max_val != min_val else 0.5
            y = height - margin_bottom - (y_norm * graph_height)
            pontos.extend([x, y])
        
        if len(pontos) >= 4:
            canvas.create_line(pontos, fill=cor, width=2, smooth=True)
            
            # Pontos
            for i in range(0, len(pontos), 2):
                x, y = pontos[i], pontos[i + 1]
                canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=cor, outline="white", width=1)
        
        # Valor atual
        if dados:
            ultimo_valor = dados[-1]
            canvas.create_text(
                width / 2,
                15,
                text=f"{label}: {ultimo_valor:.1f}",
                fill=cor,
                font=("Arial", 14, "bold")
            )
        
    def atualizar_graficos(self):
        """Atualiza os gráficos em tempo real"""
        # Gráfico de temperatura
        self.desenhar_grafico(
            self.canvas_temp,
            self.historico_temp,
            "#ff6b6b",
            0, 50,
            "Temperatura"
        )
        
        # Gráfico de umidade
        self.desenhar_grafico(
            self.canvas_umid,
            self.historico_umid,
            "#4ecdc4",
            20, 90,
            "Umidade"
        )
        
    def atualizar_estatisticas(self):
        """Atualiza estatísticas dos dados"""
        if self.historico_temp:
            media = sum(self.historico_temp) / len(self.historico_temp)
            maxima = max(self.historico_temp)
            minima = min(self.historico_temp)
            
            self.label_media_temp.config(text=f"Temp Média: {media:.1f}°C")
            self.label_max_temp.config(text=f"Temp Máx: {maxima:.1f}°C")
            self.label_min_temp.config(text=f"Temp Mín: {minima:.1f}°C")
    
    def toggle_modo_automatico(self):
        """Ativa/desativa modo automático de variação"""
        self.modo_automatico = self.var_auto.get()
        if self.modo_automatico:
            self.adicionar_log("🤖 Modo automático ATIVADO")
        else:
            self.adicionar_log("🤖 Modo automático DESATIVADO")
    
    def simular_variacao_automatica(self):
        """Simula variações automáticas de temperatura"""
        if self.modo_automatico:
            # Simula variação senoidal + ruído
            tempo = time.time()
            variacao = math.sin(tempo / 10) * 3
            self.sensor.variacao_temp = variacao
            
    def loop_leitura(self):
        """Loop principal de leitura dos sensores (roda em thread separada)"""
        contador = 0
        while self.rodando:
            try:
                # Lê sensores
                self.temperatura_atual = self.sensor.ler_temperatura()
                self.umidade_atual = self.sensor.ler_umidade()
                
                # Atualiza histórico
                self.historico_temp.append(self.temperatura_atual)
                self.historico_umid.append(self.umidade_atual)
                self.historico_tempo.append(contador)
                
                # Limita tamanho do histórico
                if len(self.historico_temp) > self.max_pontos:
                    self.historico_temp.pop(0)
                    self.historico_umid.pop(0)
                    self.historico_tempo.pop(0)
                
                # Atualiza interface (deve ser no thread principal)
                self.root.after(0, self.atualizar_interface)
                
                # Modo automático
                if self.modo_automatico:
                    self.simular_variacao_automatica()
                
                contador += 1
                time.sleep(2)  # Simula DHT11 (2 segundos entre leituras)
                
            except Exception as e:
                print(f"Erro no loop de leitura: {e}")
                time.sleep(1)
    
    def atualizar_interface(self):
        """Atualiza todos os elementos da interface"""
        # Atualiza LCD
        self.lcd_linha1.config(text=f"Temp: {self.temperatura_atual:4.1f}°C")
        self.lcd_linha2.config(text=f"Umid: {self.umidade_atual:4.1f}%")
        
        # Atualiza LEDs
        self.atualizar_leds()
        
        # Atualiza gráficos
        self.atualizar_graficos()
        
        # Atualiza estatísticas
        self.atualizar_estatisticas()
        
    def fechar_aplicacao(self):
        """Fecha a aplicação corretamente"""
        self.rodando = False
        self.adicionar_log("Sistema encerrado.")
        time.sleep(0.5)
        self.root.destroy()


def main():
    """Função principal"""
    root = tk.Tk()
    app = SistemaMonitoramento(root)
    root.mainloop()


if __name__ == "__main__":
    main()

