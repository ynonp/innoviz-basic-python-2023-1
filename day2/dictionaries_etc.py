# Dictionaries are like lists with generic indexes
servers = {
    "172.2.20.30": {
        "ip": "172.2.20.30",
        "hostname": "dev1",
        "os": "linux",
        "ports": [80, 21]
    },
    "172.2.20.35": {
        "ip": "172.2.20.35",
        "hostname": "db",
        "os": "windows",
        "ports": [80, 21]
    },
    "172.2.20.40": {
        "ip": "172.2.20.40",
        "hostname": "test",
        "os": "linux",
        "ports": [80, 21]
    },
}


print(servers["172.2.20.35"]["os"])
servers["172.2.20.35"]["ports"].append(443)

del(servers["172.2.20.35"])

print(servers)

for key, value in servers.items():
    print(f"IP = {key}")
    print(value)


def make_list():
    return [10, 20, 30]


a, b, c = make_list()
print(b)

# tuple - immutable list
t = (10, 20, 30)


s = set()

s.add(10)
s.add(20)
s.add(30)
s.remove(10)

if 20 in s:
    print("wow")









