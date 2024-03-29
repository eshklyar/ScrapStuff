def count_sheeps(sheep):
    count = 0
    for s in sheep:
        try:
            if not (type(s) in bool):
                raise TypeError ("only bools")
            else:
                if s:
                    count += 1
        except Exception as TypeError:
            pass

    return count
def typeS (sh):
    for s in sh:
        if type(s) is bool:
            print("bool")
        else:
            print("not bool")
            
def count_sheeps2(arrayOfSheeps):
  return arrayOfSheeps.count(True)

mysheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True, None]

# print(count_sheeps(mysheep))
print(typeS(mysheep))


# try:
#     # do something
# except Exception as e:
#     # handle it