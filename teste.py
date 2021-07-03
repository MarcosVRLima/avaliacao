from pessoa import Aluno
from prova import Caderno
import json

escola = {'nome': 'EEEP Rita Aguiar',
          'alunos': [{'matricula': '1234', 'nome': 'Pedro', 'proficiencia_mt': '127.3', 'proficiencia_pt': '153.3'},
                    {'matricula': '3216', 'nome': 'Rogerio', 'proficiencia_mt': '185.8', 'proficiencia_pt': '125.5' },
                    {'matricula': '3216', 'nome': 'Maria', 'proficiencia_mt': '110.7', 'proficiencia_pt': '181.3'},
                    {'matricula': '3216', 'nome': 'ana', 'proficiencia_mt': '152.9', 'proficiencia_pt': '120.9'}]}

cadernos_prova = [{'disciplina': 'matematica', 'codigo': '100', 'dificuldade': '100'},
                  {'disciplina': 'matematica', 'codigo': '101', 'dificuldade': '125'},
                  {'disciplina': 'matematica', 'codigo': '107', 'dificuldade': '150'},
                  {'disciplina': 'matematica', 'codigo': '106', 'dificuldade': '175'},
                  {'disciplina': 'matematica', 'codigo': '104', 'dificuldade': '200'},
                  {'disciplina': 'portugues', 'codigo': '105', 'dificuldade': '100'},
                  {'disciplina': 'portugues', 'codigo': '103', 'dificuldade': '125'},
                  {'disciplina': 'portugues', 'codigo': '102', 'dificuldade': '150'},
                  {'disciplina': 'portugues', 'codigo': '102', 'dificuldade': '175'},
                  {'disciplina': 'portugues', 'codigo': '108', 'dificuldade': '200'}]

#calcula a dificuldade mais próxima
def dificuldade_aproximada(cadernos, proficiencia, disciplina):
    i = 0   #indice a ser incrementado no for each
    n = 200 #numero máximo dado da dificuldade
    r = 0   #numero do indice a ser retornado no final da função
    for caderno in cadernos:
        if disciplina == caderno.disciplina and n > abs(float(proficiencia) - float(caderno.dificuldade)):  #compara a disciplina passada por parametro e depois verifica se o valor absoluto da subtração da proficiencia do aluno pela dificuldade da disciplina é menor que o dificuldade anterior
            n = abs(float(proficiencia) - float(caderno.dificuldade))   #n será o valor aproximado
            r = i #r será o numero do indice da dificuldade atual
        i += 1
    return r 

#Função para criar uma lista de objetos de aluno a partir do dicionario escola
def aluno():
    lista_aluno = []    #cria a lista a ser retornada
    for aluno in escola['alunos']:
        lista_aluno.append(Aluno(aluno["nome"], aluno["matricula"], aluno["proficiencia_mt"], aluno["proficiencia_pt"]))   #vai adicionando a lista cada instancia de aluno na lista
    return lista_aluno

#Função para criar uma lista de objetos de caderbi a partir do dicionario cadernos_prova
def caderno():
    lista_caderno = []
    for caderno in cadernos_prova:
        lista_caderno.append(Caderno(caderno["disciplina"], caderno["codigo"], caderno["dificuldade"])) #vai adicionando a lista cada instancia de caderno
    return lista_caderno

#Função que direciona o aluno aos cadernos de pt e mt a partir da proficiencia
def caderno_aluno():
    cadernos = caderno()    #variavel com a lista de objetos de cadernos
    alunos = aluno()    #variavel com a lista de objetos de alunos
    lista_dicionario = []   #cria uma lista de dicionario a ser retornada no final da função
    for a in alunos:    #for each para percorrer a lista alunos
        student = dict(nome = a.nome, matricula = a.matricula, proficiencia_mt = a.proficiencia_mt, proficiencia_lp = a.proficiencia_pt)    #dicionario de um aluno
        caderno_mt = dificuldade_aproximada(cadernos, a.proficiencia_mt, 'matematica') #variavel que tem o valor do indice do caderno de mt aproximado a proficiencia
        book_mt = dict(codigo = cadernos[caderno_mt].codigo, dificuldade = cadernos[caderno_mt].dificuldade)    #dicionario de um caderno de mt
        caderno_pt = dificuldade_aproximada(cadernos, a.proficiencia_pt, 'portugues')   #variavel que tem o valor do indice do caderno de pt aproximado a proficiencia
        book_pt = dict(codigo = cadernos[caderno_pt].codigo, dificuldade = cadernos[caderno_pt].dificuldade)    #dicionario de um caderno de pt
        lista_dicionario.append(dict(aluno = student, caderno_mt = book_mt, caderno_lp = book_pt))  #vai adicionando a lista os dicionarios
    return lista_dicionario

#Função que cria o arquivo de retorno em json
def cria_arquivo():
    with open('data.json', 'w') as f:    #guarda em f o caminho para escrever em um arquivo
        json.dump(caderno_aluno(), f, indent=3) #converte a lista de dicionario para json e escreve no arquivo de saída

cria_arquivo()