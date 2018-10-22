import csv
import json

csvfile = open('/home/delhivery/Desktop/out.csv', 'r')
jsonfile = open('fileout.json', 'w')

fieldnames = ("origin_lat","origin_long","origin_id","destination_lat","destination_long","destination_id","km")
reader = csv.DictReader(csvfile, fieldnames)
reader.next()
for row in reader:
	json.dump(row, jsonfile, indent=2)
    #jsonfile.write("\n")
