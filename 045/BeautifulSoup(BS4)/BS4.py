from bs4 import BeautifulSoup

# import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)                                        # print title
# print(soup.title.string)                                 # print string between the title tag
# print(soup.prettify())                                   # print all the data in the html page
# print(soup.p)                                            # Search and print first p tag
all_anchor_tags = soup.find_all(name="a")                  # Search all anchor tags
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())                                 # Print strings between all the anchor tags
    # print(tag.get("href"))                               # Print links of all anchor tags

heading = soup.find(name="h1", id="name")                  # Find h1 heading with id 'name'
print(heading)

section_heading = soup.find(name="h3", class_="heading")   # Find h3 heading with class 'heading'
print(section_heading)

# company_url = soup.select_one(selector="p a")            # Gives first matching item (anchor tag within paragraph tag)
# print(company_url)
# name = soup.select_one(selector="#name")                 # Search first tag with id 'name'
# print(name)
headings = soup.select(".heading")                        # Search all tags with class 'heading'
print(headings)
