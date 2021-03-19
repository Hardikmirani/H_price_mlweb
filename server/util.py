import json
import pickle
import numpy as np
__city = None
__data_columns = None
__model = None


def get_estimated_price(city, bedrooms, bathrooms, sqft_living, floors, condition, price_per_sqft):
    try:
        loc_index = __data_columns.index(city.lower())
    except:
        loc_index = -1


    x = np.zeros(len(__data_columns))

    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft_living
    x[3] = floors
    x[4] = condition
    x[5] = price_per_sqft

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_city_names():
    return __city


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __city

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __city = __data_columns[6:]

    global __model
    with open("./artifacts/ashwathi_model01.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    print("test")
    load_saved_artifacts()
    print(get_city_names())
    print(get_estimated_price('Shoreline', 3, 1.5, 1340, 3, 3, 300))
