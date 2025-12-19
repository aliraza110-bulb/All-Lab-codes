log='ip:192.168.1.22 [STATUS=494] ENDPOINT="/api/v1/users" TIME=0.452s'

# Extract IP
ip = log[log.index(":")+1 : log.index(" ")]

# Extract STATUS
status = int(log[log.index("=")+1 : log.index("]",log.index("="))])

# Extract ENDPOINT
endpoint = log.split('"')[1]

print("IP :", ip)
print("Status :", status)
print("Endpoint :", endpoint)

# Extract TIME and convert to float
time_str = log.split("TIME=")[1].replace("s","")  # "0.452"
time = float(time_str)

print("The Time in Float is:", time)

# Flag logs >= 400
if status >= 400:
    print("⚠️ FLAG: Error status detected!")
