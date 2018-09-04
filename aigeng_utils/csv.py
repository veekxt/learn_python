import copy

def csv2json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f = f.read()
        root_node = ""
        i = 0
        root = {}
        key_stack = []
        while i < len(f):
            if f[i] == ",":
                i += 1
            elif f[i] == "\n":
                i += 1
                comma_count = 0
                while i < len(f):
                    if f[i] == ",":
                        comma_count += 1
                        i += 1
                    else:
                        break
                if comma_count > 0:
                    key_stack = key_stack[0:comma_count]

            elif f[i] != "\r":
                a_node = ""
                while i < len(f):
                    if f[i] != "\r" and f[i] != "\n" and f[i] != ",":
                        a_node += str(f[i])
                        i += 1
                    else:
                        break
                now = {}
                now[a_node] = []
                if len(key_stack) != 0:
                    key_stack[-1].append(now)
                else:
                    root[a_node] = []
                    root_node = a_node
                key_stack.append(now[a_node])
            else:
                i += 1
                pass
        root[root_node] = key_stack[0]
        return root


def get_path(node, result, tmp=list()):
    (key, val), = node.items()
    tmp.append(node)
    if len(val) == 0:
        a_path = []
        for i in tmp:
            (keyi, vali), = i.items()
            a_path.append(keyi)
        result.append(a_path)
        return
    for i in val:
        get_path(i, result, copy.deepcopy(tmp))


def find(json, key):
    r = []
    get_path(json, r, [])
    for list in r:
        try:
            where = list.index(key)
            list = list[0:where + 1]
            split = "."
            return split.join(list)
        except Exception as e:
            pass
    return '不存在关键字: %s' % key


if __name__ == '__main__':
    a = csv2json("history.csv")
    print(a, '\n')
    r = find(a, "希腊")
    print(r)
    r = find(a, "城邦")
    print(r)
    r = find(a, "亚洲")
    print(r)
    r = find(a, "汉谟拉比法")
    print(r)
