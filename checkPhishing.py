import os
import pandas as pandas

# ----------------Config----------------------------
tagLinkPercentageUpperLevel1=17/100
tagLinkPercentageLowerLevel2=17/100
tagLinkPercentageUpperLevel2=81/100

reqLinkPercenatgeUpperLevel1=22/100
reqLinkPercenatgeUpperLevel2=61/100

titleNumOfWordsUpperLimit1=24/100

filePath='phishingDetection/testdataset.csv'

newColumnName='Evaluated status(Phishing=1,Legit=0)'
# -------------------------------------------------

dataFrame = pandas.read_csv(filePath)


urlList = []
favIconUrlList = []
tagLinkPercentageList = []
reqUrlPercentageList = []
titleList = []

statusList = []




def setStatus(status: bool, rowNum: int):
    strStatus=str(status)
    # True if phishing, flase if legit
    if(len(statusList)-1>=rowNum):
        if(not statusList[rowNum]):
            statusList[rowNum]=strStatus
    else:
        statusList.append(strStatus)
    
def main():
    for val in dataFrame.values:
        urlList.append(str(val[4]).lower().split('/')[2])
        favIconUrlList.append(val[1])
        tagLinkPercentageList.append(val[2])
        reqUrlPercentageList.append(val[3])
        titleList.append(val[0])

    numRecords = len(urlList)

    for index in range(0, numRecords):
        os.system('cls')
        print("Processing URL:"+str(urlList[index]))

        # Check favIcon URL
        if (str(favIconUrlList[index]).lower().find('null')>-1):
            setStatus(False,index)
        elif((str(favIconUrlList[index]).find('http')>-1)and(not str(favIconUrlList[index]).find(str(urlList[index]))>-1)):
            setStatus(False,index)
        else:
            setStatus(True,index)

        # Check tag link percentage
        if(float(tagLinkPercentageList[index])<tagLinkPercentageUpperLevel1):
            setStatus(False,index)
        elif(float(tagLinkPercentageList[index])<=tagLinkPercentageUpperLevel2):
            setStatus(True,index)
        else:
            # Not given in requirements
            setStatus(False,index)

        # Check req URL percentage
        if(float(reqUrlPercentageList[index])<reqLinkPercenatgeUpperLevel1):
            setStatus(False,index)
        elif(float(reqUrlPercentageList[index])<reqLinkPercenatgeUpperLevel2):
            setStatus(True,index)
        else:
            # Not given in requirements
            setStatus(False,index)

        # Check no of words in title
        if(len(str(titleList[index]).split(' '))<titleNumOfWordsUpperLimit1):
            setStatus(True,index)
        else:
            setStatus(False,index)

    os.system('cls')
    print("Processed "+str(len(statusList))+" records")
    print("Appending evaluated status to <"+filePath+">")

    # Convert True->1, False->0
    index=0
    convertedStatus=[]
    for rec in statusList:
        if(str(rec).lower()=='false'):
            convertedStatus.append(str(0))
        else:
            convertedStatus.append(str(1))
        
        index=index+1
            
    
    evaluatedDataFrame=pandas.DataFrame({newColumnName:convertedStatus})
    dataFrame[newColumnName]=evaluatedDataFrame[newColumnName]
    dataFrame.to_csv(filePath,index=False,header=True)

    print("Done appending data")


main()