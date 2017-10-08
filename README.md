# collegeclairvoyant

https://collegeclairvoyant.herokuapp.com/

Inspiration
-----------
We all spent hours in late high school stalking our dream school forums on College Confidential and thought it would be cool to automate and quantify this information.

What it does
-----------
Crawls College Confidential forums for Stanford between 2017 to 2021 and pulls student decision information. Uses IBM-Watson to parse out extracurriculars and regexes to pull objective information about the student. Makes a training matrix and an expectation matrix with this data, uses an MLP to learn from it. Takes in user info and runs it through the program which guesses how you'd fair in the admission decision.

How we built it
---------------
Using Python and Beautiful Soup for crawling, regexes and Watson for parsing, SKlearn for predicting.

Accomplishments that we're proud of
-----------------------------------
It works! Our webpage outputs info and the parsing of the website data does a good job summarizing each student.
