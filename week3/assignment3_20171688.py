import pickle

dbfilename = 'test3_4.dat'


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

#def findException(str):



def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        #findException(inputstr)

        try:
            if inputstr == "": continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                #try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]
            elif parse[0] == 'del':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)

            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                #if parse [1] == 'Age':
                #    sortKey = 'Age'
                #elif parse[1] =='Score':
                #    sortKey = 'Score'
                showScoreDB(scdb, sortKey)

            elif parse[0] == 'quit':
                break

            elif parse[0] == 'find':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)

            elif  parse[0] == 'inc':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)
                        p['Score'] = str(int(p['Score']) + int(parse[2]))
                        print(p)
            else:
                print("Invalid command: " + parse[0])
        #except:
         #   print("Exception Occured")
        except IndexError as e:
            print(e)






def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(str(attr) + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
