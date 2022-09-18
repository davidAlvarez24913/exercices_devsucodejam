
def face(x):

    half = round(x/2)

    aux1 = [_*-1 for _ in range(0, half, 3)][1:]
    aux2 = [_ for _ in range(0, half, 3)]
    aux3 = aux1 + aux2
    # aux3.remove(0)

    completed_guy = '(-_-)'
    partial_guy_right = '-_-)'
    side_guy_right = '_-)'
    final_guy_right = '-)'
    partial_guy_left = '(-_-'
    side_guy_left = '(-_'
    final_guy_left = '(-'

    out = ''
    if (x > 1 and x <= 255):
        if x < 7:
            if x % 2 == 0:
                index = [x for x in range(-half, half)]

                for i in index:

                    if i < 0:
                        if i in aux3:
                            out += partial_guy_left
                        else:
                            out += side_guy_left
                    if i > 0:
                        if i in aux3:
                            out += partial_guy_right
                        else:
                            out += side_guy_right
                    if i == 0:
                        out += completed_guy

            else:
                # impar && menor a 7

                index = [x for x in range(1-half, half)]

                for i in index:
                    if i < 0:
                        if i in aux3:
                            out += partial_guy_left
                        else:
                            out += side_guy_left
                    if i > 0:
                        if i in aux3:
                            out += partial_guy_right
                        else:
                            out += side_guy_right
                    if i == 0:
                        out += completed_guy
        else:
            if x % 2 == 0:
                # par y mayor a 7
                index = [x for x in range(-half, half)]

                for i in index:

                    if i < 0:
                        if i == index[0]:
                            out += final_guy_left
                        else:
                            if i in aux3:
                                out += partial_guy_left
                            else:
                                out += side_guy_left
                    if i > 0:
                        if i == index[-1]:
                            out += final_guy_right
                        else:
                            if i in aux3:
                                out += partial_guy_right
                            else:
                                out += side_guy_right
                    if i == 0:
                        out += completed_guy

            else:
                # impar && mayor a 7
                index = [x for x in range(1-half, half)]

                for i in index:
                    if i < 0:
                        if i == index[0]:
                            out += final_guy_left
                        else:
                            if i in aux3:
                                out += partial_guy_left
                            else:
                                out += side_guy_left
                    if i > 0:
                        if i == index[-1]:
                            out += final_guy_right
                        else:
                            if i in aux3:
                                out += partial_guy_right
                            else:
                                out += side_guy_right
                    if i == 0:
                        out += completed_guy

    return out


if __name__ == '__main__':
    print(face(14))
