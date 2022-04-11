from sistema import Turma

turma = Turma()
comando = 0

while comando !=15:
  comando = int(input("\n1. Adicionar Aluno 2. Adicionar Nota 3. Remover Aluno\n4. Remover Nota 5. Editar Nome Aluno 6. Editar Nota Aluno\n7. Buscar Aluno Por Nome 8. Calcular Média da turma 9. Exibir Melhor Aluno\n10.Exibir Alunos Em Ordem Alfabética 11.Exibir Aluno Por Ordenados Por Nota 12.Exibir alunos aprovados por média (>=7)\n13.Exibir Alunos Na Final (>=5) 14.Exibir Alunos Reprovados (<5) 15.Encerra o Programa\n\n"))
  if comando ==1:
    nome = input('Digite o nome do Aluno a ser Adcionado:')
    resposta = turma.adciona_aluno(nome)
    if resposta == True:
      print("Aluno Adcionado com Sucesso!")
    elif resposta == False:
      print("O Aluno ja Existe!")
  elif comando ==2:
    nome = input('Digite o nome do Aluno:')
    nota = float(input("Digite a nota do aluno:"))
    resposta = turma.aluno_existe(nome)
    if resposta == True:
      resposta = turma.adcionar_notas(nome,nota)
      if resposta == True:
        print("Nota Adcionada com Sucesso!")
      elif resposta == False:
        print("O Aluno ja Possui 3 Notas!")
    elif resposta == False:
      print("O Aluno Nao Existe!")
  
  elif comando == 3:
    nome = input('Digite o nome do Aluno a ser Removido:') 
    resposta = turma.aluno_existe(nome)
    if resposta ==  True:
      turma.aluno_delete(nome)
      print("Aluno Removido com Sucesso!")
    else:
      print("O Aluno Nao Existe!")
  
  elif comando == 4:
    nome = input('Digite o nome do Aluno:')
    resposta = turma.aluno_existe(nome)
    if resposta == True:
      resposta = turma.chama_aluno(nome)
      print(resposta)
      nota = int(input("Qual Nota Deseja Remover, Digite 1 , 2 ou 3?"))
      resposta2 = turma.nota_delete(nome,nota)
      if resposta2 == True:
        print("Nota Removida com sucesso!")
      elif resposta2 == False:
        print("Nota não existe!")
    elif resposta == False:
      print("O Aluno nao existe!")
  
  elif comando ==5:
    nome = input('Digite o nome do Aluno a ser Editado:')
    resposta = turma.aluno_existe(nome)
    if resposta == True:
      novo_nome = input("Digite o Novo Nome:")
      resposta2 = turma.edita_aluno(nome,novo_nome)
      print("Aluno Editado")
    elif resposta == False:
      print("O ALUNO NAO EXISTE!")
  
  elif comando ==6:
    nome = input('Digite o nome do Aluno:')
    resposta = turma.aluno_existe(nome)
    if resposta == True:
      resposta = turma.chama_aluno(nome)
      print(resposta)
      nota = int(input("Qual Nota Deseja editar, Digite 1 , 2 ou 3?"))
      resposta2 = turma.nota_delete(nome,nota)
      nova_nota = float(input("DIGITE A NOVA NOTA DE %s:\n" %(nome)))
      resposta3 = turma.adcionar_notas(nome,nova_nota)
      if resposta3 == True:
        print("NOTA ALTERA COM SUCESSO!")
      elif resposta3 == False:
        print("ALGO DEU ERRADO")
    elif resposta == False:
      print("O ALUNO NAO EXISTE!")
  
  elif comando ==7:
    nome = input("digite o nome:")
    resposta = turma.nomes_parecidos(nome)
    print(resposta)
  
  elif comando == 8:
    melhor = 0
    resposta = turma.media_turma(melhor)
    if resposta == False:
      print('NAO HÁ NOMES')
    else:
      print('A MEDIA DA TURMA É %.2f' %(resposta))
  
  elif comando == 9:
    melhor = 1
    pessoa = turma.media_turma(melhor)
    print("O melhor Aluno é: ")
    print(*pessoa)
    print('PARABENS!')
   
  elif comando ==10:
    resposta = turma.notas_dos_alunos()
    if resposta == False:
      print("Algum aluno nao possui nota")
  
  elif comando ==11:
    resposta = turma.maiores_notas()
    print(resposta)
  
  elif comando == 12:
    resposta = turma.alunos_aprovados()
  elif comando ==13:
    resposta = turma.alunos_na_final() 
  elif comando == 14:
    resposta = turma.alunos_reprovados()

    
  
print("OBRIGADO POR USAR NOSSO SISTEMA!")
