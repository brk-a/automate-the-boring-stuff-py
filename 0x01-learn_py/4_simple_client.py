'''
Personal Opinion

Never ever use `urllib`; use `requests` instead
'''

import urllib

fhand = urllib.request.urlopen('http//127.0.0.1:9000/romeo.txt')
for line in fhand:
    print(line.decode().strip())
