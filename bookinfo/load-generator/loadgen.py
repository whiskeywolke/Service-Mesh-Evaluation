import os
import requests
import subprocess
from requests.sessions import Session
import time



os.system("export INGRESS_HOST=$(minikube ip)")
os.system("export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name==\"http2\")].nodePort}')")
os.system("export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT")

result = str(subprocess.check_output("echo $GATEWAY_URL", shell=True))
ip = result[2:len(result)-3]

URL = "http://" + ip + "/productpage"

count = 10000

print(URL, ",", count, "times")


# # using curl
# start = time.time()
# for i in range(count):
# 	x = os.system("curl -s http://$GATEWAY_URL/productpage > /dev/null")

# end = time.time()
# print("curl", "time", end-start, "req/s", count/(end - start))




# # using requests
# start = time.time()
# for i in range(count):
# 	# if i % 10 == 0:
# 	# 	print(i)
# 	r = requests.get(url = URL)
# end = time.time()
# print("requests","time", end-start, "req/s", count/(end - start))

# # using requests + session
# start = time.time()
# with requests.Session() as session:
# 		for i in range(count):
# 			r = session.get(url = URL)

# end = time.time()
# print("requests+session","time", end-start, "req/s", count/(end - start))



#using aiohttp + async
import aiohttp
from aiohttp.client import ClientSession
import asyncio

async def sendRequest(url:str,session:ClientSession):
    async with session.get(url) as response:
        result = await response.text()
        #print(f'Read {len(result)} from {url}')

async def benchmark():
    my_conn = aiohttp.TCPConnector(limit=1000)
    async with aiohttp.ClientSession(connector=my_conn) as session:
        tasks = []
        for i in range(count):
            task = asyncio.ensure_future(sendRequest(url=URL,session=session))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True)

start = time.time()
asyncio.run(benchmark())
end = time.time()
print("aiohttp + async","time", end-start, "req/s", count/(end - start))
