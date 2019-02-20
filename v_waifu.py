import time
import urllib
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]
urllib.request.install_opener(opener)

def get_waifu(n,next_do,i):
    try:
        request = urllib.request.urlopen('http://www.thiswaifudoesnotexist.net/example-' + str(n) + '.jpg', timeout=5)
        with open('D:/wf/' + 'example-' + str(n) + '.jpg', 'wb') as f:
            f.write(request.read())
            print('down-ok-' + str(n))
    except:
        print("error" + str(n))
        next_do.append(n)

# for i in range(1, 40001):
#     local_filename, headers = urllib.request.urlretrieve(
#         'http://www.thiswaifudoesnotexist.net/example-' + str(i) + '.jpg',
#         'wf/' + 'example-' + str(i) + '.jpg')
#     f = open(local_filename)
#     f.close()
#     print('down-ok-' + str(i))
#     time.sleep(5)
err = list(range(1,20))

while True:
    next_do = []
    for i,v in enumerate(err):
        print("v is "+str(v))
        get_waifu(v,next_do,i)
    if len(next_do) == 0:
        break
    else:
        err = next_do
        continue

