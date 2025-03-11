import pyautogui
import time

def capturar_posicao(delay=5):
    """Aguarda um tempo e captura a posição atual do cursor."""
    print(f"Aguardando {delay} segundos...")
    time.sleep(delay)
    posicao = pyautogui.position()
    print(f"Posição do mouse: {posicao}")
    return posicao

if __name__ == "__main__":
    capturar_posicao()
