import json
import random
import time
from datetime import datetime

ips = [
    "192.168.1.5",
    "45.33.12.90",
    "185.220.101.1",
    "10.0.0.8"
]

events = [
    "failed_login",
    "succesful_login",
    "malware_detected",
    "port_scan",
    "brute_force_attempt"
]

users = [
    "admin",
    "root", 
    "ubuntu",
    "guest"    
]

while True:
    log = {
        "@timestamp": str(datetime.now()),
        "event": random.choice(events),
        "source": {
            "ip": random.choice(ips)
        },
        "user": {
            "hostname": random.choice(users)
        },
        "host": {
            "hostname": "soc-lab"
        }
    }

    with open("logs/security_logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")

    print(log)
    time.sleep(2)