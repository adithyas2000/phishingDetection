import os
import pandas as pandas

# ----------------Config----------------------------
tagLinkPercentageUpperLevel1 = 17
tagLinkPercentageLowerLevel2 = 17
tagLinkPercentageUpperLevel2 = 81

reqLinkPercenatgeUpperLevel1 = 22
reqLinkPercenatgeUpperLevel2 = 61

titleNumOfWordsUpperLimit1 = 24

filePath = 'phishingDetection/testdataset.csv'

titleStatusHeading = "Evaluated status for title"
favIconStatusHeading = "Evaluated status for favicon"
tagLinkStatusHeading = "Evaluated status for tag link percentage"
reqUrlStatusHeading = "Evaluated status for req url percenatge"

columnHeadingList = [titleStatusHeading, favIconStatusHeading,
                     tagLinkStatusHeading, reqUrlStatusHeading]
# -------------------------------------------------

dataFrame = pandas.read_csv(filePath)


urlList = []
favIconUrlList = []
tagLinkPercentageList = []
reqUrlPercentageList = []
titleList = []

titleStatusList = []  # id-1
favIconStatusList = []  # id-2
tagLinkStatusList = []  # id-3
reqUrlStatusList = []  # id-4


def setStatus(status: bool,column: int):
    strStatus = str(status)
    print()
    print(column)
    if (column == 1):
        titleStatusList.append(strStatus)
    elif (column == 2):
        favIconStatusList.append(strStatus)
    elif (column == 3):
        tagLinkStatusList.append(strStatus)
    elif (column == 4):
        reqUrlStatusList.append(strStatus)
    else:
        print("Invalid array id")
    # True if phishing, flase if legit
    # if (len(statusList)-1 >= rowNum):
    #     statusList[rowNum] = strStatus
    # else:
    #     statusList.append(strStatus)


def main():
    trueCount = 0
    for val in dataFrame.values:
        urlList.append(str(val[4]).lower().split('/')[2])
        favIconUrlList.append(val[1])
        tagLinkPercentageList.append(val[2])
        reqUrlPercentageList.append(val[3])
        titleList.append(val[0])

    numRecords = len(urlList)

    for index in range(numRecords):
        # os.system('cls')
        print("Processing URL:"+str(urlList[index]))

        # Check favIcon URL
        if (str(favIconUrlList[index]).lower().find('null') > -1):
            setStatus(False, 1)
        elif ((str(favIconUrlList[index]).find('http') > -1) and (not str(favIconUrlList[index]).find(str(urlList[index])) > -1)):
            setStatus(False, 1)
        else:
            setStatus(True, 1)

        # Check tag link percentage
        if (float(tagLinkPercentageList[index]) < tagLinkPercentageUpperLevel1):
            setStatus(False, 2)
        elif (float(tagLinkPercentageList[index]) <= tagLinkPercentageUpperLevel2):
            setStatus(True, 2)
        else:
            # Not given in requirements
            setStatus(False, 2)

        # Check req URL percentage

        if (float(reqUrlPercentageList[index]) < reqLinkPercenatgeUpperLevel1):
            setStatus(False, 3)
        elif (float(reqUrlPercentageList[index]) < reqLinkPercenatgeUpperLevel2):
            trueCount = trueCount+1
            setStatus(True, 3)
        else:
            # Not given in requirements
            setStatus(False, 3)

        # Check no of words in title
        if (len(str(titleList[index]).split(' ')) < titleNumOfWordsUpperLimit1):
            setStatus(True, 4)
        else:
            setStatus(False, 4)

    # os.system('cls')
    print("Processed "+str(len(titleList))+" records")
    print("Appending evaluated status to <"+filePath+">")

    # Convert True->1, False->0
    index = 0

    convertedStatusList = []
    statusArryList = [titleStatusList, favIconStatusList,
                      tagLinkStatusList, reqUrlStatusList]
    for col in statusArryList:
        temparray = []
        for rec in col:
            # print(str(rec).lower())
            if (str(rec).lower() == 'false'):
                print("FALSE")
                temparray.append('0')
            else:
                temparray.append('1')
                print("TRUE")
        print(temparray)
        convertedStatusList.append(temparray)

    # print(convertedStatusList)

    evaluatedDataFrame = pandas.DataFrame({titleStatusHeading: convertedStatusList[0], favIconStatusHeading: convertedStatusList[1],
                                          tagLinkStatusHeading: convertedStatusList[2], reqUrlStatusHeading: convertedStatusList[3]})
    for heading in range(4):
        dataFrame[columnHeadingList[heading]]=evaluatedDataFrame[columnHeadingList[heading]]
    dataFrame.to_csv(filePath,index=False,header=True)

    print("Done appending data")
    print(trueCount)


main()
