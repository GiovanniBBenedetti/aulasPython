import psutil
import time

# medindo o uso da CPU
cpu=psutil.cpu_percent(interval=1)  # interval=1 mede o uso durante 1 segundo (quanto maior o intervalo, mais estável a medida)
print("Uso da CPU:",cpu,"%")        # cpu é uma float

mem=psutil.virtual_memory()         # lendo o uso da memória
print("Memória total:",mem.total)
print("Memória usada:",mem.used)
print("Memória disponível:",mem.available)
print("Uso da memória:",mem.percent,"%")

rede=psutil.net_io_counters()       # lendo tráfego da rede
print("Bytes enviados:",rede.bytes_sent)
print("Bytes recebidos:",rede.bytes_recv)

r1=psutil.net_io_counters()         # medindo a velocidade da rede
time.sleep(1)                       # espera 1 segundo 
r2=psutil.net_io_counters()
upload=r2.bytes_sent-r1.bytes_sent
download=r2.bytes_recv-r1.bytes_recv
print("Upload:",upload,"bytes/s")
print("Download:",download,"bytes/s")