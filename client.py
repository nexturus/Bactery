import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect(("localhost", 10000))

while True:
    if random.randint(1,2) == 1:
        sock.send(
            "Унылая пора! очей очарованье! Приятна мне твоя прощальная краса — Люблю я пышное природы увяданье,В багрец и в золото одетые леса.".encode())
    else:
        sock.send(
            "Мороз и солнце; день чудесный! Еще ты дремлешь, друг прелестный — Пора, красавица, проснись…".encode())