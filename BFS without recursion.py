# словарь, по которому проходимся
dct = {'start': 'mid', 'mid': ['node1', 'node2'], 'node2': 'finish'}
current_node = 'start'

# после того, как мы прошли по узлу, мы аппендим его в данный массив
previous_nodes = []

# после того, как мы прошли по узлу в первый раз, мы аппендим его в данный массив
checked_nodes = []


def return_to_previous_node(current, previous_ones, checked_ones):
    checked_ones.append(current)
    current = previous_ones[-1]
    del previous_ones[-1]

    return current, previous_ones, checked_ones


while True:
    # условие выхода
    if len(previous_nodes) == 0 and len(checked_nodes) > 0:
        break
    if current_node in dct.keys():
        if type(dct[current_node]) is str:

            if dct[current_node] not in checked_nodes:
                previous_nodes.append(current_node)
                checked_nodes.append(current_node)
                current_node = dct[current_node]
                continue

            if dct[current_node] in checked_nodes:
                current_node, previous_nodes, checked_nodes = return_to_previous_node(current_node, previous_nodes,
                                                                                      checked_nodes)
                continue

        if type(dct[current_node]) is list:
            temp = current_node
            flag = False
            for i in range(len(dct[current_node])):

                # после того, как мы дойдем до конца, мы вернемся к предыдущему узлу, чтобы проверить, есть ли другие родственные непроверенные узлы
                if dct[current_node][i] not in checked_nodes:
                    previous_nodes.append(current_node)
                    checked_nodes.append(current_node)
                    current_node = dct[current_node][i]
                    flag = True
                    break
            if flag is False:
                current_node, previous_nodes, checked_nodes = return_to_previous_node(current_node, previous_nodes,
                                                                                      checked_nodes)
            continue

    # если дошли до конца
    if current_node not in dct.keys():
        current_node, previous_nodes, checked_nodes = return_to_previous_node(current_node, previous_nodes,
                                                                              checked_nodes)


print(checked_nodes)
print(current_node)
print(previous_nodes)