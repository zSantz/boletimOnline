print("=================CALCULADORA DE MÉDIAS=================")

professor_ou_aluno = input('Bem vindo! Você é um professor ou Aluno? ')

credencial_professor = '1'

aluno_existente = 'Pedro'

if professor_ou_aluno == 'Professor' or professor_ou_aluno == 'professor':
    validar_credencial = input('Digite sua credencial: ')
    if validar_credencial == credencial_professor:
        print('Escolha uma opção: ')
        condicao2 = input('Se você quiser adicionar notas para um aluno digite [1]\nSe você quiser consultar a nota do aluno digite [2]\nDigite [3] para sair: ')  
        if condicao2 == '1':
            aluno = input('Digite o nome do aluno: ')
            try:
                nota1 = float(input('Digite a primeira nota do aluno: '))
                nota2 = float(input('Digite a segunda nota do aluno: '))
                nota3 = float(input('Digite a terceira nota do aluno: '))
                nota4 = float(input('Digite a quarta nota do aluno: '))
            except:
                    print('Digite um número válido')
        elif condicao2 == '2' :
            consultar_nota = input('Você quer consultar a nota do aluno? ')
            if consultar_nota != 'sim' and consultar_nota != 'Sim':
                print('Infelizmente não podemos atender as suas necessidades. Bye Bye!')
            else:
                aluno = input('Digite o nome do aluno: ')
                
                if aluno == aluno_existente:
                    nota1 = 5
                    nota2 = 3
                    nota3 = 7
                    nota4 = 5
                    media = (nota1 + nota2 + nota3 + nota4)/4
                    print('=' * 10)
                    print(f'Boletim do aluno {aluno}')
                    print('=' * 10)
                    print(f'Primeira nota: {nota1}')
                    print(f'Segunda nota: {nota2}')
                    print(f'Terceira nota: {nota3}')
                    print(f'Quarta nota: {nota4}')
                    print(f'A média do aluno {aluno} foi de {media:.1f}')
        elif condicao2 == '3':
            print('Saindo do programa')    
        else:
            print('Opção invalida')
    else:
        print('Credencial Incorreta')
elif professor_ou_aluno == 'aluno' or professor_ou_aluno == 'Aluno':
    nome_aluno = input('Aluno digite seu nome: ')
    if nome_aluno == aluno_existente: 
        print('Escolha uma opção: ')
        condicao1 = input('Digite [1] para ver suas notas\nDigite [2] para calcular sua media e ver se foi aprovado \nDigite [3] para sair:')
        if condicao1 == '1':
            nota1 = 5
            nota2 = 3
            nota3 = 7
            nota4 = 5
            print('=' * 10)
            print(f'Boletim do aluno {nome_aluno}')
            print('=' * 10)
            print(f'Primeira nota: {nota1}')
            print(f'Segunda nota: {nota2}')
            print(f'Terceira nota: {nota3}')
            print(f'Quarta nota: {nota4}')
        elif condicao1 == '2':
            nota1 = 5
            nota2 = 3
            nota3 = 7
            nota4 = 5
            media = (nota1 + nota2 + nota3 + nota4)/4
            if media >= 20:
                print(f'{nome_aluno}, sua média foi {media} você esta aprovado')
            else:
                print(f'{nome_aluno}, sua média foi {media} você esta reprovado')
        elif condicao1 == '3':
            print('Saindo do programa')      
else:
    print('error 404\nVocê não é professor e nem aluno, não tem permissão para acessar')