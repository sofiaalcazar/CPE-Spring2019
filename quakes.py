from quakeFuncs import *

def main():
   quakes = read_quakes_from_file('quakes.txt')
   print_earthquakes(quakes)
   res = str(input('Choice: '))

   while res.lower() != 'q':
      if res.lower() == 's':
         sort_by = str(input('Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? '))
         quakes = sorting_quakes(quakes, sort_by)
         print_earthquakes(quakes)   
      elif res.lower() == 'f':
         filter_by = str(input('Filter by (m)agnitude or (p)lace? '))
         if filter_by.lower() == 'p':
            search = str(input('Search for what string? '))
            quakes_out = filter_by_place(quakes, search)
            print_earthquakes(quakes_out)
         if filter_by.lower() == 'm':
            low = float(input('Lower bound: '))
            high = float(input('Upper bound: '))
            quakes_out = filter_by_mag(quakes, low, high)
            print_earthquakes(quakes_out)
      elif res.lower() == 'n':
         dict1 =  get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
         features = dict1['features']
         n = False
         for feature in features:
            new = quake_from_feature(feature)
            if not new in quakes:
               quakes.append(new)
               n = True
         if n == True:
            print('\nNew quakes found!!!') 
         print_earthquakes(quakes)   
      res = str(input('Choice: '))

   out = open('quakes.txt', 'w')
   for quake in quakes:
      data = quake_back_to_file(quake)
      out.write(data + '\n')
   out.close()

if __name__ == "__main__":
   main()
