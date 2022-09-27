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

def get_all_object_names(model: QAbstractItemModel):
    d = list()
    for i in range(model.rowCount()):
        ix = model.index(i, 0)
        _get_all_object_names(ix, d, model)
    return d

def findFreeName(item: QStandardItem, name: str):
    names = [item.child(i).data(0) for i in range(item.rowCount())]            

    counter = 0
    freeName = name
    if freeName in names:
        freeName = "Copy of " + name
    while freeName in names:
        counter+=1                
        freeName = "Copy of " + name + " (" + str(counter) + ")"
    
    return freeName
