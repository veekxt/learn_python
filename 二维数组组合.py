a = [[1,2],[3,4,5],[6,7],[1,2,3]]


def make_a(a):
    li=[]
    for i in a:
        li.append(len(i))
    t = []
    k = len(li) - 1
    for i in range(k + 1):
        t.append(0)
    t[k]=-1
    while (True):
        is_end = False
        k = len(li) - 1
        while (True):
            if t[k] < li[k]:
                t[k] += 1
                if (t[k]) == li[k]:
                    t[k] = 0;
                    k -= 1
                else:
                    break
                if (k < 0):
                    is_end = True
                    break
        if (is_end):
            break
        else:
            rs = []
            for i,j in enumerate(t):
                rs.append(a[i][j])
            print(rs)
make_a(a)