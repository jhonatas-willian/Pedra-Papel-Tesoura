import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import random

# Cores da Interface Gráfica
branco = "#FFFFFF"    # white / branco
preto = "#333333"     # black / preto
laranja = "#fcc058"   # orange / laranja
amarelo = "#fff873"   # yellow / amarelo
verde = "#34eb3d"     # green / verde
vermelho = "#e85151"  # red / vermelho
fundo = "#3b3b3b"     # grey / cinza

# Configurando a Interface Gráfica
janela = Tk()
janela.title('')
janela.geometry('320x340')
janela.configure(background=fundo)


# Configurando a Interface Gráfica (Frame Cima)
frame_cima = Frame(janela, width=320, height=130, background=preto, relief='raised')
frame_cima.grid(row = 0, column= 0, sticky=NW)

frame_baixo = Frame(janela, width=320, height=210, background=branco, relief='flat')
frame_baixo.grid(row = 1, column= 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando o Player 1
player_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), background=preto, fg=branco)
player_1.place(x=15, y=100)

player_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), background=branco, fg=branco)
player_1_linha.place(x=0, y=0)

player_1_pontos = Label(frame_cima, text="  0", height=1, anchor='center', font=('Ivy 50 bold'), background=preto, fg=branco)
player_1_pontos.place(x=50, y=15)

# Configurando o Player 2 (Computador)
player_2 = Label(frame_cima, text="Computador", height=1, anchor='center', font=('Ivy 10 bold'), background=preto, fg=branco)
player_2.place(x=225, y=100)

player_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), background=branco, fg=branco)
player_2_linha.place(x=313.50, y=0)

player_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 50 bold'), background=preto, fg=branco)
player_2_pontos.place(x=190, y=15)

# Configurando o :
app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 50 bold'), background=preto, fg=branco)
app_.place(x=147, y=10)

# Configurando o Empate
app_empate = Label(frame_cima, text="", width=320, anchor='center', font=('Ivy 1 bold'), background=branco, fg=branco)
app_empate.place(x=0, y=123)

# Mostrar na parte superior oque você jogou (Pedra, Papel, Tesoura)
voce_joga = Label(frame_cima, text="", height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=preto, fg=preto)
voce_joga.place(x=15, y= 0)

# Mostrar na parte superior oque computador jogou (Pedra, Papel, Tesoura)
computador_joga = Label(frame_cima, text="", height=1, anchor=CENTER, font=('Ivy 10 bold'), bg=preto, fg=preto)
computador_joga.place(x=250, y= 0)

global voce
global computador
global rodadas
global pontos_voce
global pontos_computador

rodadas = 5
pontos_voce = 0
pontos_computador = 0

# Função Lógica do Jogo

def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_computador

    # Se algum jogador fizer 50 pontos o jogo finaliza!
    if rodadas > 0 and pontos_voce < 50 and pontos_computador < 50:
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        computador = random.choice(opcoes)
        voce = i
        
        # Mostrar na parte superior oque você jogou (Pedra, Papel, Tesoura)
        voce_joga['text'] = voce
        voce_joga['fg'] = branco
        
        # Mostrar na parte superior oque computador jogou (Pedra, Papel, Tesoura)
        computador_joga['text'] = computador
        computador_joga['fg'] = branco
        
        # Player 1 Vence
        if voce == 'Pedra' and computador == 'Tesoura':
            print('Você venceu!')
            player_1_linha['bg'] = verde
            player_2_linha['bg'] = branco
            app_empate['bg'] = branco
            pontos_voce += 10
            
        elif voce == 'Papel' and computador == 'Pedra':
            print('Você venceu!')
            player_1_linha['bg'] = verde
            player_2_linha['bg'] = branco
            app_empate['bg'] = branco
            pontos_voce += 10
        elif voce == 'Tesoura' and computador == 'Papel':
            print('Você venceu!')
            player_1_linha['bg'] = verde
            player_2_linha['bg'] = branco
            app_empate['bg'] = branco
            pontos_voce += 10
        else:
            fim_de_jogo()
        
        
        # Empate
        if voce == 'Pedra' and computador == 'Pedra':
            print('Empate!')
            player_1_linha['bg'] = branco
            player_2_linha['bg'] = branco
            app_empate['bg'] = amarelo
        elif voce == 'Papel' and computador == 'Papel':
            print('Empate!')
            player_1_linha['bg'] = branco
            player_2_linha['bg'] = branco
            app_empate['bg'] = amarelo
        elif voce == 'Tesoura' and computador == 'Tesoura':
            print('Empate!')
            player_1_linha['bg'] = branco
            player_2_linha['bg'] = branco
            app_empate['bg'] = amarelo
        else:
            fim_de_jogo()
        
        # Player 2 vence
        if computador == 'Pedra' and voce == 'Tesoura':
            print('Computador venceu!')
            player_1_linha['bg'] = branco
            player_2_linha['bg'] = vermelho
            app_empate['bg'] = branco
            pontos_computador += 10

        elif computador == 'Papel' and voce == 'Pedra':
            print('Computador venceu!')
            player_1_linha['bg'] = branco
            player_2_linha['bg'] = vermelho
            app_empate['bg'] = branco
            pontos_computador += 10

        elif computador == 'Tesoura' and voce == 'Papel':
            print('Computador venceu!')
            player_1_linha['bg'] = branco
            player_2_linha['bg'] = vermelho
            app_empate['bg'] = branco
            pontos_computador += 10

        # Atualizando a pontuação
        player_1_pontos['text'] = pontos_voce
        player_2_pontos['text'] = pontos_computador
                
        
    else:
        player_1_pontos['text'] = pontos_voce
        player_2_pontos['text'] = pontos_computador
        
        # Chamando a função terminar
        fim_de_jogo()
        

