import random
from random import choice

NomePro = input("Escreve aqui um nome próprio: ")
Verbo = input("Escreve aqui um verbo no presente: ")
Adjetivo = input("Escreve aqui um adjetivo: ")
Local = input("Escreve aqui um local: ")

Frases = {
    1: f"No calor do {Local}, sob os gritos ensurdecedores da torcida, {NomePro} sentiu o coração pulsar forte. Com uma postura {Adjetivo}, ele(a) começou a {Verbo} o jogo com uma intensidade que parecia contagiar todos ao redor. Cada passe, cada drible, era como uma dança precisa, e o gramado era seu palco. A cada avanço, o público se levantava, vibrando com a energia que só os verdadeiros craques conseguem transmitir. Era mais do que um jogo — era uma batalha, uma prova de coragem e paixão que ficaria marcada para sempre na história daquele estádio."
,
   2: f"No silêncio pesado do {Local}, onde apenas o som da respiração e o toque dos corpos se faziam ouvir, {NomePro} preparava-se para {Verbo}. Seus olhos, firmes e {Adjetivo}, avaliavam o adversário, enquanto o suor escorria pela testa. No tatami, cada movimento era calculado, uma combinação de força, técnica e estratégia. O público assistia em silêncio, consciente de que presenciava algo raro — uma luta de titãs, onde o respeito e a determinação se misturavam numa coreografia quase sagrada. Quando finalmente se lançou, a tensão explodiu, e o tempo parecia desacelerar. Era um momento único, que mostrava a verdadeira essência da arte marcial.",

3: f"A luz forte iluminava o {Local}, onde a multidão pulsava ao ritmo frenético da partida. {NomePro} segurava a bola com mãos firmes e um olhar {Adjetivo} que denunciava a concentração total. Cada passo era calculado, cada movimento feito com precisão. Naquele instante, nada mais existia além do som dos dribles e das batidas do coração acelerado. Ao se preparar para arremessar, o silêncio caiu por um instante, seguido por um estrondo quando a bola cortou o ar e acertou a cesta. Era a vitória a poucos segundos, e o rosto de {NomePro} expressava toda a emoção de quem luta por um sonho."
,
}

new_var = random.choice(list(Frases.values()))
print(new_var)
