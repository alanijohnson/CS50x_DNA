# Program that identifies a person based on their DNA

from sys import argv, exit
import csv

def countStrs(str_types,sequence):

    lengthSeq = len(sequence)
    strcounts = {}

    # create dictionary of empty counts
    for item in str_types:
        strcounts[item] = 0

    # count strtypes

    for i in range(lengthSeq):
        #iterate through all types
        for item in str_types:

            lengthSTR = len(item)
            #print(sequence[i:i+lengthSTR])
            if sequence[i:i+lengthSTR] == item:
                strcounts[item] += 1
                print(sequence[i:i+lengthSTR], strcounts)

    return strcounts

def maxSTRcounts(str_types,sequence):

    lengthSeq = len(sequence)
    strcounts = {}
    counter = 1

    # create dictionary of empty counts
    for item in str_types:
        strcounts[item] = 0

    # count strtypes

    for i in range(lengthSeq):
        #iterate through all types
        for item in str_types:

            lengthSTR = len(item)
            #print(sequence[i:i+lengthSTR])
            while sequence[i:i+(lengthSTR*counter)] == item*counter:
                #print(counter, sequence[i:i+(lengthSTR*counter)], strcounts)
                counter += 1

            if strcounts[item] < counter - 1:
                strcounts[item] = counter - 1
            counter = 1

    return strcounts

# error check command line useage for arguements
if len(argv) != 3:
    print("Exiting. Two inputs are required.\nEnter Database and then csv file as arguments")
    exit(0)

# save arguements
database_filename = argv[1]
txtfilename = argv[2]

# open database and read into memory
DNA_Dict = {}
database = open(database_filename)
reader = csv.DictReader(database)
str_types = ['AGATC','AATG','TATC']

for line in reader:
    name = line['name']
    DNA_Dict[name] = {'AGATC' : int(line['AGATC']), 'AATG' : int(line['AATG']), 'TATC' : int(line['TATC'])}

database.close()

# open DNA file
seqfile = open(txtfilename, "r")
seqSTRcounts = {}
seq = seqfile.readline()
seqfile.close()

seqDict = maxSTRcounts(str_types,seq)
#print(seqDict)

for name in DNA_Dict.keys():
    #print(name, DNA_Dict[name])
    if DNA_Dict[name] == seqDict:
        print("%s" % name)
        exit(0)

print("No match")

