import random
import streamlit as st


def sorteio(candidatoss, nn):
    candidatoss = candidatoss.copy()
    outt = []
    for ii in range(nn):
        auxx = random.choices(list(candidatoss.keys()), weights=list(candidatoss.values()))
        outt.append(auxx[0])
        del candidatoss[auxx[0]]
    return outt


# Valores iniciais ============================================================
nomes_temp = ["Andre", "Enzo", "Maju", "Henrique", "Pozza", "Shen",
              "Thiago", "Debora", "Mailson", "Astolfo", "Clemente"]
values_temp = [10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20]

# Streamlit ===================================================================
# Title and main text -------------------------------------
st.title('Sorteio')
st.write('Esse programa foi desenvolvido para sortear _n_ itens em uma lista'
         ' de _m_ itens, com probabilidades individuais diferentes e'
         ' selecionadas pelo usuário.')

# Inputs --------------------------------------------------
main_col1, main_col2 = st.columns([2, 1])
with main_col1:
    st.header('Entradas')
    m = st.number_input('m: quantidade de itens na lista', min_value=1, max_value=50,
                        value=len(nomes_temp), step=1)
    n = st.number_input('n: quantidade a ser sorteada', min_value=1, max_value=m,
                        value=2, step=1)

# Montando listas de input
nomes_final = []
values_final = []
for i in range(m):
    if i < len(nomes_temp):
        nomes_final.append(nomes_temp[i])
        values_final.append(values_temp[i])
    else:
        nomes_final.append(f'Participante {i+1}')
        values_final.append(0)

# Recebendo input para listas
with main_col1:
    st.subheader('Lista de participantes e chances individuais')
    col1, col2 = st.columns([3, 1])
    for i in range(m):
        with col1:
            nomes_final[i] = st.text_input(f'Participante {i+1}:', value=nomes_final[i])
        with col2:
            values_final[i] = st.number_input(f'Chance {i+1}:', min_value=0, value=values_final[i], key=i)

# Rodando sorteio -----------------------------------------
candidatos = dict(zip(nomes_final, values_final))
ganhadores = sorteio(candidatos, n)

# Saidas --------------------------------------------------
with main_col2:
    st.header('Resultado')
    revelar = st.button('Revelar resultado')
    if revelar:
        for i in range(n):
            st.write(f'Ganhador {i+1}: {ganhadores[i]}')
