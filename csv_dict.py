from csv import DictWriter
with open("dogs.csv","w") as file:
    head = ["Name","Breed"]
    csv_write = DictWriter(file,fieldnames = head)
    csv_write.writeheader()
    csv_write.writerow({
        "Name":"Oril",
        "Breed": "German Shefard"})