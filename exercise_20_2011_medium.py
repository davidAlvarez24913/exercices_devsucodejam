# 20. Come on, give me something challenging man!
# From Wikipedia:
# In number theory, a partition of a positive integer n, also called an integer partition, is a
# way of writing n as a sum of positive integers. Two sums that differ only in the order of their
# summands are considered to be the same partition.
# The partitions of 4 are listed below:
# 1. 4
# 2. 3 + 1
# 3. 2 + 2
# 4. 2 + 1 + 1
# 5. 1 + 1 + 1 + 1
# The partitions of 8 are listed below:
# 1. 8
# 2. 7 + 1
# 3. 6 + 2
# 4. 6 + 1 + 1
# 5. 5 + 3
# 6. 5 + 2 + 1
# 7. 5 + 1 + 1 + 1
# 8. 4 + 4
# 9. 4 + 3 + 1
# 10. 4 + 2 + 2
# 11. 4 + 2 + 1 + 1
# 12. 4 + 1 + 1 + 1 + 1
# 13. 3 + 3 + 2
# 14. 3 + 3 + 1 + 1
# 15. 3 + 2 + 2 + 1 --->
# 16. 3 + 2 + 1 + 1 + 1
# 17. 3 + 1 + 1 + 1 + 1 + 1
# 18. 2 + 2 + 2 + 2
# 19. 2 + 2 + 2 + 1 + 1 --->
# 20. 2 + 2 + 1 + 1 + 1 + 1
# 21. 2 + 1 + 1 + 1 + 1 + 1 + 1
# 22. 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# Create a function that receives one integer: x. If the value received is 0 or negative, or if it is
# greater than 255, the function should return -1
# The function should return the number of partitions x has.
# For example: If the function receives 4, it should return 5. If it receives 8, it will return 22, etc.
# The function will receive one integer, return another integer.
# David Alvarez C

def ramanujam(number):
    count = 0
    list_solution = [[x for _ in range(1, number+1)]
                     for x in range(1, number+1)]
    aux_a = []
    aux_b = []
    for x in list_solution:
        # When array all are ones
        if x[0] == 1:
            aux_a.append(x)

        # if the sum of array is greater thant number, reshape list
        if sum(x) > number:
            while sum(x) > number:
                x = x[:-1]
            aux_a.append(x)

        # if the sum of array is less than number, append the diferen between number and sum of elements x
        if sum(x) < number:
            magic_number = number - sum(x)
            x.append(magic_number)
            if x not in aux_a:
                aux_b.append(x)

    result = aux_a + aux_b
    # print('result ==>')

    # print(result)

    aux = []
    # Para este bloque de codigo ordeno el arreglo resultante
    for r in result[:-1]:
        # se verifica si la lista ordenada no esta en el arreglo result ejemplo: [7,1] not in [....,[7,1]]
        lista_aux = sorted([r[0], sum(r[1:])], reverse=True)
        flag_1 = lista_aux not in result
        if flag_1:
            flag_2 = lista_aux not in aux
            # en el anterior ya se agregaron nuevas combinaciones asi que se vuelve a verificar que no sea una combinacion repetiva
            if flag_2:
                aux.append(lista_aux)

    # result2 = result + aux
    result2 = tuple(tuple(x) for x in result) + tuple(tuple(x) for x in aux)

    count = len(result2)
    return (count, result2)


def combination(lista):
    lista = list(lista)
    out = []
    # si la longitud del arreglo es mayor a 1, toma el ultimo elmento y lo suma al primer elemento
    # obteniendo una nueva combinacion, se agrega el nuevo elemento a un arreglo auxiliar out, y
    # finalmente se redimensiona la lista
    if len(lista)-1 > 1:
        while len(lista)-1 > 1:
            lista[0] = lista[0] + lista[-1]
            out.append(lista[:-1])
            lista = lista[:-1]

    return out


def descomposition(lista):
    longitud_lista = len(lista)
    first_elements = lista[:longitud_lista-1]
    lista_1 = []
    aux_list = [-x for x in range(1, longitud_lista)]

    lista_3 = []
    for d in aux_list:
        if len(lista) >= 2 and lista[-1] > 1:
            # number_to_descomp = lista[-1]
            number_to_descomp = lista[d]

            lista_aux_2 = [number_to_descomp]
            while lista_aux_2[-1] > 1:

                lista_aux_2.insert(0, 1)
                lista_aux_2[-1] = lista_aux_2[-1]-1
                lista_aux = list(lista_aux_2)
                lista_1.append(lista_aux)
        # print(lista_1)

        lista_2 = []
        for lta in lista_1:
            # aux = [lista[0]]
            aux = list(first_elements)
            for l in lta:
                aux.append(l)
            lista_2.append(tuple(aux))

        # mientras todos los elementos menos el primero sean 1
        lista_2 = [list(_) for _ in lista_2]
        for z in lista_2:
            if z not in lista_3:
                lista_3.append(z)

    return lista_3


def solution(number):
    lista_principal = ramanujam(number)[1]

    sol = []
    for r in lista_principal:
        aux_2 = combination(r)
        if aux_2 != []:
            for x in aux_2:
                if x not in lista_principal:
                    sol.append(x)

    # Create tuples because are inmutables and have not reference original list
    lp_copy = tuple(tuple(x) for x in lista_principal)
    sol_copy = tuple(tuple(x) for x in sol)

    # Join tuples
    out = []
    for x in lp_copy:
        out.append(x)
    for x in sol_copy:
        if x not in out:
            out.append(x)

    # Filtered tuples by lenght is equal 2
    # list_filtered_1 = list(filter(lambda y: len(y) == 2, lista_principal))
    list_filtered_1 = list(filter(lambda y: len(y) >= 2, lista_principal))

    l_f_1 = list(map(lambda x: sorted(x), list_filtered_1))

    aux_sol = []
    for element in l_f_1:
        aux = descomposition(element)
        aux_sol.append(aux)
    # print(aux)

    aux_sol_2 = []
    for element in aux_sol:
        for el in element:
            xxx = tuple(sorted(el, reverse=True))
            if xxx not in out and xxx not in aux_sol_2:
                aux_sol_2.append(xxx)

    # Join out and aux_sol_2
    out_partial = tuple(out) + tuple(aux_sol_2)
    out_partial = sorted(
        list(filter(lambda x: sum(x) == number, out_partial)), reverse=True)
    for x in out_partial:
        print(x)
    print('--------------')
    leng = len(out_partial)
    return leng


if __name__ == '__main__':
    number_test = 6
    print(solution(number_test))
    # print(descomposition([5, 4]))
    # falta abordar mas casos revisar porque no se agrega [2,2,2,2]
    # reordenar en caso exista un arreglo '[2 + 2 + 2 + 1 + 1]', ubicar el mayor al final
    # si es el mismo numero contar cuantas veces se repite, y hacer descomposicion a cada elemento
    # agregar en el mismo arreglo
    # print(ramanujam(number_test))
    # print(descomposition([3, 2, 3]))
