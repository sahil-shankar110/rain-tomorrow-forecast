def prepare_live_data(weather, le_wind):
    if weather['WindGustDir'] in le_wind.classes_:
        wind_encoded = le_wind.transform([weather['WindGustDir']])[0]
    else:
        wind_encoded = 0

    return [[
        weather['MinTemp'],
        weather['MaxTemp'],
        weather['WindGustSpeed'],
        weather['Humidity'],
        weather['Pressure'],
        weather['Temp'],
        wind_encoded
    ]]
