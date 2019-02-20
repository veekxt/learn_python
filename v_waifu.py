import time
import urllib
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]
urllib.request.install_opener(opener)

def get_waifu(n,err,i):
    request = urllib.request.urlopen('http://www.thiswaifudoesnotexist.net/example-' + str(i) + '.jpg', timeout=5)
    with open('wf/' + 'example-' + str(i) + '.jpg', 'wb') as f:
        try:
            f.write(request.read())
            err.pop(i)
            print('down-ok-' + str(i))
        except:
            print("error" + str(i))
            err.append(i)

# for i in range(1, 40001):
#     local_filename, headers = urllib.request.urlretrieve(
#         'http://www.thiswaifudoesnotexist.net/example-' + str(i) + '.jpg',
#         'wf/' + 'example-' + str(i) + '.jpg')
#     f = open(local_filename)
#     f.close()
#     print('down-ok-' + str(i))
#     time.sleep(5)
err = list(range(1,40001))

while True:
    for i,v in enumerate(err):
        get_waifu(v,err,i)
    if len(err) == 0:
        break
    else:
        continue

