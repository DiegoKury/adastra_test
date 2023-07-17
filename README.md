# Diego Kury Rivera, Test Results!

Some quick notes I wanted to mention here...

- I rewrote most of the files using Prettier. I noticed some of them were a bit hard to follow, so instead of refactoring them myself, I decided to use this tool. It's easier to follow now!
- It's easier to note changes directly from Github pushes, but I thought it would be better for the purpose of this exercise to note the changes manually.
- I tried to change the base code the least that I could! I believe it's important to keep the code as readable as it was when you encountered it. If I changed something, it was purely because of the need for a new implementation (e.g., adding classes to div), and I included comments for every change.

## Documentation (changes made)

Added comments in every area where I changed the existing code, and references to said comments.

LOG 1: Added a '%' to the right of the percentage value (ZoneEditable.vue, line 107).

LOG 2: Added cancel method (ZoneEditable.vue, line 252).

LOG 3: Fixed the save method. It saves the inputted value and saves the previous value in case the user cancels (ZoneEditable.vue, line 154).

LOG 4: Added a new button for adding distributions and addDistribution method (ZoneEditable.vue, line 141).

LOG 5: Added a new button for deleting distributions and deleteDistribution method (ZoneEditable.vue, line 149).

LOG 6: Added error variables to show errors on the screen (ZoneEditable.vue, line 104).

LOG 7: Added an error for the distribution values not adding up to 100% (ZoneEditable.vue, line 215).

LOG 8: Added an error for non-integer values in the distribution (ZoneEditable.vue, line 202).

LOG 9: Added an error for empty zone names (ZoneEditable.vue, line 163).

LOG 10: Added an error for more than one space between words and real-time error checking (ZoneEditable.vue, line 157).

LOG 11: Added an error for names with spaces at the start or end (ZoneEditable.vue, line 181).

LOG 12: Added an error for repeated name values between zones. Added a "zoneNames" property to pass name values to ZoneEditable (ZoneEditable.vue, line 169) (ZoneEditable.vue, line 93).

LOG 13: Added "updated_at" variable to Zone Class from the back end (models.py, line 14).

LOG 14: Added "updated_at" value to the front end, and it now automatically updates to the current date when a zone is edited (ZoneEditable.vue, line 94).

LOG 15: Added saving timeout to notify the user that a save is being performed (ZoneEditable.vue, line 238).

LOG 16: Zones now have a grey display background if they have 5 distributions or more (ZoneEditable.vue, line 4).

LOG 17: Added an additional error check: distributions cannot be empty, have 0%, or non-numbers as a value (ZoneEditable.vue, line 187).

LOG 18: Added a new API Path "api/put" to save zone changes (urls.py, line 26).

LOG 19: Modified the edit API to include updated_at and distribution values (views.py, line 7).

LOG 20: Added a fetch() in front to save the changes directly (HomePage.vue, line 103).

## How to Run the Project

Tools needed:
- Python 3.10.5 [Download and install](https://www.python.org/downloads/), ensure Python is in the PATH for Windows.
- Node.js v16.13.0 [Download and install](https://nodejs.org/ru/blog/release/v16.13.0/).
- SQLite 3.39.5 [Download and install](https://www.sqlite.org/download.html), ensure SQLite is in the PATH for Windows.

For Windows, open the command prompt and navigate to the project folder.

1. Create a virtual environment:
```
python -m venv c:\path\to\your\project\env_name
```

2. Activate the environment:
```
env_name\Scripts\activate.bat
```

4. Install the packages in the `requirements.txt` file:
```
pip install -r requirements.txt
```

5. Run the Django server (this command should create a `db.sqlite3` file):
```
python manage.py runserver
```

6. Open another command prompt and navigate to the project folder where the `package.json` file is located, then run:
```
npm install
```

7. Compile the assets:
```
npm run dev
```

To compile while working, use:
```
npm run watch
```

8. Create migrations:
```
python manage.py makemigrations
```

9. Apply the migrations:
```
python manage.py migrate
```

10. Populate the database with initial data:
```
python manage.py seed_db
```
