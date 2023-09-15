from dataclasses import dataclass


@dataclass
class Carta():
    valor: int
    naipe: str


carta = Carta(1, "paus")
carta.valor = 10
print(carta)