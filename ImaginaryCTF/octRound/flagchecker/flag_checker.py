import hashlib
print("Welcome to flag checker!")
print("What flag would you like to check?")
flag = input()
result = ""
for n in flag:
  n = ord(n)
  n += 10
  n -= 4
  n += 3
  n -= 7
  n = chr(n)
  n = hashlib.md5(n.encode())
  n = n.hexdigest()
  result += str(n)

if result == "8ce4b16b22b58894aa86c421e8759df3e1671797c52e15f763380b45e841ec329e3669d19b675bd57058fd4664205d2a2510c39011c5be704182423e3a695e91cbb184dd8e05c9709e5dcaedaa0495cf8fa14cdd754f91cc6554c9e71929cce78ce4b16b22b58894aa86c421e8759df37b774effe4a349c6dd82ad4f4f21d34c0cc175b9c0f1b6a831c399e2697726618ce4b16b22b58894aa86c421e8759df37b774effe4a349c6dd82ad4f4f21d34c0cc175b9c0f1b6a831c399e2697726619e3669d19b675bd57058fd4664205d2a363b122c528f54df4a0446b6bab05515b2f5ff47436671b6e533d8dc3614845d0cc175b9c0f1b6a831c399e269772661e358efa489f58062f10dd7316b65649e8ce4b16b22b58894aa86c421e8759df3865c0c0b4ab0e063e5caa3387c1a8741363b122c528f54df4a0446b6bab055159e3669d19b675bd57058fd4664205d2a0cc175b9c0f1b6a831c399e2697726612510c39011c5be704182423e3a695e917b8b965ad4bca0e41ab51de7b31363a14a8a08f09d37b73795649038408b5f33865c0c0b4ab0e063e5caa3387c1a874183acb6e67e50e31db6ed341dd2de1595":
  print("Thats the right flag!")
else:
  print("Sorry, that flag is wrong...")