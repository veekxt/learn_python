import threading
import time
import urllib
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]
urllib.request.install_opener(opener)


def get_waifu(n, next_do, i):
    try:
        request = urllib.request.urlopen('http://www.thiswaifudoesnotexist.net/example-' + str(n) + '.jpg', timeout=5)
        with open('example-' + str(n) + '.jpg', 'wb') as f:
            f.write(request.read())
            print('down-ok-' + str(n))
    except:
        print("[retry later] error-" + str(n))
        next_do.append(n)


def down(start, stop):
    err = list(range(start, stop))
    while True:
        next_do = []
        for i, v in enumerate(err):
            get_waifu(v, next_do, i)
        if len(next_do) == 0:
            break
        else:
            err = next_do
            continue


def sp(start, stop, num):
    start_s = start
    step = (stop - start) // num
    while start_s != stop:
        stop_s = start_s + step
        if stop_s >= stop:
            stop_s = stop
        tmp = threading.Thread(target=down, args=(start_s, stop_s))
        tmp.start()
        start_s = stop_s


sp(1, 40001, 64)
