# no python temos basicamentre 3 tipos de controle de fluxo:
# if,elif, else
# for
# while

# if, elif, else
# o if, elif, else é uma estrutura que permite a checagem de condições específicas para que um código seja executado, por, exemplo:
melancia = False

if melancia is True:
    print('melancia')
else:
    print('hmmmm')

# o cógio acima pode ser lido como:
#            Se a melancia é Verdade, imprima no terminal a palavra melancia, mas em qualquer outra condição (melancia é Falso, melancia é uma lista, melancia não é nada ...) imprima a palavra hmmm
# o elif pode ser lido como um else if, ou seja, uma condição intermediária entre o if e o else
# nesse sentido, o elif só é avaliado após o if ou outro elif, funcionando como o select, switch em outras linguagens, veja um exemplo:

melancia = False

if melancia is True:
    print('melancia')
elif melancia is False:
    print('melão')
else:
    print('hmmmm')

# o cógio acima pode ser lido como:
#            Se a melancia é Verdade, imprima no terminal a palavra melancia, mas se não for, verifique se ela é Falsa, nesse caso imprima a palavra 'melão', e por fim, caso ela não seja verade nem mentira, imprima a palavra hmmmm.