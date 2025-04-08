import programa_exec
import keyboard as kb

def continua_sair(navegador, linkp):
    while True:
        if kb.is_pressed('('):
            programa_exec.programa_exec(navegador, linkp)
        if kb.is_pressed(')'):
            navegador.close()
            exit()
