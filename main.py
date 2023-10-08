import os

maudoso = input('Maudoso? ')
singleItem = input('Single Item? ')
length = input('Len? ')

if maudoso == 'SIM':
    maudoso = True

if singleItem.lower() == 'true' or singleItem.lower() == 'sim' or singleItem.lower() == 's':
    singleItem = True

if length.lower() == 'true' or length.lower() == 'sim' or length.lower() == 's':
    length = True

disco = 'c:/'

list1 = os.listdir(disco)
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
lista7 = []
lista8 = []
lista9 = []
lista10 = []
listaTotal = []

for item in list1:
    try:
        lista2 = os.listdir(f'{disco}{item}')
    except:
        pass


    for item2 in lista2:
        try:
            lista3 = os.listdir(f'{disco}{item}/{item2}')
        except:
            pass


        for item3 in lista3:
            try:
                lista4 = os.listdir(f'{disco}{item}/{item2}/{item3}')
            except:
                pass


            for item4 in lista4:
                try:
                    lista5 = os.listdir(f'{disco}{item}/{item2}/{item3}/{item4}')
                except:
                    pass


                for item5 in lista5:
                    try:
                        lista6 = os.listdir(f'{disco}{item}/{item2}/{item3}/{item4}/{item5}')
                    except:
                        pass


                    for item6 in lista6:
                        try:
                            lista7 = os.listdir(f'{disco}{item}/{item2}/{item3}/{item4}/{item5}/{item6}')
                        except:
                            pass

                        for item7 in lista7:
                            try:
                                lista8 = os.listdir(f'{disco}{item}/{item2}/{item3}/{item4}/{item5}/{item6}/{item7}')
                            except:
                                pass

                            for item8 in lista8:
                                try:
                                    lista9 = os.listdir(f'{disco}{item}/{item2}/{item3}/{item4}/{item5}/{item6}/{item7}/{item8}')
                                except:
                                    pass

                                for item9 in lista9:
                                    try:
                                        lista10 = os.listdir(f'{disco}{item}/{item2}/{item3}/{item4}/{item5}/{item6}/{item7}/{item8}/{item9}')
                                    except:
                                        pass

                                    for item10 in lista10:
                                        try:
                                            if maudoso:
                                                os.system(f'start {disco}{item}/{item2}/{item3}/{item4}/{item5}/{item6}/{item7}/{item8}/{item9}/{item10}')
                                            else:
                                                if singleItem:
                                                    print(item10)
                                                elif length:
                                                    listaTotal.append(item10)
                                                else:
                                                    print(f'{disco}{item}/{item2}/{item3}/{item4}/{item5}/{item6}/{item7}/{item8}/{item9}/{item10}')
                                        except:
                                            pass
if length:
    print(len(listaTotal))