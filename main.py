from transformers import pipeline
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import sys

class Journal:
    # Initalize a csv called journal.csv and write its fieldnames(if not already)
    def __init__(self):
        self.file_name = "journal.csv"
        with open(self.file_name,'a') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "sentiment", "dailyJournal"])
            if file.tell() == 0:
                writer.writeheader()


    # Write the journal of the Date given into journal.csv file
    def write_entry(self,entryDate,journal,sentiments):
        with open(self.file_name,'a', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "sentiment", "dailyJournal"])
            writer.writerow({"date": entryDate, "dailyJournal" : journal, "sentiment" : sentiments})


    # Return the journal of the Date provided if not avaliable returns None
    def read_entry(self,seachDate):
        with open(self.file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"] == seachDate:
                    return row["dailyJournal"]
            return None
        

    # Checks if there already exist an journal on provided date
    def checks_entry(self,entryDate):
        with open(self.file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"] == entryDate:
                    print("A journal already exist on",entryDate)
                    while True:
                        confirmation = input("You wish to overwrite it (yes/no): ")
                        if confirmation == "yes":
                            return True
                        elif confirmation == "no":
                            sys.exit()
            return False


    # rewrite the journal and sentiment part of a given date
    def overwrite_entry(self,entryDate,journal,sentiments):
        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                if row["date"] == entryDate:
                    row['dailyJournal'] = journal
                    row['sentiment'] = sentiments
                rows.append(row)

        with open(self.file_name,'w') as file:
            writer = csv.DictWriter(file, fieldnames= ["date", "sentiment", "dailyJournal"])
            writer.writeheader()
            writer.writerows(rows)


    # visualize the sentiments using matplotlib
    def visualize_sentiments(self):
        dates = []
        sentiment_score = []
        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(datetime.strftime(row['date'], "%d-%m-%Y").date())
                sentiment_score.append(float(row['sentiment']))

        sorted_data = sorted(zip(dates, sentiment_score))
        dates, sentiment_score = zip(*sorted_data)

        plt.plot(dates, sentiment_score, c= "#4169E1", marker= 'o', label= "Sentiments Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sentiments")
        plt.title("Daily Sentiment Analysis")

        # display datetime object as only date with format "DD-MM-YYYY"
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%d-%m-%Y")) 

        # get currect axes and set the xticks to date (to eliminate duplicate dates over a region)
        plt.gca().set_xticks(dates)
        plt.xticks(rotation=45)
        plt.yticks(
            [1, 2, 3, 4, 5],  # Tick positions
            ["Very Bad", "Bad", "Neutral", "Good", "Very Good"]  # Custom labels
        )
        plt.legend()
        plt.tight_layout()
        plt.show()


def main():
    while True:
        # Interactive Menu for the user
        print("\nJournal Menu:")
        print("1. Write a new entry")
        print("2. Read previous entries")
        print("3. Visualize Sentiment trends")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Checks for a Valid Date
            while True:
                user_date = input("Enter Date (DD-MM-YYYY): ")
                if valid_date(user_date):
                    break
                else:
                    print("Enter a Valid Date in format DD-MM-YYYY.")

            # write/overwrite the journal accordingly
            journal = Journal()
            if journal.checks_entry(user_date):
                print("enter your jounral below :-")
                print('-'*108)
                user_journal = input()
                sentiment_score = calculate_sentiment(user_journal)
                journal.overwrite_entry(user_date,user_journal,sentiment_score)
                print('-'*108)
                print("Entry Saved.\n")
                break
            else:
                print("enter your jounral below :-")
                print('-'*108)
                user_journal = input()
                sentiment_score = calculate_sentiment(user_journal)
                journal.write_entry(user_date,user_journal,sentiment_score)
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
            journal = Journal()
            journal.visualize_sentiments()

        elif choice == '4':
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
    it will return a average score between 1 to 5.
    where:- 5 stars = very good
            4 stars = good
            3 stars = netural
            2 stars = bad
            1 stars = very bad
    """
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    journal = journal.split('.')
    scores = [sentiment_pipeline(line)[0]['label'] for line in journal]

    star_values = {"1 star": 1, "2 stars": 2, "3 stars": 3, "4 stars": 4, "5 stars": 5}
    numeric_scores = [star_values[score] for score in scores]
    average_score = sum(numeric_scores) / len(numeric_scores)
    return round(average_score,2)

if __name__ == "__main__":
    main()