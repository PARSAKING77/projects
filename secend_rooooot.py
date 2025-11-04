import csv
import os
from statistics import mean
from collections import OrderedDict


def read_file():
    csv_file_path = os.path.dirname(os.path.abspath(__file__)) + '/input.csv'
    data = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    
        for row in csv.reader(file):
            data.append(row)
        return data  





def calculate_averages():
     
     for row in read_file():
          for r in row:
               
                names = r[0]
                scorse = list(map(float, r[1:]))
                avg = mean(scorse)
                print(names, avg)
            
     
     

def calculate_sorted_averages():

    averages = []

    for row in read_file():
        for r in row:

            name = r[0]
            scores = list(map(float, r[1:]))
            avg = mean(scores)
           
    for name, avg in averages: 
        print(avg, name)





def calculate_three_best():
        
        averages = []

        for row in read_file():
            for r in row:

                name = r[0]
                scores = list(map(float, r[1:]))
                avg = mean(scores)
                averages.append((name, avg))
                averages.sort(key=lambda x: (-x[1], x[0]))

        for name, avg in averages[:3]:
            print(name, avg)





def calculate_three_worst():
        
        averages = []
        for row in read_file():
            for r in row:
                 
                name = r[0]
                scores = list(map(float, r[1:]))
                avg = mean(scores)
                averages.append((name, avg))
            averages.sort(key=lambda x: (x[1], x[0]))

            for name, avg in averages[:3]:
                print(avg)






def calculate_average_of_averages():
        
        total_avg = []
        for row in read_file():

            scores = list(map(float, row[1:]))
            avg = mean(scores)
            total_avg.append(avg)
        overall_avg = mean(total_avg)

        for x in overall_avg:
            print(x)





def main():

    calculate_averages()
    calculate_sorted_averages()
    calculate_three_best()
    calculate_three_worst()
    calculate_average_of_averages()
main()