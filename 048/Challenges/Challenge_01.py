# Challenge_01: Use Selenium to Scrape Website Data #

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
# for time in event_times:
#     print(time.text)
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit() 
