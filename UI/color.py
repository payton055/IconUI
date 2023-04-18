import csv

def rgbtohex(r,g,b):
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

def colors():
    labels = {}

    with open("color.csv", "r", newline="",encoding = "ISO-8859-1") as csvfile:
        reader = csv.reader(x.replace('\0', '') for x in csvfile)
        next(reader)
        for row in reader:
            rgb=[]

            for i in range(5):
                r = row[2+i*4]
                g = row[3+i*4]
                b = row[4+i*4]
                color = rgbtohex(r,g,b)
                rgb.append(color)
            labels[row[0]]=rgb
        
    return(labels)
