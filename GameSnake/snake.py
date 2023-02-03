#Snakes Game using Python
#Use as SETAS para jogar, a BARRA DE ESPAÇO para pausar/reiniciar e a tecla Esc para sair


import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                   # Inicializando valores
score = 0

snake = [[4,10], [4,9], [4,8]]                                    # Coordenadas iniciais da cobra
food = [10,20]                                                     # Primeiras coordenadas alimentares

win.addch(food[0], food[1], '*')                                   # Imprime a comida

while key != 27:                                                   # Enquanto a tecla Esc não é pressionada
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                  # Imprimindo 'Pontuação' e
    win.addstr(0, 27, ' SNAKE ')                                    # strings 'SNAKE'
    win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)             # Aumenta a velocidade do Snake conforme seu comprimento aumenta
    
    prevKey = key                                                   # Tecla anterior pressionada
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):                                           # Se a BARRA DE ESPAÇO for pressionada, aguarde outro for another
        key = -1                                                   # um (Pausar/Reiniciar)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # Se uma tecla inválida for pressionada
        key = prevKey

    # Calcula as novas coordenadas da cabeça da cobra. NOTE: len(snake) aumenta.
    # Isso é resolvido mais tarde em [1].
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # Sair se a cobra cruzar os limites (Remova o comentário para habilitar)
    #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

    # Se a cobra atropelar a si mesma
    if snake[0] in snake[1:]: break

    
    if snake[0] == food:                                            #  Quando a cobra come a comida
        food = []
        score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 58)]                 # Calculando as coordenadas do próximo alimento
            if food in snake: food = []
        win.addch(food[0], food[1], '*')
    else:    
        last = snake.pop()                                          # [1] Se não comer a comida, o comprimento diminui
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')
    
curses.endwin()
print("\nScore - " + str(score))
print("http://bitemelater.in\n")