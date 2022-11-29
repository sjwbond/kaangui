import copy
from typing import List
from qt_core import *


def fill_dict_from_model(parent_index: QModelIndex, d: dict, model: QAbstractItemModel):
    for i in range(model.rowCount(parent_index)):
        ix = model.index(i, 0, parent_index)
        current = ix.data(0)

        if ix.data(Qt.UserRole) == "folder":
            d[current] = {}
            fill_dict_from_model(ix, d[current], model)
        else:
            d[current] = ix.data(Qt.UserRole)

def model_to_dict(model: QAbstractItemModel):
    d = dict()
    fill_dict_from_model(model.index(0, 0), d, model)

    return d

def model_to_dict_1(ix: QModelIndex, model: QAbstractItemModel):
    d = dict()
    fill_dict_from_model(ix, d, model)    
    return d

def _get_all_object_names(parent_index: QModelIndex, d: list, model: QAbstractItemModel):
    for i in range(model.rowCount(parent_index)):
        ix = model.index(i, 0, parent_index)

        if model.index(i, 0, parent_index).data(Qt.UserRole) == "folder":
            pass
        else:
            d.append(model.index(i, 0, parent_index).data(0))
        _get_all_object_names(ix, d, model)

def get_all_object_names(model: QAbstractItemModel) -> List[str]:
    d = list()
    for i in range(model.rowCount()):
        ix = model.index(i, 0)
        _get_all_object_names(ix, d, model)
    return d

def findFreeName(item: QStandardItem, name: str, prefix: str = ""):
    names = [item.child(i).data(0) for i in range(item.rowCount())]            

    counter = 0
    freeName = name
    if freeName in names:
        freeName = prefix + name
    while freeName in names:
        counter+=1                
        freeName = prefix + name + " (" + str(counter) + ")"
    
    return freeName


def sanitize_json(json):
    model = copy.deepcopy(json) 
    if "name" in model:
        del model["name"]
    if "hash" in model:
        del model["hash"]
    if "id" in model:
        del model["id"]
    if "modelId" in model:
        del model["modelId"]
    if "savedAt" in model:
        del model["savedAt"]
    if "savedBy" in model:
        del model["savedBy"]
    if "savedByName" in model:
        del model["savedByName"]
    if "versionId" in model:
        del model["versionId"]
    return model
