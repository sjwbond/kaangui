from glob import glob

def load_directory(path, objects):
    objectsFilenamesList = glob(path+"/Objects*.txt")
    relationshipsFilenamesList = glob(path+"/Relationships*.txt")
    propertiesFilenamesList = glob(path+"/Properties*.txt")

    for objectsFilePath in objectsFilenamesList:
        with open(objectsFilePath) as file_in:
            next(file_in)
            for line in file_in:
                line = line.rstrip()
                parts = line.split('\t')
                objects[parts[0]] = {
                "Object_Name": parts[0],
                "Object_Type": parts[1],
                "Parent Objects": [],
                "Properties": []
            }

    for relationshipsFilePath in relationshipsFilenamesList:
        with open(relationshipsFilePath) as file_in:
            next(file_in)
            for line in file_in:
                line = line.rstrip()
                parts = line.split('\t')
                if parts[0] in objects:
                    objects[parts[0]]["Parent Objects"].append({
                        "Parent Object" : parts[1],
                        "Parent Property" : parts[2] if len(parts) > 2 else ""
                    })

    for propertiesFilePath in propertiesFilenamesList:
        with open(propertiesFilePath) as file_in:
            next(file_in)
            for line in file_in:
                parts = line.split('\t')
                if parts[0] in objects:
                    objects[parts[0]]["Properties"].append({
                        "Parent Object": parts[1],
                        "Target Object": parts[2],
                        "Property": parts[3],
                        "Date_From": parts[4],
                        "Date_To": parts[5],
                        "Value": parts[6],
                        "Variable": parts[7],
                        "Variable_Effect": parts[8],
                        "Timeslice": parts[9],
                        "Timeslice_Index": parts[10],
                        "Group_id": parts[11],
                        "Priority": parts[12],
                        "Scenario": parts[13]
                    })

def get_folder(name: str):
    parts = name.split()
    if len(parts[0]) == 2:
        return parts[0].upper()
    return None

def readTxt(folder):
    objectDict = {}
    load_directory(folder+"/Common", objectDict)
    load_directory(folder+"/Data", objectDict)

    newDict = {"SystemInputs": {"Generator":{} , "Demand":{},"Variable":{},"DataSource":{},"Storage":{},"Reservoir":{},"DBDataSource":{},"DBTimeSeries":{},"Hydro_Generator":{},"Group":{},"Fuel":{},"Node":{},"Line":{},"Currency":{},"Emissions":{},"Scenario":{}}}

    for key, value in objectDict.items():
        folder = get_folder(value["Object_Name"])
        if folder is not None:
            if folder not in newDict["SystemInputs"][value["Object_Type"]]:
                newDict["SystemInputs"][value["Object_Type"]][folder] = {}
            newDict["SystemInputs"][value["Object_Type"]][folder][value["Object_Name"]] = value
        else:
            newDict["SystemInputs"][value["Object_Type"]][value["Object_Name"]] = value

    return newDict
