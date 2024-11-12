from transformers import pipeline
from datetime import datetime
import csv
import sys

class Journal:
    # Initalize a csv called journal.csv and write its fieldnames(if not already)
    def __init__(self):
        self.file_name = "journal.csv"
        with open(self.file_name,'a') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "sentiment", "accuracy", "dailyJournal"])
            if file.tell() == 0:
                writer.writeheader()


    # Write the journal of the Date given into journal.csv file
    def write_entry(self,entryDate,journal,sentiments):
        with open(self.file_name,'a', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "sentiment", "accuracy", "dailyJournal"])
            writer.writerow({"date": entryDate, "dailyJournal" : journal, "sentiment" : sentiments['label'], "accuracy" : sentiments['score']})


    # Return the journal of the Date provided if not avaliable returns None
    def read_entry(self,seachDate):
        with open(self.file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"] == seachDate:
                    return row["dailyJournal"]
            return None


def main():
    while True:
        # Interactive Menu for the user
        print("\nJournal Menu:")
        print("1. Write a new entry")
        print("2. Read previous entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Checks for a Valid Date
            while True:
                user_date = input("Enter Date (DD-MM-YYYY): ")
                if valid_date(user_date):
                    break
                else:
                    print("Enter a Valid Date in format DD-MM-YYYY.")

            # Prompt user to write the journal
            print("enter your jounral below :-")
            print('-'*108)
            user_journal = input()
            sentiments = calculate_sentiment(user_journal)
            journal = Journal()
            journal.write_entry(user_date,user_journal,sentiments)
            print('-'*108)
            print("Entry Saved.\n")
            break

        elif choice == '2':
            # Checks for a Valid Date
            while True:
                query_date = input("Query Date (DD-MM-YYYY): ")
                if valid_date(query_date):
                    break
                else:
                    print("Enter a Valid Date in format DD-MM-YYYY.")

            # Prints the Journal of the date provided
            journal = Journal()
            query = journal.read_entry(query_date)
            if query != None:
                print('-'*108)
                print(query_date)
                print(valid_date(query_date), end='\n\n')
                print(query)
                print('-'*108)
            else:
                print("No entry found on",query_date)
            break

        elif choice == '3':
            sys.exit()


def valid_date(givenDate):
    """
    function to check for a Valid Date entered and also returns the day of the week.
    """
    try:
        date_obj = datetime.strptime(givenDate, '%d-%m-%Y')
        weekday = date_obj.strftime('%A')  # %A = Wednesday, %a = Wed, %w = 3 (0 = Sunday)
        return weekday
    except ValueError:
        return False
    

def calculate_sentiment(journal):
    """
    function to calculate the sentiment of a journal,
    it will return a dictonary like {'label': '3 stars', 'score': 0.79}
    label:- 5 stars = very good
            4 stars = good
            3 stars = netural
            2 stars = bad
            1 stars = very bad
    score:- displays the correctness level of provided stars.
    """
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    result = sentiment_pipeline(journal)
    result = result[0]
    result['score'] = f"{result['score']:.2f}"
    return result


if __name__ == "__main__":
    main()