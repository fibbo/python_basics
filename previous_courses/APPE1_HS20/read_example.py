with open('data.csv', 'r') as f:
    header = f.readline()
    header.strip()  ## This didn't work as the strip doesn't act on the object itself but creates a stripped copy
    header = header.strip() ## This works now as I assign it to the (same) variable
    columns = header.split(',') ## Split a string at the ',' character
    print(columns)

    for line in f:
        line = line.strip() ## Also here remove \n from the strings
        print(line)