import pickle
import json
import numpy as np

__area = None
__data_columns = None
__model = None


def get_estimated_price(area, total_sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(area.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __area

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __area = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/Estate_Price_Prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_area_names():
    return __area


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_area_names())
    print(get_estimated_price('Bomet Town	', 1000, 3, 3))
    print(get_estimated_price('Longisa', 1000, 2, 2))
    print(get_estimated_price('Mulot', 1000, 2, 2)) # other location
    print(get_estimated_price('Ruiru', 1000, 2, 2))  # other location
