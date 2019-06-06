# This is a program for mapping GPS coordinates; example of places we flew to DHSI from.
# Written by Colin Rose (crose@brocku.ca) with instruction from Jessica Otis (jmotis13@gmail.com)
# Written in Python 3.6.x 
# DHSI June 5 2019
# Downlad mapFlights and rename it as places.csv

# Find mapping code
import gmplot
import csv
import numpy as np
# read stuff from the file
placesFile = open("Places.csv")
placesReader = csv.reader(placesFile)
#latitude_list = [42, 42, 44, 44]
#longitude_list = [14, 12, 12, 14]
#latitude = (np.random.random_sample(size = 700) - 0.5) * 180
#longitude = (np.random.random_sample(size = 700) - 0.5) * 360

# convert CSV data into geoplotting

gmap = gmplot.GoogleMapPlotter(53.79648, -1.54785, 2)
#gmap = gmplot.GoogleMapPlotter(0,0,1)
#gmap = gmplot.GoogleMapPlotter.from_geocode("Toronto, Ontario", 2)

#create lists of lat and long
#loop through each list [lat, long] in placesReader

list2zip = []


for location in placesReader:
	#print(location[0], location[1]) #places showing up from CSV read
	gmap.marker(float(location[0]), float(location[1]), title=location[2])
	#print(gmap.points)
	list2zip.marker(float(location[0]), float(location[1]), "a")

gmap.plot(list2zip, color = 'blue', edge_width = 3.0)

#gmap.polygon(latitude_list, longitude_list, color = 'blue')

#create random heatmap
#gmap.heatmap(location[0], location[1])
#gmap.scatter(latitude, longitude, c='r', marker=False)

# create map, save as map.html in the working directory

gmap.draw('map.html')

# close everything
placesFile.close()

import re
with open('map.html','r') as originalMapFile:
        with open('map-clean.html','w') as cleanMapFile:
                for line in originalMapFile:
                        cleanMapFile.write(re.sub(r'\\','/',line)+'\n')