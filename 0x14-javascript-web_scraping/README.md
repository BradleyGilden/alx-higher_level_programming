# Web Scraping

Web scraping is used to extract data from websites. This is different from an API that is designed to serve you specific content depending on your request. Web scraping extracts data straight from web pages by parsing HTML structures. There are many frameworks that can automate this process

**NB: Web Scraping should always be done ethically and legally. Before attempting to scrape data, check a websites terms of services and robots.txt file to ensure no rules are violated**

I will be using the Node.js request module (`npm install request`).<br> *WARNING: this package is deprecated however is still used in this project because of my coursework requirements*

## Directory Files:

* [0-readme.js](0-readme.js) - a script that reads and prints the content of a file.
* [1-writeme.js](1-writeme.js) - a script that writes a string to a file.
* [2-statuscode.js](2-statuscode.js) -  a script that display the status code of a GET request.
* [3-starwars_title.js](3-starwars_title.js) - a script that prints the title of a Star Wars movie where the episode number matches a given.
* [4-starwars_count.js](4-starwars_count.js) - a script that prints the number of movies where the character “Wedge Antilles” is present.
* [5-request_store.js](5-request_store.js) - a script that gets the contents of a webpage and stores it in a file.
* [6-completed_tasks.js](6-completed_tasks.js) - a script that computes the number of tasks completed by user id.
