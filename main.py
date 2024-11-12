import csv
import sys
import datetime

class Journal:
    def __init__(self):
        self.file_name = "journal.csv"
        with open(self.file_name,'a') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "dailyJournal"])
            if file.tell() == 0:
                writer.writeheader()


    def write_entry(self,entryDate,journal):
        with open(self.file_name,'a', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "dailyJournal"])
            writer.writerow({"date": entryDate, "dailyJournal" : journal})


    def read_entry(self,seachDate):
        with open(self.file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"] == seachDate:
                    return row["dailyJournal"]
            return None


def main():
    while True:
        print("\nJournal Menu:")
        print("1. Write a new entry")
        print("2. Read previous entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_date = input("Date: ")
            print("enter your jounral below :-")
            print('-'*108)
            user_journal = input()
            journal = Journal()
            journal.write_entry(user_date,user_journal)
            print('-'*108)
            print("Entry Saved.\n")
            break

        elif choice == '2':
            query_date = input("Query Date: ")
            journal = Journal()
            query = journal.read_entry(query_date)
            if query != None:
                print('-'*108)
                print(query_date, end='\n\n')
                print(query)
                print('-'*108)
            else:
                print("No entry found on",query_date)
            break

        elif choice == '3':
            sys.exit()


if __name__ == "__main__":
    main()