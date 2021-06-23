### Selecionar o caderno de prova que mais se adequa ao nível de proficiência de um aluno

O problema consiste em encontrar, dentre um conjunto de cadernos de prova, o caderno que possui dificuldade mais próxima da proficiência de cada aluno.

### Requisitos
1) A função deverá receber uma lista de objetos do tipo "Aluno" e uma lista de objetos do tipo "Caderno" e retornar uma lista de dicionários contendo cada aluno e seus respectivos cadernos. Cada dicionário deve ter as seguintes chaves:
- "aluno": contendo o objeto "Aluno";
- "caderno_mt": contendo o objeto "Caderno" referente ao caderno prova de matemática selecionado para o aluno;
- "caderno_lp": contendo o objeto "Caderno" referente ao caderno prova de língua portuguesa selecionado para o aluno;

- Exemplo de retorno:

[
    {
        'aluno': instância de Aluno, 
        'caderno_mt': instância de Caderno, 
        'caderno_lp': instância de Caderno
    },
    {
        'aluno': instância de Aluno, 
        'caderno_mt': instância de Caderno, 
        'caderno_lp': instância de Caderno
    },
    {
        'aluno': instância de Aluno, 
        'caderno_mt': instância de Caderno, 
        'caderno_lp': instância de Caderno
    },
    ...
]


2) Criar um teste automático para testar a funcionalidade.

Obs.: o arquivo test.py contém as listas de alunos e de cadernos que devem ser utilizados.