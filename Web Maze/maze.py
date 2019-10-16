# Solves the Web Maze challenge by hammering the server with requests.

import requests
import base64

# Encode the global list of strings into one string via base64
def encode():
    s = "".join(l)
    b = base64.b64encode(s.encode('utf-8'))
    return str(b, "utf-8")

def encs(s):
    b = base64.b64encode(s.encode("utf-8"))
    return str(b, "utf-8")


l = ["|"]
baseUrl = "http://172.17.35.181/"

#l.append("|right")

i = 0  # Occasionally the server would kick us out. Set this to where you were last to resume your progress.
k = 2**20
while("will you proceed" in str(requests.get(baseUrl + encode()).content, "utf-8") and i < k):
    p = "{0:b}".format(i).zfill(20)
    l = ["|"]
    for c in p:
        if c == '0':
            l.append("|right")
        else:
            l.append("|left")
    i += 1
    if(i % 1000 == 0):
        print(i)

# Once the loop has found node that doesn't contain "will you proceed", print it out.
print(str(requests.get(baseUrl + encode()).content, "utf-8"))
