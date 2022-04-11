class Turma:

  def __init__(self):
    self.alunos = {}
  
  def adciona_aluno(self, nome):
    if nome in self.alunos:
      resposta = False
    else:
      self.alunos[nome] =[]
      resposta = True
    return resposta
  
  def aluno_existe(self,nome):
    if nome in self.alunos:
      resposta = True
    else:
      resposta = False
    return resposta
  
  def adcionar_notas(self,nome,nota):
    if len(self.alunos[nome]) <3:
      self.alunos[nome].append(nota)
      resposta = True
    else:
      resposta =False
    return resposta
  
  def aluno_delete(self,nome):
    if nome in self.alunos:
      del self.alunos[nome]
  
  def chama_aluno(self, nome):
    if nome in self.alunos:
      resposta = self.alunos[nome]
      return resposta
  
  def nota_delete(self,nome, nota):
    if nome in self.alunos:
      if nota ==1:
        if len(self.alunos[nome]) >=1:
          self.alunos[nome].pop(0)
          resposta2 =True
        else:
          resposta2 = False
      elif nota ==2:
        if len(self.alunos[nome]) >=2:
          self.alunos[nome].pop(1)
          resposta2 =True
        else:
          resposta2 = False
      elif nota ==3:
        if len(self.alunos[nome]) ==3:
          self.alunos[nome].pop(2)
          resposta2 =True
        else:
          resposta2 = False
      return resposta2
  def edita_aluno(self,nome,novo_nome):
    if nome in self.alunos:
      self.alunos[novo_nome] = self.alunos[nome]
      del self.alunos[nome]

  
  def media_turma(self,melhor):
    melhor_aluno = 0
    n_turma = 0
    media_turma = 0
    n = 0
    media_aluno = 0
    pessoa = []
    soma_do_aluno = 0
    soma_aluno = 0
    n2 = 0
    if len(self.alunos) > 0:
      if melhor ==1:
        for nome,valor in self.alunos.items():
          rept = 0
          n_turma = len(valor)
          soma_do_aluno = 0
          n2 = 0
          while rept < (n_turma):
            soma_aluno = float(valor[rept])
            rept +=1
            soma_do_aluno += soma_aluno
            media_turma += (soma_aluno) 
            n += rept
            n2 += 1
          media_aluno = soma_do_aluno / n2
          if media_aluno > melhor_aluno:
            melhor_aluno = media_aluno
            pessoa.append(nome)
            pessoa.append('.   Notas  :')
            for nota in self.alunos[nome]:
              pessoa.append(nota)
            pessoa.append(".   Media  :")
            pessoa.append(melhor_aluno)
        return pessoa
      else:
         for nome,valor in self.alunos.items():
          rept = 0
          n_turma = len(valor)
          while rept < (n_turma):
            soma_aluno = float(valor[rept])
            rept +=1
            media_turma += (soma_aluno) 
            n += 1
      resposta = media_turma/n
      return resposta
    else:
      resposta = False
    return resposta

  def dicionario(self, codigo):
    if codigo ==1:
      lista = []
      for i in sorted(self.alunos.items()):
        lista.append(i)
      resposta = lista       
    else:
      resposta = self.alunos
    return resposta

  def notas_dos_alunos(self):
    lista = []
    lista2 = []
    for nome,nota in self.alunos.items(): 
      media_do_aluno = 0
      media_aluno = 0
      contador = 0
      while contador < len(self.alunos[nome]) :
        media_aluno += nota[contador]
        contador += 1 
      media_do_aluno = media_aluno / contador
      geral = nome,' notas: ',self.alunos[nome],'media:', media_do_aluno
      lista.append(geral) 

    for i in sorted(lista):
      lista2.append(i)
    for i,word in enumerate(lista2):
      print(i+1, word)

  def alunos_aprovados(self):
    aprovados = []
    lista2 = []
    for nome,nota in self.alunos.items():
      media_do_aluno = 0
      media_aluno = 0
      contador = 0
      while contador < len(self.alunos[nome]) :
        media_aluno += nota[contador]
        contador += 1 
      media_do_aluno = media_aluno / contador
      if media_do_aluno >= 7:
        geral = nome,' Notas: ', self.alunos[nome],'media: ', media_do_aluno
        aprovados.append(geral)
    for i in sorted(aprovados):
      lista2.append(i)
    print('OS ALUNOS APROVADOS SÃO:')
    for i,word in enumerate(lista2):
      print(i+1 , word)
    
  def alunos_reprovados(self):
    reprovados = []
    lista2 = []
    for nome,nota in self.alunos.items():
      media_do_aluno = 0
      media_aluno = 0
      contador = 0
      while contador < len(self.alunos[nome]) :
        media_aluno += nota[contador]
        contador += 1 
      media_do_aluno = media_aluno / contador
      if media_do_aluno < 5:
        geral = nome,' Notas: ', self.alunos[nome],'media: ', media_do_aluno
        reprovados.append(geral)
    for i in sorted(reprovados):
      lista2.append(i)
    print('OS ALUNOS REPROVADOS SÃO:')
    for i,word in enumerate(lista2):
      print(i+1 , word)
  
  def alunos_na_final(self):
    na_final = []
    lista2 = []
    for nome,nota in self.alunos.items():
      media_do_aluno = 0
      media_aluno = 0
      contador = 0
      while contador < len(self.alunos[nome]) :
        media_aluno += nota[contador]
        contador += 1 
      media_do_aluno = media_aluno / contador
      if 5 <= media_do_aluno <7 :
        geral = nome,' Notas: ', self.alunos[nome],'media: ', media_do_aluno
        na_final.append(geral)
    for i in sorted(na_final):
      lista2.append(i)
    print('OS ALUNOS NA FINAL SÃO:')
    for i,word in enumerate(lista2):
      print(i+1 , word)
  
  def maiores_notas(self):
    dic = {}
    for i in self.alunos:
      media = sum(self.alunos[i])/3
      dic[media] = i
    notas = list(dic.keys())
    notas.sort(reverse=True)
    pos = 0
    for i in notas:
      pos += 1
      resposta = (f'{pos}. {dic[i]}. Notas :  {self.alunos[dic[i]][0]:.1f} {self.alunos[dic[i]][1]:.1f} {self.alunos[dic[i]][2]:.1f} ')
      return resposta
  
  def nomes_parecidos(self,nome):
      pos = 0
      nomes = list(self.alunos.keys())
      nomes.sort()
      for i in nomes:
        if i.startswith(nome):
          pos +=1          
          media = sum(self.alunos[i])/3
          resposta = (f'{pos}. {i}. Notas : {self.alunos[i][0]:.1f} {self.alunos[i][1]:.1f} e {self.alunos[i][2]:.1f}. Media:{media:.1f} ')
          return resposta
