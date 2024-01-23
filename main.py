import pyautogui
import time
import tkinter as tk
import threading

duration_padrao = 0

def mine_straight(duration=duration_padrao):

    time.sleep(2)
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.keyUp('w')
    pyautogui.mouseUp()
    print("Mining complete.")

def mine_thread():
    mining_duration = float(entry.get())  # Convertendo para número
    mine_thread = threading.Thread(target=mine_straight, args=(mining_duration,))
    mine_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minecraft Mining")

    label = tk.Label(root, text="Digite o tempo em segundos: ")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Minerar!", command=mine_thread)
    button.pack(pady=10)

    root.mainloop()
