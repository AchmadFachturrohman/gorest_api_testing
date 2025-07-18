# gorest_api_testing

1. `token_manager.py`
   - this code for:
     - Automatically log in to GitHub using Selenium.
     - Scrape the token from a specific page (likely the GoREST access token page).
     - Save the token to a .env file so it can be used by the automation pipeline.
     - Provide the Authorization header for API requests.
2. `login_manager.py`
   - this code for:
     - Automatically log in to GitHub using Selenium.
     - Scrape the token from a web page (likely the GoREST access token page).
     - Save the token to a `.env` file.
     - Provide the Authorization header for use in API testing.
3. `scenario.py`<br>
   Perform automated testing on the endpoint https://gorest.co.in/public-api/users using pytest, with the following scenarios:
   - Create user (positive & negative)
   - Get user (positive & negative)
   - Update user (positive & negative)
   - Delete user (positive & negative)
4. `conftest.py`<br>
   This code defines two fixtures for use in GoREST API testing:
     - `user_payload`: Provides valid user data for the create user test.
     - `user_holder`: Stores the user_id of the successfully created user, so it can be used in subsequent tests (get, update, delete).
6. `main.py`<br>
   This script serves as an automated entry point for:
   - Scraping the token from GoREST using TokenManager.
   - Running pytest tests on the scenario.py file.
   - Generating an HTML `report.html` from the test results.


<br>🔧 **How to Run This Code** <br>
**Option 1:** Using a Code Editor (e.g., Visual Studio Code)
1. Clone this repository to your local computer.
2. Open the project folder in Visual Studio Code or your preferred code editor.
3. Open the terminal inside the editor.
4. Run the script using:
   `python run.py`
   
**Option 2:** Using Command Prompt (CMD)
1. Clone this repository to your local computer.
2. Open CMD and navigate to the directory where the repo was downloaded.
3. Run the script using:
   `python run.py`
