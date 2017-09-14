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
                try :
                    record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                except ValueError :
                    print("Please input Age and Score the type of 'int'.")

                else :
                    scdb += [record]

            elif parse[0] == 'del':
                del_list = []
                for p in scdb:
                    if p['Name'] == parse[1]:
                        del_list.append(p)
                for name in del_list:
                    scdb.remove(name)

            elif parse[0] == 'show':
                try:
                    sortKey = 'Name' if len(parse) == 1 else parse[1]
                    showScoreDB(scdb, sortKey)
                except KeyError:
                    print("Please input the correct form.\nex)'show Age'")

            elif parse[0] == 'quit':
                break

            elif parse[0] == 'find':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)

            elif  parse[0] == 'inc':
                try:
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            p['Score'] = str(int(p['Score']) + int(parse[2]))
                except ValueError:
                    print("Please input a correct form.")
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
