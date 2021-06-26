import datetime
import time
import os
import json
import csv

CSV_FILE="timeseries.csv"


def create_time_series_csv():

    file = open(CSV_FILE,"w")
    for i in range(1,5):
       time.sleep(1)
       timeseries_data = str(datetime.datetime.now()) + "," + str(i)
       file.write(str(timeseries_data))
       file.write("\n")
    file.close()


def csvstring_to_dictonary():
    file = open(CSV_FILE,"r")
    d = dict()
    for line in file:
        line = line.strip('\n')
        (key,value) = line.split(",")
        d[key] = value

    for i in d:
        print("{} {}".format(i,d[i]))
        #print(i, d[i])
    print(d)
    file.close()
#    os.remove(CSV_FILE)

def read_csv_file():
    fields = []
    rows = []
    with open(CSV_FILE,'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        fileds = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print("Total line number: {}".format(csvreader.line_num))
    for row in rows[:5]:
        for col in row:
            print("%10s"%col,end=" ")
        print('\n')

def sort_by_timestamp():
    pass

create_time_series_csv()
#csvstring_to_dictonary()
read_csv_file()
