![alt text](https://raw.githubusercontent.com/51j0/Android-CertKiller/master/res/network.png "icon")
## UpstreamProxy

UpstreamProxy is a command line proxy server which provides tcpdump-like functionality to let you view, record, and programmatically transform HTTP traffic. It uses mitmdump for capturing the traffic


Currently Supporting

 * Capture HTTP and HTTPS traffic
 * Modify Request/Response
 * AES-CBC-PKCS5Padding/PKCS7Padding Encryption and Decryption


Usage
------------------

```bash
git clone https://github.com/51j0/UpstreamProxy.git
cd UpstreamProxy/
chmod 755 mitmdump


root$ ./mitmdump --ssl-insecure --mode upstream:http://127.0.0.1:8080 -p 8081 -s main.py #(forward traffic to Burp or ZAP)
 #or
root$ ./mitmdump --ssl-insecure --mode upstream:http://127.0.0.1:8080 -p 8081 -s main.py

```


![alt text](https://raw.githubusercontent.com/51j0/Android-Storage-Extractor/master/res/android.png "icon")
<div>Icons made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
