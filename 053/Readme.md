# DAY-53 (100 Days of Code Python)

## Web Scraping Capstone - Data Entry Job Automation

* Important Links: 
  * [Google Forms](https://docs.google.com/forms/)     <!-- https://docs.google.com/forms/d/e/1FAIpQLSc1HKNf5H6WZttOhSYgnBPK676eGdqxo0gNL1PcOG7hiilvAg/viewform?usp=sf_link -->
  * [Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D) 

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/053/Web%20Scraping%20Capstone%20-%20Data%20Entry%20Job%20Automation/main.py) Capstone Project Program Requirements <br>
<!--
**Capstone Project Program Requirements**  
---
As we get closer to the latter part of the course, and as you build up your skills every day, 
the challenges are going to become more life-like and more challenging. As a developer, 
you will spend most of your time figuring out how to do things using Google and StackOverflow. 
It's rare that I come across a new project and already know exactly what code I need to write.

In this capstone project, you will need to apply everything you've learnt about website and 
web scraping with Beautiful Soup and Selenium to complete the project and fulfil the project requirements. 
You might also need to do your own research and revision to complete the task.

But first, you need to create a new form in Google Forms.
``` shell
    1. Go to https://docs.google.com/forms/ and create your own form.
    2. Add 3 questions to the form, make all questions "short-answer".
    3. Click send and copy the link address of the form. You will need to use this in your program.
    4. Go to this web address on Zillow and see how the website is structured, this is where you'll be scraping the data from.
```
Program Requirements:  
``` shell
    * Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).  
    * Create a list of links for all the listings you scraped.  
    * Create a list of prices for all the listings you scraped.  
    * Create a list of addresses for all the listings you scraped.  
    * Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. 
      You will need to fill in a new form for each new listing.   
    * Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. 
      You should end up with a spreadsheet with all the details from the properties.  
```
-->

[>](https://github.com/Aniruddh-482/Python-Bootcamp/blob/main/053/Web%20Scraping%20Capstone%20-%20Data%20Entry%20Job%20Automation/main.py) HINTS & SOLUTION <br>
<hr>
