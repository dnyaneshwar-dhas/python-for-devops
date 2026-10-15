##(1)
server = {
    "name": "my_server",
    "status": "stop",
    "region": "ap-south-1",
    "cpu": 75
}

print("Server Name:", server["name"])
print("Server Status:", server["status"])
print("Server Region:", server["region"])
print("CPU Usage:", server["cpu"], "%")

if server ["cpu"] > 70:
    print("Warning: High CPU usage")
else:
    print("CPU usage is normal")

    


    
