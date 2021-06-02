def split_coord1(list1, list2):
    for i in list1:
        lista = i.split(",")
        lista[0] = lista[0].replace('(', '')
        lista[1] = lista[1].replace(')', '')
        list2.append([int(lista[0]), int(lista[1])])


def split_coord2(list1, list2, list3):
    for i in list1:
        listb = i.split(",")
        list2.append(listb[0])
        list3.append(listb[1])

def split_coord3(list1, list2, list3):
    for i in list1:
        listc = i.split(",")
        listc[0] = listc[0].replace('(', '')
        listc[1] = listc[1].replace(')', '')
        list2.append(int(listc[0]))
        list3.append(int(listc[1]))