# Função Iniciar o Jogo
def iniciar_jogo():
    global Pedra
    global Pedra_1
    
    global Papel
    global Papel_1
    
    global Tesoura
    global Tesoura_1
    
    Botao.destroy()
    
    # Pedra
    Pedra_texto = Label(frame_baixo, text='Pedra', width=5, font=('Ivy 15 bold'), background= branco, fg=preto, relief=FLAT)
    Pedra_texto.place(x=25, y=20)
    Pedra = Image.open('images/Pedra-100.png')
    Pedra = Pedra.resize((80, 80), Image.LANCZOS)
    Pedra = ImageTk.PhotoImage(Pedra)
    Pedra_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=80, image=Pedra, compound=CENTER, background=branco, fg=branco, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
    Pedra_1.place(x=15, y= 60)

    # Papel
    Papel_texto = Label(frame_baixo, text='Papel', width=5, font=('Ivy 15 bold'), background= branco, fg=preto, relief=FLAT)
    Papel_texto.place(x=125, y=20)
    Papel = Image.open('images/Papel-100.png')
    Papel = Papel.resize((70, 70), Image.LANCZOS)
    Papel = ImageTk.PhotoImage(Papel)
    Papel_1 = Button(frame_baixo, command=lambda: jogar('Papel'), width=80, image=Papel, compound=CENTER, background=branco, fg=branco, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
    Papel_1.place(x=115, y= 60)

    # Tesoura
    Papel_texto = Label(frame_baixo, text='Tesoura', width=6, font=('Ivy 15 bold'), background= branco, fg=preto, relief=FLAT)
    Papel_texto.place(x=222, y=20)
    Tesoura = Image.open('images/Tesoura-100.png')
    Tesoura = Tesoura.resize((70, 70), Image.LANCZOS)
    Tesoura = ImageTk.PhotoImage(Tesoura)
    Tesoura_1 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=80, image=Tesoura, compound=CENTER, background=branco, fg=branco, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
    Tesoura_1.place(x=220, y= 60)


# Botão "Jogar" que irá iniciar o Jogo
Botao = Button(frame_baixo, command=iniciar_jogo, width=10, text='Jogar', background=fundo, fg=branco, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
Botao.place(x=120, y= 160)
    

# Função Terminar o Jogo
def fim_de_jogo():
    global rodadas
    global pontos_voce
    global pontos_computador
    
    # Definindo o vencedor
    jogador_voce = int(player_1_pontos['text'])
    jogador_computador = int(player_2_pontos['text'])
    
    if jogador_voce >= 50:
        vencedor_1 = Label(frame_baixo, text="Parabéns, você Ganhou!", height=1, anchor="center", font=('Ivy 10 bold'), bg=branco, fg=verde)
        vencedor_1.place(x=60, y=163)
    elif jogador_computador >= 50:
        vencedor_2 = Label(frame_baixo, text="Infelizmente você Perdeu!", height=1, anchor="center", font=('Ivy 10 bold'), bg=branco, fg=vermelho)
        vencedor_2.place(x=60, y=163)
    
    # Reiniciar o jogo
    def reset():
        player_1_pontos['text'] = '0'
        player_2_pontos['text'] = '0'
        
        iniciar_jogo()
    
    Restart = Button(frame_baixo, command=reset, width=7, text='Reiniciar', background=vermelho, fg= branco, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    Restart.place(x=240, y= 160)


janela.mainloop()
