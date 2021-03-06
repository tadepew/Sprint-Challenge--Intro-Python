# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.name} ({self.lat}, {self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    with open("/Users/tadepew/Desktop/Lambda Projects/Sprint-Challenge--Intro-Python/src/cityreader/cities.csv", newline="") as csvfile:
      # Why can't I just write cities.csv????

        lines = csv.reader(csvfile, delimiter=",")

        for index, data in enumerate(lines):
            if index > 0:
                cities.append(City(data[0], float(data[3]), float(data[4])))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def match_cities():
    print("Search for a city:")
    corner_1 = input("Enter lat and long of one corner seperated by a comma\n")
    corner_2 = input(
        "Enter lat and long of other corner seperated by a comma\n")

    # CONVERT coordinates
    conv_corner_1 = [float(value.strip()) for value in corner_1.split(",")]
    conv_corner_2 = [float(value.strip()) for value in corner_2.split(",")]

    # print(conv_corner_1)

    global cities
    matching_cities = cityreader_stretch(
        conv_corner_1[0], conv_corner_1[1], conv_corner_2[0], conv_corner_2[1], cities)

    if len(matching_cities) > 0:
        print("Matching cities found below:\n")

        for c in matching_cities:
            print(c)

    else:
        print("No cities found. Try again\n")

    return matching_cities


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    min_lat = min(lat1, lat2)
    min_lon = min(lon1, lon2)
    max_lat = max(lat1, lat2)
    max_lon = max(lon1, lon2)
    # print(min_lat)
    within = [c for c in cities if (c.lat >= min_lat) and (
        c.lat <= max_lat) and (c.lon >= min_lon) and (c.lon <= max_lon)]

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within


match_cities()
