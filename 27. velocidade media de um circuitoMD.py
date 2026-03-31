#Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

#declaração de variáveis
voltas: int = 0
extensao_m: float = 0
duracao_m: int = 0

def calc_vel(extensao_kilometros , duracao_horas):
    global vel_media
    vel_media = ((extensao_kilometros * voltas) / duracao_horas)
    print("A velocidade média é de " , vel_media , "km/h.")

def conversao(duracao_minutos , extensao_metros):
    duracao_h = duracao_minutos / 60
    extensao_km = extensao_metros / 1000

    calc_vel(extensao_km , duracao_h)

def main():
    global voltas
    global extensao_m
    global duracao_m

    voltas = int(input("Digite o número de voltas: "))
    extensao_m = float(input("Digite a extensão do circuito em metros: "))
    duracao_m = int(input("Digite o tempo em minutos: "))
    
    conversao(duracao_m , extensao_m)

if (__name__ == '__main__'):
    main()