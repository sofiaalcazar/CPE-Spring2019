from urllib.request import *
from json import *
from datetime import *
from operator import *
from utility import *

# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
# Add Earthquake class definition here   
class Earthquake:
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time   

   def __eq__(self, other):
      return self.place == other.place and \
             epsilon_equal(self.mag, other.mag) and \
	     epsilon_equal(self.longitude, other.longitude) and \
             epsilon_equal(self.latitude, other.latitude) and \
             self.time == other.time

   def __repr__(self):
      return self.place + ' ' + str(self.mag) + ' ' + str(self.longitude) + ' ' + str(self.latitude) + ' ' + str(self.time)

   def __str__(self):
      return '(%.2f)%40s at %s (%8.3f, %.3f)' % (self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude)

# Required function - implement me!   
def read_quakes_from_file(filename):
   f = open(filename, 'r')
   quakes = []
   for line in f:
      line = line.split()
      place = ' '.join(line[4:])
      mag = float(line[0])
      longitude = float(line[1])
      latitude = float(line[2])
      time = int(line[3])
      quakes.append(Earthquake(place, mag, longitude, latitude, time))
   f.close()
   return quakes
      
# Required function - implement me!
def filter_by_mag(quakes, low, high):
   filtered = []
   low = float(low)
   high = float(high)
   for quake in quakes:
      if quake.mag <= high and quake.mag >= low:
         filtered.append(quake)
   return filtered     
     
# Required function - implement me!
def filter_by_place(quakes, word):   
   filtered = []
   word = word.lower()
   for quake in quakes:
      quake_place = quake.place.lower()
      if word in quake_place:
         filtered.append(quake)
   return filtered

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   place = feature['properties']['place']
   mag = feature['properties']['mag']   
   longitude = feature['geometry']['coordinates'][0]
   latitude = feature['geometry']['coordinates'][1]
   time = int(feature['properties']['time'] / 1000)
   new = Earthquake(place, mag, longitude, latitude, time)
   return new   

def print_earthquakes(quakes):
   print('\nEarthquakes:\n------------')
   for quake in quakes:
      print(quake)
   print('\nOptions:\n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit\n') 

def sorting_quakes(quakes, sort_by):
   sort_quakes = list(quakes)
   sort_by = sort_by.lower()
   if sort_by == 'm':
      sort_quakes.sort(key = attrgetter('mag'), reverse = True)
   elif sort_by == 't':
      sort_quakes.sort(key = attrgetter('time'), reverse = True)
   elif sort_by == 'l':
      sort_quakes.sort(key = attrgetter('longitude'))
   elif sort_by == 'a':
      sort_quakes.sort(key = attrgetter('latitude'))
   return sort_quakes

def quake_back_to_file(quake):
   list_out = []
   list_out.append(str(quake.mag))
   list_out.append(str(quake.longitude))
   list_out.append(str(quake.latitude))
   list_out.append(str(quake.time))
   list_out.append(quake.place)
   line = ' '.join(list_out)
   return line
