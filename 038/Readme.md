# DAY-38 (100 Days of Code Python)

## Workout Tracking Using Google Sheets

* Important Links:  
  * [Nutritionix API](https://www.nutritionix.com/business/api) 
  * [Nutritionix "Natural Language for Exercise" API Documentation](https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#) 
  * [Sheety](https://sheety.co/) 
  * [Sheety Documentation](https://sheety.co/docs/requests) 
<!-- 
  * My Workouts (Spreadsheet): https://docs.google.com/spreadsheets/d/12TZ00o3ApWV-iste-smnnkBPfnGGagTE8wj0Z6WURlE/edit#gid=0 <br>
-->
[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/038/Workout%20Tracking%20Project/main.py) Step 1 - Setup API Credentials and Google Spreadsheet <br>
<!--
1. Go to this link and create a copy of the My Workouts Spreadsheet. You may need to login/register.

2. Go to the Nutritionix API website and select "Get Your API Key" to sign up for a free account. 
   Double check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email.
   
3. Once logged in, you should be able to access your API key and App id:

4. Create a new project in PyCharm and in the main.py create 2 constants to store the APP_ID and API_KEY that you got from Nutritionix.
-->

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/038/Workout%20Tracking%20Project/main.py) Step 2 - Get Exercise Stats with Natural Language Queries <br>
<!--
1. Using the Nutritionix "Natural Language for Exercise" API Documentation, figure out how to print the exercise stats for a plain text input.
-->

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/038/Workout%20Tracking%20Project/main.py) Step 3 - Setup Your Google Sheet with Sheety <br>
<!--
1. Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1).
   Make sure the email matches between your Google Sheet and Sheety Account. 
   
2. In your project page, click on "New Project" and create a new project in Sheety 
   with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
   
3. Click on the workouts API endpoint and enable GET and POST.
-->

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/038/Workout%20Tracking%20Project/main.py) Step 4 - Saving Data into Google Sheets <br> 
<!--
1.  Using the Sheety Documentation, write some code to use the Sheety API to generate a new row of data in your Google Sheet 
    for each of the exercises that you get back from the Nutritionix API. 
    The date and time columns should contain the current date and time from the Python datetime module.
-->

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/038/Workout%20Tracking%20Project/main.py) Step 5 - Authenticate Your Sheety API <br>
<!--
At the moment there is no authentication that's required to access your Sheety endpoint. 
That means anyone could read and write to your "My Workout" Google Sheet.

1. Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.  
   You can hardcode the token in your code for now while you test your code. Once you're sure it works, we can add it to the environment variables in the next step.
* What is Bearer authentication?
  Bearer authentication (also known as token authentication) is an HTTP authentication scheme that involves security tokens. 
  The name “Bearer authentication” basically means “give access to the bearer of this token.” The security token or “bearer token” is just a cryptic string. 
  An example of a bearer token would be a string that could look something like this:
  "AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"

  The idea is that whoever has the secret token, has permission to interact with the spreadsheet. 
  A client - like your browser or mobile app - would then send this security token in the Authorization header when making requests to Sheety's server.

2. Using the Sheety documentation on authentication to update your Python code to authenticate your request.
-->

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/038/Workout%20Tracking%20Project/main.py) Step 6 - Environment Variables in Repl.it <br>
<!--
In order to be able to post our workout data while we're out and about, it would be easier if we can access the console and run the code in Repl.it
However, because Repl.it is open source, we don't want other people to see our API keys and secrets.

1. Using what you know about Environment Variables (see Day 35), update your code to use environment variables for all sensitive data including:

    APP_ID

    API_KEY

    SHEET_ENDPOINT

    USERNAME

    PASSWORD

    TOKEN

HINT 1: You'll need to import the os module.

  Here's how you would set environment variables

      APP_ID = os.environ["APP_ID"]
      API_KEY = os.environ["API_KEY"]
      
  and here is how you would get an environment variable

      APP_ID = os.environ.get("APP_ID")
      API_KEY = os.environ.get("API_KEY")

2. Use the Repl.it documentation to work out how to create a .env file in Repl.it and store your Environment Variables in there.
    https://docs.repl.it/repls/secret-keys#:~:text=env%20files%20are%20used%20for,see%20the%20contents%20of%20the%20.
-->
<hr>
