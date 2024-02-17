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
while True:
 bab = [{"Ivan":"1248092"},{"Petor":"4758943098"},{"Fedya":"8304986549"}]
 pox = int(input("To show phonebook[1]\nTo add to phonebook[2]\nTo delete from phonebook[3]\nTo stop [0]:"))
 if pox == 1:
  print(bab)
 elif pox == 2:
  name = input("Ent name:")
  num = input("Ent num:")
  bab.append({"name":"num"})
  print(bab)
 elif pox == 3:
  name = input("Ent name:")
  bab.remove({"name":"num"})
  print(bab)
 elif pox == 0:
   break

  