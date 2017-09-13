import pickle

dbfilename = 'assignment3.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
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
    while True:
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
            except ValueError:
                print("Score and Age must be Integer")
            except:
                print("Please rewrite properly")
                print("Example: add Jung 21 100")
            else:
                scdb += [record]

        elif parse[0] == 'del':
            del_list = []
            for p in scdb:
                if p['Name'] == parse[1]:
                    del_list.append(p)
            for each in del_list:
                scdb.remove(each)

        elif parse[0] == 'show':
            if len(parse) <= 2:
                try:
                    sortKey = 'Name' if len(parse) == 1 else parse[1]
                    if len(scdb) == 0:
                        print("DB is empty")
                    else:
                        showScoreDB(scdb, sortKey)
                except KeyError:
                    print("Input right key")
            else:
                print("Please rewrite properly")
                print("Example: show Age")

        elif parse[0] == 'quit':
            break

        elif parse[0] == "find":
            for i in range(len(scdb)):
                if parse[1] == scdb[i]["Name"]:
                    for attr in sorted(scdb[i]):
                        print(attr + "=" + str(scdb[i][attr]), end=' ')
                    print()

        elif parse[0] == "inc":
            try:
                for i in range(len(scdb)):
                    if parse[1] == scdb[i]["Name"]:
                        scdb[i]["Score"] += int(parse[2])
            except ValueError:
                print("Input amount properly")
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

