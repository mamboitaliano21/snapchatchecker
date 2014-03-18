import csv
username = raw_input("Enter your username: ")

with open('schat.csv', 'rb') as csvfile:
    snapchat = csv.reader(csvfile)
    for row in snapchat:
        if row[1] == username:
            print row
            break
        else:
            print "You are safe from the leak"
            break
