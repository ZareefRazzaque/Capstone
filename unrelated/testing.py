import subprocess
import time
import os

process = subprocess.Popen("C:\Program Files\WindowsApps\\57540AMZNMobileLLC.AmazonAlexa_3.25.1177.0_x64__22t9g3sebte08\Alexa.exe")
for i in range(10):
    time.sleep(1)
    print(i)

print(process)
process.kill()