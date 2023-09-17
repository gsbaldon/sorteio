import random


def sorteio(candidatoss, nn):
    candidatoss = candidatoss.copy()
    outt = []
    for ii in range(nn):
        auxx = random.choices(list(candidatoss.keys()), weights=list(candidatoss.values()))
        outt.append(auxx[0])
        del candidatoss[auxx[0]]
    return outt


candidatos = {
    "Andre": 10,
    "Enzo": 10,
    "Maju": 20,
    "Henrique": 20,
    "Pozza": 20,
    "Shen": 20,
    "Thiago": 20,
    "Debora": 20,
    "Mailson": 20,
    "Astolfo": 20,
    "Clemente": 20
              }

N_ganhadores = 2

ganhadores = sorteio(candidatos, nn=2)
print(60*'=', '\n')
print(f'O ganhador 1 é: {ganhadores[0]} !!!')
print('\n', 60*'=', '\n')
print(f'O ganhador 2 é: {ganhadores[1]} !!!')
print('\n', 60*'=')

print(candidatos.values())
