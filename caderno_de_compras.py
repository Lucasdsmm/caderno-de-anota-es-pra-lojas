"""essas são as listas que armazenam as produtos que
estão faltando (eu coloquei em inglês pra eu ir treinando)"""
cd_dvd = []     # lista de (CD e DVD) * ela junta a lista de DVD e CD em uma só
other = []      # lista de produtos que não se encaixão nas outras listas
school_supplies = []     # lista de material escolar * lapis, borracha, caderno, etc...
adapter_cable = []      # lista de cabos e adaptadores * cabo de carregar celular, adaptador de p2 pra p10...
bijou = []      # lista de bijoterias * brincos, colar fêmenino, pulceira fêmenina, etc...
electronic = []     # lista de eletrônicos * caixa de som, conversor de TV, etc...
cover = []      # lista de capinhas pra celular * capinha pra moto g1, capinha pra samsung j2, etc...
dvd_tv_control = []  # lista de controles de TV e DVD * ela junta a lista de controle de TV, DVD e conversor em  uma só
toy = []     # lista de brinquedos pra criança
fashion_accessories = []    # lista de acessórios para o corpo masculino ou unisex
femalle_accessories = []    # lista para acessórios fêmeninos * maquiagem, unhas portiças, etc...
hookah = []     # lista para produtos relacionado a narguile * carvão, essência, alúminio, etc...
dvd_control = []    # lista de controles de DVD * uma lista individual só pra controle de DVD
tv_control = []     # lista de controles de TV * uma lista individual só pra controle de TV
converter_control = []    # lista de controles de conversor de TV * uma lista individual só pra controle de conversor
DVD = []    # lista de DVD * filmes, DVD de música
CD = []     # lista de CD * CD de músicas
ps2 = []    # lista de jogos pra playstation 2
xbox360 = []    # lista de jogos pra xbox 360
film = []   # lista de pelicula de celular * pelicula de moto g1, pelicula de samsung j2
separator = '\n'    # isso é uma gambiarra pros produtos aparecerem em forma de lista

