import csv
import datetime

class Journal:
    def __init__(self):
        self.file_name = "journal.csv"
        with open(self.file_name,'a') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "dailyJournal"])
            if file.tell() == 0:
                writer.writeheader()


    def write_entry(self,entryDate,journal):
        with open(self.file_name,'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "dailyJournal"])
            writer.writerow({"date": entryDate, "dailyJournal" : journal})


    def read_entry(self,seachDate):
        with open(self.file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"] == seachDate:
                    print(row["dailyJournal"])




def main():
    date1 = '17-11-2024'
    note1 = "today i am feeling good."
    date2 = '18-11-2024'
    note2 = "today i am feeling okay."
    date3 = '19-11-2024'
    note3 = "today i am feeling bad."

    journal = Journal()
    # journal.write_entry(date2,note2)
    # journal.write_entry(date3,note3)
    journal.read_entry(date3)


if __name__ == "__main__":
    main()