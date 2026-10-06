import subprocess
result = subprocess.run(
    ["ping","-n","4","127.0.0.1"],
    capture_output=True,
    text=True
    )
print(result.stdout)
