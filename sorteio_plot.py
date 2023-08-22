import random
import matplotlib.pyplot as plt


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

N = 1e6
candidatos0 = candidatos.copy()
soma = [0 for i in range(len(candidatos))]
soma = dict(zip(candidatos0, soma))

for j in range(int(N)):
    ganhadores = sorteio(candidatos, nn=2)
    # print(f'O ganhador 1 é: {ganhadores[0]} !!!')
    # print(f'O ganhador 2 é: {ganhadores[1]} !!!')
    soma[ganhadores[0]] += 1
    soma[ganhadores[1]] += 1
    # candidatos = candidatos0.copy()
    if ganhadores[0] == ganhadores[1]:
        print('ERRO!')

print(soma)

fig, ax = plt.subplots()

ax.bar(range(len(candidatos0)), soma.values())
ax.set_ylabel('# vitórias')
ax.set_xticks(range(len(candidatos0)), list(soma.keys()))
ax.set_xticklabels(soma.keys(), rotation=45)
ax.grid()

fig.tight_layout()

plt.show()

