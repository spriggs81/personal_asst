def addName(who,info):
    if who == 'user':
        userName = open('./.data/uName.txt','w')
        userName.write(info)
        userName.close()
    if who == 'cpu':
        cpuName = open('./.data/cName.txt','w')
        cpuName = write(info)
        cpuName.close()
    return True
