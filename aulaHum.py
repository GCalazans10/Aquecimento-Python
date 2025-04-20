 # Informações dos candidatos fictícios
candidato1_numero = 1
candidato1_partido = 'Partido A'
candidato1_nome = 'João'
candidato1_vice = 'Maria'
candidato2_numero = 2
candidato2_partido = 'Partido B'
candidato2_nome = 'Pedro'
candidato2_vice = 'Ana'
 # Ler o número do candidato digitado pelo usuário 
numero_candidato = int(input('Digite o número do candidato (1 ou 2)'))
 
 # Verificar as informações do candidato e exibir os dados
if numero_candidato == (candidato1_numero):
    print('Candidato:', candidato1_nome)
    print('Partido:', candidato1_partido)
    print('Vice-prefeito:', candidato1_vice)
elif numero_candidato == (candidato2_numero):
    print('Candidato:', candidato2_nome)
    print('Partido:', candidato2_partido)
    print('Vice-prefeito:', candidato2_vice)
else:
    print('Candidato não encontrado.')