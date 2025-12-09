log='ip:192.168.1.22 [STATUS=494] ENDPOINT="/api/v1/users" TIME=0.452s'

ip=log[log.index(":")+1 : log.index(" ")]
status=log[log.index("=")+1 : log.index("]",log.index("="))]
endpoint=log.split('"')[1]

print("IP : ",ip)
print("Status",status)
print("Endpoint",endpoint)

time1=log[log.split("TIME=")[1].replace("s"," ")]
time=float(time1)
print("The Time In FLoat IS ",time)