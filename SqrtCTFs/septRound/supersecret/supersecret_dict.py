o = False
pip = False

palpha = "{ABCDEFGHIJKLMNOPQRSTUVWXYZ_}"
plaintext = ""
ct = "{fzR*RzkRf>RzkRkfzkRRkzkRk>zkzW*kfWCz}"

for n in palpha:
    if n == "{":
        o = True
        pip = True
    if n == "}":
        o = True
    n = int(ord(n))
    n = n + 43
    n = n - 654
    n = n * 4
    n = n + 4321
    n = n -543
    n = n* 5
    n = n + 543
    n = n - 87
    n = n - 54
    n = n + 54
    n = n - 65
    if n > 100:
        n = n-403
    else:
        n = n + 1
    n = n + 1
    n = n - 1
    n  = n + 2
    n = n + 32
    if n > 100:
        n = n- 50
    else:
        n = n +1
    n = n - 8500
    if n > 300:
        n = n - 300
    if n > 200:
        n = n - 110
    if n > 100:
        n = n - 60
    if n > 150:
        n = n - 60
    if n < 0:
        n = n + 300
        if n < 0:
            n = n+ 300
    if n < 65:
        n = n + 65
    if n > 127:
        n = n - 100
    if o == True:
        o = False
        if pip == True:
            pip = False
            plaintext+="{"
        else:
            plaintext+="}"
    else:
        plaintext+=chr(n)
print(plaintext)

pt = ""

for i in range(len(ct)):
  pt += ct[i] + ":"
  for j in range(len(plaintext)):
    if ct[i] == plaintext[j]:
      pt += palpha[j]
  pt+="\n"

print(pt)