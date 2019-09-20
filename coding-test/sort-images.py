def solution(S):
    # code
    pass
    photoLines = S.splitlines()
#    print( S.splitlines())

    citiesList = []
    photoList = []
    newPhotoList = []
    for i in photoLines:
        arr = i.split(',')
        photoList.append(arr)
        citiesList.append(arr[1])

    #print(citiesList)

    list_set = set(citiesList)

    uniqueCities = (list(list_set))

    #print(uniqueCities)
    #print(photoList)

    num = {}
    countDict = {}
    sortedDict = {}

    for i in uniqueCities:
        num[i] = 0
        countDict[i] = 1
        sortedDict[i] = []
    # Calculate total number of photos for each city
    for i in range(len(uniqueCities)):
        for j in photoList:
            if j[1] == uniqueCities[i]:
                num[uniqueCities[i]] += 1
    #print(num)

    #sort by date
    for i in photoList:
        sortedDict[i[1]].append(i)

    #print("Dict")
    #print(sortedDict)
    for i in sortedDict.values():
        i.sort(key=lambda x: x[2])

    #print("Sorted by \n")
    #print(sortedDict)

    #print("\n")
    for k in sortedDict.values():
        for i in k:
            ext = i[0].rsplit(".", 1)[1]

            numOfLetters = len(str(num[i[1]]))

            number = str(countDict[i[1]]).zfill(numOfLetters)

            i.append(i[1] + number + "." + ext)
            countDict[i[1]] += 1
#    print("\n", sortedDict)

    # rename files
    for i in photoList:

        sortedList = sortedDict[i[1]]
        for j in sortedList:
            if(i[0] == j[0]):
                #print(j[3])
                i[0] = j[3]
                i.pop(3)
    strList = ""

    #print("\n".join(photoList))

    newList = []
    for i in photoList:
        newList.append(i[0])

    result=[]
    for i in newList:
        result.append(i.lstrip())
    return "\n".join(result)
    # "\n".join(strList)

print(solution('photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11' ))