message = "hello"
print(message)
new = ""
n = len(message)
new += message[n-1]
i = 1
while i < n - 1:
    new += message[i]
    i += 1
new += message[0]
print(new)
