wupin = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(wupin):
    totalNum = 0
    print('Inventory:')
    for item,num in wupin.items():
        print('{} {}'.format(num,item))
        totalNum = totalNum + int(num)
    print('Total number of items:{}'.format(totalNum))

def addToInventory(addLs:list,wupin:dict):
    for i in addLs:
        wupin[i] = wupin.get(i,0) + 1
    return wupin
wupin = addToInventory(dragonLoot,wupin)

displayInventory(wupin)