while True:
    print('''
OPÇÕES: 

[ 1 ] película de vidro
[ 2 ] capinha
[ 3 ] cabo e adaptador
[ 4 ] eletrônicos
[ 5 ] bijuteria
[ 6 ] acessórios para o corpo
[ 7 ] acessorio feminino
[ 8 ] material escolar
[ 9 ] narguile
[ 10 ] controle de TV, DVD e conversor
[ 11 ] brinquedo
[ 12 ] CD e DVD
[ 13 ] jogo de PS2 e Xbox 360
[ 14 ] outro
[ sair ] sair do programa
''')                                        # opção de escolhas númeradas (cada número é uma escolha)
    print('')
    op = str(input('escolher opção principal: ').lower().strip())  # opção númerada
    print('')
    if op == '1':   # se o usuario digitar o número 1
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ pelicula ] confirme sua escolha: ').strip())   # confirmador de escolhas
            if a == '':     # se o usuario apertar ENTER
                def eliminator_film(film):
                    l_film = []
                    for i in film:
                        if i not in l_film:     # função que não deixa o produto duplicar
                            l_film.append(i)    # ele apaga produtos com o mesmo nome em uma lista especifica
                    l_film.sort()
                    return l_film
                print('')
                film.append(input('anotar pelicula: ').strip().lower().title())  # peliculas
                film = eliminator_film(film)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ] ')
            pass
    elif op == '2':    # se o usuario digitar o número 2
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ capinha ] confirme sua escolha: ').strip())   # confirmador de escolhas
            if a == '':     # se o usuario apertar ENTER
                def eliminator_cover(cover):
                    l_cover = []
                    for i in cover:
                        if i not in l_cover:     # função que não deixa o produto duplicar
                            l_cover.append(i)    # ele apaga produtos com o mesmo nome em uma lista especifica
                    l_cover.sort()
                    return l_cover
                print('')
                cover.append(input('anotar capinha: ').strip().lower().title())    # capinhas
                cover = eliminator_cover(cover)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '3':    # se o usuario digitar o número 3
        print('''
[ ENTER ] para prosseguir                               
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ cabo ou adaptador ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_adapter_cable(adapter_cable):
                    l_adapter_cable = []
                    for i in adapter_cable:
                        if i not in l_adapter_cable:     # função que não deixa o produto duplicar
                            l_adapter_cable.append(i)    # ele apaga produtos com o mesmo nome em uma lista especifica
                    l_adapter_cable.sort()
                    return l_adapter_cable
                print('')
                adapter_cable.append(input('anotar cabo ou adaptador: ').strip().lower())
                # cabo e adaptador
                adapter_cable = eliminator_adapter_cable(adapter_cable)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '4':    # se o usuario digitar o número 4
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ eletrônico ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_eletronic(eletronic):
                    l_eletronic = []
                    for i in eletronic:
                        if i not in l_eletronic:     # função que não deixa o produto duplicar
                            l_eletronic.append(i)    # ele apaga produtos com o mesmo nome em uma lista especifica
                    l_eletronic.sort()
                    return l_eletronic
                print('')
                electronic.append((input('anotar eletronico: ').strip().lower()))  # eletronicos
                electronic = eliminator_eletronic(electronic)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '5':    # se o usuario digitar o número 5
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ bijuteria ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_bijou(bijou):
                    l_bijou = []
                    for i in bijou:
                        if i not in l_bijou:     # função que não deixa o produto duplicar
                            l_bijou.append(i)    # ele apaga produtos com o mesmo nome em uma lista especifica
                    l_bijou.sort()
                    return l_bijou
                print('')
                bijou.append(input('anotar bijuteria: ').strip().lower())  # bijuterias
                bijou = eliminator_bijou(bijou)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '6':    # se o usuario digitar o número 6
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ acessório para o corpo ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_fashion_accessories(fashion_accessories):
                    l_fashion_accessories = []
                    for i in fashion_accessories:
                        if i not in l_fashion_accessories:     # função que não deixa o produto duplicar
                            l_fashion_accessories.append(i)    # ele apaga produtos com o mesmo nome em
                    l_fashion_accessories.sort()               # uma lista especifica
                    return l_fashion_accessories
                print('')
                fashion_accessories.append(input('anotar acessório para o corpo: ').strip().lower())
                # acessorios para o corpo
                fashion_accessories = eliminator_fashion_accessories(fashion_accessories)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '7':    # se o usuario digitar o número 7
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ acessório fêminino ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_femalle_accessories(femalle_accessories):
                    l_femalle_accessories = []
                    for i in femalle_accessories:
                        if i not in l_femalle_accessories:     # função que não deixa o produto duplicar
                            l_femalle_accessories.append(i)    # ele apaga produtos com o mesmo nome em
                    l_femalle_accessories.sort()               # uma lista especifica
                    return l_femalle_accessories
                print('')
                femalle_accessories.append(input('anotar acessório fêminino: ').strip().lower())
                # acessórios fêmeninos
                femalle_accessories = eliminator_femalle_accessories(femalle_accessories)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '8':    # se o usuario digitar o número 8
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ material escolar ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_school_supplies(school_supplies):
                    l_school_supplies = []
                    for i in school_supplies:
                        if i not in l_school_supplies:     # função que não deixa o produto duplicar
                            l_school_supplies.append(i)    # ele apaga produtos com o mesmo nome em
                    l_school_supplies.sort()               # uma lista especifica
                    return l_school_supplies
                print('')
                school_supplies.append(input('anotar material escolar: ').strip().lower())
                # material escolhar
                school_supplies = eliminator_school_supplies(school_supplies)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '9':    # se o usuario digitar o número 9
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ narguile ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_hookah(hookah):
                    l_hookah = []
                    for i in hookah:
                        if i not in l_hookah:     # função que não deixa o produto duplicar
                            l_hookah.append(i)    # ele apaga produtos com o mesmo nome em
                    l_hookah.sort()               # uma lista especifica
                    return l_hookah
                print('')
                hookah.append(input('anotar narguile: ').strip().lower())    # narguile
                hookah = eliminator_hookah(hookah)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '10':    # se o usuario digitar o número 10
        while True:
            print('''
Opções:

[ 1 ] TV
[ 2 ] DVD
[ 3 ] conversor
[ 0 ] para voltar às opções principais
''')    # aqui o usuario escolhe se vai anotar um controle de TV, DVD, conversor ou se vai voltar pro menu principal
            p = str(input('[ controle de TV, DVD ou conversor ] escolher opção: ').strip())  # escolher
            if p == '1':    # se o usuario digitou 1 ele vai para à anotação de controle de TV
                def eliminator_tv_control(tv_control):
                    l_tv_control = []
                    for i in tv_control:
                        if i not in l_tv_control:     # função que não deixa o produto duplicar
                            l_tv_control.append(i)    # ele apaga produtos com o mesmo nome em
                        l_tv_control.sort()           # uma lista especifica
                        return l_tv_control
                print('')
                tv_control.append(input('anotar controle de TV: ').strip().lower())  # controle de TV
                tv_control = eliminator_tv_control(tv_control)
                break
            elif p == '2':    # se o usuario digitou 2 ele vai para à anotação de controle de DVD
                def eliminator_dvd_control(dvd_control):
                    l_dvd_control = []
                    for i in dvd_control:
                        if i not in l_dvd_control:     # função que não deixa o produto duplicar
                            l_dvd_control.append(i)    # ele apaga produtos com o mesmo nome em
                    l_dvd_control.sort()               # uma lista especifica
                    return l_dvd_control
                print('')
                dvd_control.append(input('anotar controle de DVD: ').strip().lower())
                # controle de DVD
                dvd_control = eliminator_dvd_control(dvd_control)
                break
            elif p == '3':    # se o usuario digitou 3 ele vai para à anotação de controle de conversor
                def eliminator_converter_control(converter_control):
                    l_converter_control = []
                    for i in converter_control:
                        if i not in l_converter_control:     # função que não deixa o produto duplicar
                            l_converter_control.append(i)    # ele apaga produtos com o mesmo nome em
                    l_converter_control.sort()               # uma lista especifica
                    return l_converter_control
                print('')
                converter_control.append(input('anotar controle de conversor: ').strip().lower())
                # controle de conversor
                converter_control = eliminator_converter_control(converter_control)
                break
            elif p == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente das opções a cima, ele volta para as opções de confirmação
                print('DIGITE APENAS AS OPÇÕES ABAIXO.')
            pass
    elif op == '11':    # se o usuario digitar o número 11
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ brinquedo ] confirme sua escolha: ').strip())   # confirmador
            if a == '':     # se o usuario apertar ENTER
                def eliminator_toy(toy):
                    l_toy = []
                    for i in toy:
                        if i not in l_toy:     # função que não deixa o produto duplicar
                            l_toy.append(i)    # ele apaga produtos com o mesmo nome em
                    l_toy.sort()               # uma lista especifica
                    return l_toy
                print('')
                toy.append(input('anotar brinquedo: ').strip().lower())  # brinquedos
                toy = eliminator_toy(toy)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == '12':    # se o usuario digitar o número 12
        while True:
            print('''
Opções:

[ 1 ] CD
[ 2 ] DVD
[ 0 ] para voltar às opções principais
''')    # aqui o usuario escolhe se vai anotar um CD, DVD ou se vai voltar pro menu principal
            p1 = str(input('[ CD ou DVD ] escolher opção: ').strip())
            if p1 == '1':    # se o usuario digitou 1 ele vai para à anotação CD
                def eliminator_CD(CD):
                    l_CD = []
                    for i in CD:
                        if i not in l_CD:     # função que não deixa o produto duplicar
                            l_CD.append(i)    # ele apaga produtos com o mesmo nome em
                    l_CD.sort()               # uma lista especifica
                    return l_CD
                print('')
                CD.append(input('anotar CD: ').strip().lower())     # CD
                CD = eliminator_CD(CD)
                break
            elif p1 == '2':    # se o usuario digitou 2 ele vai para à anotação DVD
                def eliminator_DVD(DVD):
                    l_DVD = []
                    for i in DVD:
                        if i not in l_DVD:     # função que não deixa o produto duplicar
                            l_DVD.append(i)    # ele apaga produtos com o mesmo nome em
                    l_DVD.sort()               # uma lista especifica
                    return l_DVD
                print('')
                DVD.append(input('anotar DVD: ').strip().lower())     # DVD
                DVD = eliminator_DVD(DVD)
                break
            elif p1 == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente das opções a cima, ele volta para as opções de confirmação
                print('DIGITE APENAS AS OPÇÕES ABAIXO.')
            pass
    elif op == '13':    # se o usuario digitar o número 13
        while True:
            print('''
Opçoes:

[ 1 ] PS2
[ 2 ] XBOX 360
[ 0 ] para voltar às opções principais
''')    # aqui o usuario escolhe se vai anotar um jogo de PS2, jogo de xbox 360 ou se vai voltar pro menu principal
            p2 = str(input('[ jogo de PS2 ou XBOX 360 ] escolher opção: ').strip())   # confirmador
            if p2 == '1':    # se o usuario digitou 1 ele vai para à anotação de jogos de ps2
                def eliminator_ps2(ps2):
                    l_ps2 = []
                    for i in ps2:
                        if i not in l_ps2:     # função que não deixa o produto duplicar
                            l_ps2.append(i)    # ele apaga produtos com o mesmo nome em
                    l_ps2.sort()               # uma lista especifica
                    return l_ps2
                print('')
                ps2.append(input('anotar jogo de PS2: ').strip().lower())     # jogo de ps2
                ps2 = eliminator_ps2(ps2)
                break
            elif p2 == '2':    # se o usuario digitou 2 ele vai para à anotação de jogos de xbox 360
                def eliminator_xbox360(xbox360):
                    l_xbox360 = []
                    for i in xbox360:
                        if i not in l_xbox360:     # função que não deixa o produto duplicar
                            l_xbox360.append(i)    # ele apaga produtos com o mesmo nome em
                    l_xbox360.sort()               # uma lista especifica
                    return l_xbox360
                print('')
                xbox360.append(input('anotar jogo de XBOX 360: ').strip().lower())  # jogo de xbox 360
                xbox360 = eliminator_xbox360(xbox360)
                break
            elif p2 == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente das opções a cima, ele volta para as opções de confirmação
                print('DIGITE APENAS AS OPÇÕES ABAIXO')
            pass
    elif op == '14':    # se o usuario digitar o número 14
        print('''
[ ENTER ] para prosseguir
[ 0 ] para voltar
''')     # uma confirmação de escolha (tem vezes que o usuario escolhe a opção errada e não consegue mais voutar)
        while True:
            a = str(input('[ objeto não listado ] confirme sua escolha: ').strip())   # confirmador
            print('')
            if a == '':
                def eliminator_other(other):
                    l_other = []
                    for i in other:
                        if i not in l_other:     # função que não deixa o produto duplicar
                            l_other.append(i)    # ele apaga produtos com o mesmo nome em
                    l_other.sort()               # uma lista especifica
                    return l_other
                other.append(input('anotar outro objeto não listado: ').strip().lower())
                other = eliminator_other(other)
                break
            elif a == '0':     # se o usuario digitar 0 ele volta pro começo das anotações
                break
            else:   # se o usuario digitar algo diferente de ENTER ou 0, ele volta pras opções de confirmação
                print('digite apenas [ ENTER ] ou [ 0 ]')
            pass
    elif op == 'sair':    # se o usuario digitar sair ele sai do programa
        print('')
        if len(film) > 0:
            # se o número de objetos na lista de peliculas for maior do que 0 ele vai executar essa condição
            print('PELÍCULAS')
            film.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(film))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(cover) > 0:
            # se o número de objetos na lista de capinhas for maior do que 0 ele vai executar essa condição
            print('CAPAS')
            cover.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(cover))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(adapter_cable) > 0:
            # se o número de objetos na lista de cabo e adaptador for maior do que 0 ele vai executar essa condição
            print('CABOS E ADAPTADORES')
            adapter_cable.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(adapter_cable))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(electronic) > 0:
            # se o número de objetos na lista de peliculas for maior do que 0 ele vai executar essa condição
            print('ELETRÔNICOS')
            electronic.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(electronic))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(bijou) > 0:
            # se o número de objetos na lista de bijuteria for maior do que 0 ele vai executar essa condição
            print('BIJUTERIAS')
            bijou.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(bijou))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(fashion_accessories) > 0:
            # se o número de objetos na lista de acessorios para o corpo for
            # maior do que 0 ele vai executar essa condição
            print('ACESSÓRIOS PARA O CORPO')
            fashion_accessories.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(fashion_accessories))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(femalle_accessories) > 0:
            # se o número de objetos na lista de acessórios fêmeninos for maior do que 0 ele vai executar essa condição
            print('ACESSÓRIOS FEMENINOS')
            femalle_accessories.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(femalle_accessories))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(school_supplies) > 0:
            # se o número de objetos na lista de material escolar for maior do que 0 ele vai executar essa condição
            print('MATERIAL ESCOLAR')
            school_supplies.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(school_supplies))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(hookah) > 0:
            # se o número de objetos na lista de narguile for maior do que 0 ele vai executar essa condição
            print('NARGUILE')
            hookah.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(hookah))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(tv_control) > 0:
            # se o número de objetos na lista de controle de TV for maior do que 0 ele vai executar essa condição
            print('CONTROLES DE TV')
            tv_control.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(tv_control))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(dvd_control) > 0:
            # se o número de objetos na lista de controle de DVD for maior do que 0 ele vai executar essa condição
            print('CONTROLES DE DVD')
            dvd_control.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(dvd_control))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(converter_control) > 0:
            # se o número de objetos na lista de controle de conversor for maior do que 0 ele vai executar essa condição
            print('CONTROLES DE CONVERSOR')
            converter_control.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(converter_control))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(toy) > 0:
            # se o número de objetos na lista de brinquedos for maior do que 0 ele vai executar essa condição
            print('BRINQUEDOS')
            toy.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(toy))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(DVD) > 0:
            # se o número de objetos na lista de DVD (filmes...) for maior do que 0 ele vai executar essa condição
            print('DVDs')
            DVD.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(DVD))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(CD) > 0:
            # se o número de objetos na lista de CD (músicas) for maior do que 0 ele vai executar essa condição
            print('CDs')
            CD.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(CD))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(ps2) > 0:
            # se o número de objetos na lista de jogos de PS2 for maior do que 0 ele vai executar essa condição
            print('JOGOS DE PS2')
            ps2.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(ps2))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(xbox360) > 0:
            # se o número de objetos na lista de jogos de xbox 360 for maior do que 0 ele vai executar essa condição
            print('JOGOS DE XBOX 360')
            xbox360.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(xbox360))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        if len(other) > 0:
            # se o número de objetos na lista de outros for maior do que 0 ele vai executar essa condição
            print('OUTRAS COISAS')
            other.sort()     # o sort() coloca todas os produtos em ordem alfabética
            print(separator.join(other))
            # o separador é a gambiarra que eu coloquei lá no inicio
            # o join() vai juntar a gambiarra '\n' para não aparecer isso [' ']
            # EX:. ['lapis'] passa a ser agora lapis
            print('')
        break
    else:   # se o usuario digitar algo diferente das opções principais ele voltará ao inicio
        print('')
        print('DIGITE APENAS AS OPÇÕES A QUE ESTÃO ABAIXO.')
pass  # se passar pelo else: ele volta pro inicio
