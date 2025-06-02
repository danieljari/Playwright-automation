# How to Run Tests

Simple steps to run the tests on your computer:

## What You Need

1. **Python** (version 3.8 or newer)
   - Get it from python.org

2. **Install the test tools:**
   
   pip install pytest playwright
   playwright install

## Getting Started

1. **Get the code:**
   
   git clone [repository-url]
   cd <your-repo-name>

2. **Start the todo app:**
   
   cd todo-app
   npm install
   npm start
   
   Keep this (Terminal) window open - the app runs on http://localhost:3000

3. **Open another terminal for tests**

cd downloaded repository (go to downloaded files in terminal)

## Run the Tests

cd <your-repo-name>
cd tests

**Run all tests:**

pytest

**Run one test at a time:**

pytest test_add_task.py
pytest test_update_task_status.py
pytest test_delete_task.py
pytest test_filter_tasks_by_status.py
pytest test_local_storage.py

**Recommended: Use -s -v flags for better output: (Used automatically through pytest.ini)** 

pytest -s -v
pytest -s -v test_add_task.py

The -s flag shows debug messages and -v shows detailed test results.

## Settings

Edit conftest.py to change:
- HEADLESS = True (run without showing browser)
- USE_REMOTE = True (test live website instead of localhost)

## Having Problems? Don't worry!

- "No module named 'playwright'" → Run pip install playwright
- "Browser not found" → Run playwright install  
- "Connection refused" → Make sure npm start is running in its own terminal
- Tests too fast to see → Set HEADLESS = False in conftest.py