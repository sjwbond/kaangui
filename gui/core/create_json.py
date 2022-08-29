import os
import json
import glob
from pathlib import Path, PureWindowsPath

def readTxt(folder, modelID):

     # with open('C:/Users/Kaan/Desktop/Git Folder/NewGui/modelstructure-fixed.json') as json_file:
     #     data = json.load(json_file)


    p1 = str(PureWindowsPath(folder))

    p2 = str(PureWindowsPath("/Common/Objects*.txt"))
    objectsFilenamesList = glob.glob(p1+p2)
    p2 = str(PureWindowsPath("/Common/Relationships*.txt"))
    relationshipsFilenamesList = glob.glob(p1+p2)
    p2 = str(PureWindowsPath("/Common/Properties*.txt"))
    propertiesFilenamesList = glob.glob(p1+p2)


    objectDict = {}

    for objectsFilePath in objectsFilenamesList:
     with open(objectsFilePath) as file_in:
         next(file_in)
         for line in file_in:
             line= line.rstrip()
             #line=line.decode('utf-8','ignore').encode("utf-8")
             objectDict[line.split('\t')[0]]= {}
             objectDict[line.split('\t')[0]]["Object_Name"] = line.split('\t')[0]
             objectDict[line.split('\t')[0]]["Object_Type"] = line.split('\t')[1]
             objectDict[line.split('\t')[0]]["Parent Objects"] = []
             objectDict[line.split('\t')[0]]["Properties"] = []
             objectDict[line.split('\t')[0]]["Model Id"] = modelID

    allParents = set()
    for relationshipsFilePath in relationshipsFilenamesList:
     with open(relationshipsFilePath) as file_in:
         next(file_in)
         for line in file_in:
                 line= line.rstrip()
                 #line=line.decode('utf-8','ignore').encode("utf-8")
                 try:
                     #objectDict[line.split('\t')[0]]["Parent Object"].append([line.split('\t')[1],line.split('\t')[2]])
                     objectDict[line.split('\t')[0]]["Parent Objects"].append({"Parent Object" : line.split('\t')[1], "Parent Property" : line.split('\t')[2]})
                     
                 except:
                    try:
                        objectDict[line.split('\t')[0]]["Parent Objects"].append({"Parent Object" : line.split('\t')[1], "Parent Property" : ""})
                    except KeyError as e:
                        pass

                 allParents.add(line.split('\t')[1])

    for propertiesFilePath in propertiesFilenamesList:
     with open(propertiesFilePath) as file_in:
         next(file_in)
         for line in file_in:
             #line=line.decode('utf-8','ignore').encode("utf-8")
             try:
                 objectDict[line.split('\t')[0]]["Properties"].append({"Parent Object": line.split('\t')[1],
                                                                       "Target Object": line.split('\t')[2],
                                                                       "Property": line.split('\t')[3],
                                                                       "Date_From": line.split('\t')[4],
                                                                       "Date_To": line.split('\t')[5],
                                                                       "Value": line.split('\t')[6],
                                                                       "Variable": line.split('\t')[7],
                                                                       "Variable_Effect": line.split('\t')[8],
                                                                       "Timeslice": line.split('\t')[9],
                                                                       "Timeslice_Index": line.split('\t')[10],
                                                                       "Group_id": line.split('\t')[11],
                                                                       "Priority": line.split('\t')[12],
                                                                       "Scenario": line.split('\t')[13]})
             except:
                 pass

    p2 = str(PureWindowsPath("/Data/Objects*.txt"))
    objectsFilenamesList = glob.glob(p1+p2)
    p2 = str(PureWindowsPath("/Data/Relationships*.txt"))
    relationshipsFilenamesList = glob.glob(p1+p2)
    p2 = str(PureWindowsPath("/Data/Properties*.txt"))
    propertiesFilenamesList = glob.glob(p1+p2)


    for objectsFilePath in objectsFilenamesList:
     with open(objectsFilePath) as file_in:
         next(file_in)
         for line in file_in:
             line= line.rstrip()
             #line=line.decode('utf-8','ignore').encode("utf-8")
             objectDict[line.split('\t')[0]]= {}
             objectDict[line.split('\t')[0]]["Object_Name"] = line.split('\t')[0]
             objectDict[line.split('\t')[0]]["Object_Type"] = line.split('\t')[1]
             objectDict[line.split('\t')[0]]["Parent Objects"] = []
             objectDict[line.split('\t')[0]]["Properties"] = []
             objectDict[line.split('\t')[0]]["Model Id"] = modelID

    

    for relationshipsFilePath in relationshipsFilenamesList:
     with open(relationshipsFilePath) as file_in:
         next(file_in)
         for line in file_in:
                 line= line.rstrip()
                 #line=line.decode('utf-8','ignore').encode("utf-8")
                 try:
                     #objectDict[line.split('\t')[0]]["Parent Object"].append([line.split('\t')[1],line.split('\t')[2]])
                     objectDict[line.split('\t')[0]]["Parent Objects"].append({"Parent Object" : line.split('\t')[1], "Parent Property" : line.split('\t')[2]})
                     
                 except:
                    objectDict[line.split('\t')[0]]["Parent Objects"].append({"Parent Object" : line.split('\t')[1], "Parent Property" : ""})
                 allParents.add(line.split('\t')[1])

    # my_list = list(allParents)
    # # with open('C:/Users/Kaan/Desktop/Git Folder/NewGui/a.txt', 'w') as f:
    # #     for item in my_list:
    # #         f.write("%s\n" % item)
    # countries =  [my_list for my_list in x if len(my_list) == 2]


    for propertiesFilePath in propertiesFilenamesList:
     with open(propertiesFilePath) as file_in:
         next(file_in)
         for line in file_in:
             #line=line.decode('utf-8','ignore').encode("utf-8")
             try:
                 objectDict[line.split('\t')[0]]["Properties"].append({"Parent Object": line.split('\t')[1],
                                                                       "Target Object": line.split('\t')[2],
                                                                       "Property": line.split('\t')[3],
                                                                       "Date_From": line.split('\t')[4],
                                                                       "Date_To": line.split('\t')[5],
                                                                       "Value": line.split('\t')[6],
                                                                       "Variable": line.split('\t')[7],
                                                                       "Variable_Effect": line.split('\t')[8],
                                                                       "Timeslice": line.split('\t')[9],
                                                                       "Timeslice_Index": line.split('\t')[10],
                                                                       "Group_id": line.split('\t')[11],
                                                                       "Priority": line.split('\t')[12],
                                                                       "Scenario": line.split('\t')[13]})

             except:
                 pass

    newDict = {"SystemInputs": {"Generator":{} , "Demand":{},"Variable":{},"DataSource":{},"Storage":{},"Reservoir":{},"DBDataSource":{},"DBTimeSeries":{},"Hydro_Generator":{},"Group":{},"Fuel":{},"Node":{},"Line":{},"Currency":{},"Emissions":{},"Scenario":{}}  , "Simulation":{"Execute":{"Models":{}, "Projects":{}}, "Simulation":{"Horizons":{},"Reports":{},"LT Plan":{},"PASA":{},"MT Schedule":{},"ST Schedule":{}}, "Settings":{"Transmission":{}, "Production":{}, "Competition":{}, "Stochastics":{}, "Performance":{}, "Diagnostics":{}}}  }

    for key, value in objectDict.items():
        newDict["SystemInputs"][value["Object_Type"]][value["Object_Name"]] = value

    return newDict


# folder = os.getcwd()

# aaa=readTxt(folder, "yarrak")

# with open('data.mdl', 'w') as fp:
#     json.dump(aaa, fp, sort_keys=True, indent=4)

# print("bok")