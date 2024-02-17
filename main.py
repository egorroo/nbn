mbn = []
while True:
  fvf = int(input("Ent num:"))
  if fvf == 0:
    print(mbn)
    break
  else:
    mbn.append(fvf)
num = int(input("ent num:"))
sym = input("Ent syb:")
numsym = sym * num
print(numsym)
awg = input("Wright somesing:")
print(awg[::-1])
