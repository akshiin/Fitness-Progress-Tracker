# Fitness Progress Tracker

## Overview
The **Fitness Progress Tracker** is a **Streamlit** web application designed to help you monitor your daily **push-up and pull-up progress**. It allows users to log their workout stats, track their best performances, and visualize progress over time using interactive charts.

## Features
- **Daily Workout Logging**: Save push-ups and pull-ups count once per day.
- **Progress Visualization**: View workout history with interactive **line charts**.
- **Personal Records Tracking**: Automatically updates the **max push-ups and pull-ups per set**.
- **One Submission Per Day**: Prevents multiple entries for the same day.
- **Persistent Data Storage**: Saves progress in **database** (`workout` and `records` tables).

## Installation & Setup
### Install Dependencies
Ensure you have **Python** installed, then install the required packages:
```bash
pip install -r requirements.txt
pip install sqlite3
```

### Run the App
Execute the following command in your terminal:
```bash
streamlit run app.py
```

## File Structure
```
Fitness-Progress-Tracker/
├── app.py             # Main Streamlit application
├── data.csv           # Stores daily push-up and pull-up logs
├── db.py              # Database initialization
├── fitness_data.db    # Database file
├── LICENSE            # MIT License file
├── records.csv        # Stores max push-ups and pull-ups per set
├── requirements.txt   # Dependencies
├── .gitignore         # Git ignore file
└── README.md          # Project documentation
```

## Usage
1. Open the **Streamlit sidebar** and input:
   - **Date** (auto-selected to today)
   - **Push-ups count**
   - **Pull-ups count**
   - **Max push-ups per set** (if a new record is achieved)
   - **Max pull-ups per set** (if a new record is achieved)
2. Click **Submit** (only allowed once per day).
3. View real-time updates in the main dashboard.

## Future Improvements
- Add authorization.
- Add calendar view for past records.
- Improve data visualization with bar charts.
- Export progress data as an Excel file.

## License
This project is open-source under the **MIT License**.

## Contact
For questions or suggestions, feel free to reach out!

---
Start tracking your fitness progress today and **stay hard!💪🏼**

