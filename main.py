#./mitmdump --ssl-insecure --mode upstream:http://127.0.0.1:8080 -p 8081 -s main.py
#python3

from mitmproxy import http
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import urllib.parse as urlparse


class AESCipher:
    #AEC-CBC-PKCS5Padding
    def __init__(self, key,iv):
        self.keyb = b64decode(key)
        self.ivb = b64decode(iv)

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.keyb, AES.MODE_CBC, self.ivb)
        return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'),AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.keyb, AES.MODE_CBC, self.ivb)
        return unpad(self.cipher.decrypt(raw), AES.block_size)


def request(flow: http.HTTPFlow) -> None:
    content = flow.request.content.decode("utf-8")
    url = flow.request.pretty_url
    print("[#]", "-----------Request--------------\n")
    print('REQ', content)

    if ("evil.com" in url):
        if(len(content)!=0):
            output = AESCipher("KEY","IV").decrypt(content).decode('utf-8')
            print ("#output: ",output)
            flow.request.content = output.encode('utf-8')


def response(flow: http.HTTPFlow) -> None:
    print("[#]", "-----------Response--------------\n")
    content = flow.response.content.decode("utf-8")
    url = flow.request.pretty_url
    print('#RES', content)

    if ("evil.com" in url):
        if(len(content)!=0):
            output = AESCipher("KEY","IV").encrypt(content).decode('utf-8')
            print ("#output: ",output)
            flow.response.content = output.encode('utf-8')
