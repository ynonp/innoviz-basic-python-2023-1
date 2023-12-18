import subprocess

# subprocess.run(["curl", "-o", "image.jpg", "https://media.bunches.co.uk/products/k0087.jpg"])

proc = subprocess.Popen(["date"], stdout=subprocess.PIPE, encoding='utf8')
result, error = proc.communicate()
print(f"Got: {result}")