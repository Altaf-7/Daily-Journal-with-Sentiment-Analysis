# Daily Journal with Sentiment Analysis

## Project Description
**Daily Journal with Sentiment Analysis** is a Python-based application that enables users to log their daily journal entries, analyze the sentiment of each entry, and visualize sentiment trends over time. This project uses the Hugging Face **`transformers`** library for sentiment analysis and **`matplotlib`** for graphical visualization.

Each journal entry is scored on a scale of 1 to 5:
- **1**: Very Bad
- **2**: Bad
- **3**: Neutral
- **4**: Good
- **5**: Very Good

The application allows users to:
1. Write new journal entries or update existing ones.
2. Retrieve and read past entries by date.
3. Visualize sentiment trends using line graphs.



## Features
1. **Write Journal Entries**:
   - Add new journal entries with an automatic sentiment analysis score.
   - Update existing entries if necessary.

2. **Read Past Entries**:
   - Search for and retrieve journal entries by date.
   - Display the day of the week for a given journal entry.

3. **Visualize Sentiments**:
   - Generate a line graph displaying sentiment trends over time.
     
     ![sentiment_graph](https://github.com/user-attachments/assets/2a616a78-d7cd-4037-b352-6ec53da55d9f)


4. **Sentiment Analysis**:
   - Utilizes the `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face.
   - Processes each journal entry and assigns an average sentiment score.



## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/daily-journal-sentiment.git
   cd daily-journal-sentiment
   ```

2. Install the required Python packages:
   ```bash
   pip install transformers matplotlib
   ```

3. (Optional) If you're running this in a cloud environment like GitHub Codespaces, set the `Agg` backend for `matplotlib`:
   ```python
   import matplotlib
   matplotlib.use("Agg")
   ```



## Usage
Run the application using:
```bash
python main.py
```

### Menu Options:
1. **Write a New Entry**:
   - Enter the date (`DD-MM-YYYY`) and your journal entry.
   - The program calculates the sentiment score and stores the entry in `journal.csv`.

2. **Read Previous Entries**:
   - Enter a date to retrieve the journal entry for that day.
   - Displays the text and sentiment score.

3. **Visualize Sentiment Trends**:
   - Generates a line graph of sentiment scores over time.

4. **Exit**:
   - Safely closes the application.



## File Structure
- **`main.py`**:
  - Main program file containing all classes, functions, and the interactive menu.
    
- **`journal.csv`**:
  - Stores all journal entries along with their respective sentiment scores.



## Example Workflow
1. Add a journal entry:
   ```
   Enter Date (DD-MM-YYYY): 18-11-2024
   Enter your journal below:
   Today was a calm and productive day. I managed to finish all my tasks on time.
   Entry Saved.
   ```

2. Read a past journal:
   ```
   Query Date (DD-MM-YYYY): 18-11-2024
   --------------------------------------------
   18-11-2024
   Monday

   Today was a calm and productive day. I managed to finish all my tasks on time.
   --------------------------------------------
   ```
   
3. Visualize sentiment trends:
   - A graph is displayed showing your sentiment trends over time.



## Technologies Used
1. **Python**:
   - Core language for scripting and managing data.

2. **Hugging Face Transformers**:
   - For sentiment analysis using the `nlptown/bert-base-multilingual-uncased-sentiment` model.
   - ***Note*** - I have achieved a desirable outcome using this model but you can always use a different model as you like.

3. **Matplotlib**:
   - For visualizing sentiment trends with line graphs.

4. **CSV Module**:
   - For storing and retrieving journal entries in `journal.csv`.



## Future Enhancements
1. Add encryption for journal entries for improved privacy.
2. Implement a GUI for enhanced user interaction.

