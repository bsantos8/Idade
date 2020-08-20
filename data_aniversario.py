#mostrar a data de anivers�rio em dias ,mes, e ano de uma pessoa

diaAtual= int(input('Dia atual:'))
mesAtual= int(input('Mes atual:'))
anoAtual= int(input('Ano atual:'))
print('')
diaNascimento= int(input('Dia nascimento:'))
mesNascimento= int(input('Mes nascimento:'))
anoNascimento= int(input('Ano nascimento:'))

anoA= anoAtual - anoNascimento
if anoA<0:
    anoA=anoA*(-1)
mesA= mesAtual - mesNascimento
if mesA<0: 
    mesA=mesA*(-1)
diaA= diaAtual - diaNascimento
if diaA<0:
    diaA= diaA*(-1)

#ano bisexto
bisexto = bool
if anoAtual % 400 == 0:
    bisexto= True
elif (anoAtual %4 == 0) & (anoAtual % 100 != 0) :
    bisexto= True
else:

    bisexto= False

#total de dias - ESTA DANDO DIFERENÇA ?
if bisexto == True:
    totaldias= anoA * 366
else: 
    totaldias= anoA * 365

print(f'Você tem: {anoA} anos, {mesA} meses e {diaA} dias\nDias Totais de vida {totaldias}')


