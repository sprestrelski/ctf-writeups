from hashlib import md5

hp = input("Enter plaintext: ")

p = bytes.fromhex(hp)

h = md5(p).hexdigest()

if h[6:-6] == "25255fb1a26e4bc422ae" and hp != "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70":
    print("Correct! Submit ictf{your_input_here}")
else:
    print("Wrong!")