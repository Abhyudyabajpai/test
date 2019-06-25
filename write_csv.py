from csv import writer
with open("first_write.csv","w") as file:
    write = writer(file)
    write.writerow(["Name","Age"])
    write.writerow(["Sheldon",31])