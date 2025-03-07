compass_dirs = {
        "N": 0.0,
        "NNE": 22.5,
        "NE": 45.0,
        "ENE": 67.5,
        "E": 90.0,
        "ESE": 112.5,
        "SE": 135.0,
        "SSE": 157.5,
        "S": 180.0,
        "SSW": 202.5,
        "SW": 225.0,
        "WSW": 247.5,
        "W": 270.0,
        "WNW": 292.5,
        "NW": 315.0,
        "NNW": 337.5,
    }

def direction(num):
    degrees = 22.5 * round(float(num)/ 22.5)
    if degrees == 360.0:
        return "N"
    else:
        for name, d in compass_dirs.items():
            if d == degrees:
                return name
    return
