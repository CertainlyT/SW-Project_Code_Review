import pickle

dbfilename = 'assignment3.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
        for p in scdb:
            for attr in p:
                if attr == 'Age' or attr == 'Score':
                    p[attr] = int(p[attr])
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]
            except ValueError:
                print("Error : input right value")
        elif parse[0] == 'del':
            try:
                scdb_del = []
                for p in scdb:
                    if p['Name'] != parse[1]:
                        scdb_del.append(p)
                        scdb = scdb_del
            except IndexError:
                print("Error : input right value")
        elif parse[0] == 'show':
            if len(parse) == 1:
                sortKey = 'Name'
            elif parse[1] == 'Name' or parse[1] == 'Age' or parse[1] == 'Score':
                sortKey = parse[1]
            else:
                print("Invalid \'show\' command: " + parse[1])
                continue
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'inc':
            try:
                aName = parse[1]
                amountValue = int(parse[2])
                incDB(scdb, aName, amountValue)
            except:
                print("Error : input right value")

        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            specName = parse[1]
            findNameDB(scdb, specName)

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        print(keyname + "=" + str(p[keyname]), end=' ')
        for attr in sorted(p):
            if attr != keyname:
                print(attr + "=" + str(p[attr]), end=' ')
        print()


def findNameDB(scdb, findname):
    filtered_scdb = []
    for i in scdb:
        if i['Name'] == findname:
            filtered_scdb.append(i)
    for p in filtered_scdb:
        print("Name" + "=" + p['Name'], end=' ')
        for attr in sorted(p):
            if attr != 'Name':
                print(attr + "=" + p[attr], end=' ')
        print()

def incDB(scdb, incName, incAmount):
    for i in scdb:
        if i['Name'] == incName:
            i['Score'] += incAmount



scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
