# Premier League
This is a web based application provides the user with some info about the premier league.
In this project, I  built a database application for the english premier
league, that allows users to get useful information about the players, teams and
matches of the football league in England over the past 4 seasons (2018/19 to 2021/22)
The main site that provides such information is the official premier league website
(https://www.premierleague.com/home). However, the website allows for viewing the
information on a single team, player or a game of interest at a time, which makes it hard
to draw any analytics or gross reporting on a wider scale.

## Stages

### 1. Data Requirements
The database that I built in this project stores the following information: <br />
Clubs: name, home stadium, club website, squad, and history of matches<br />
Players: name, nationality, date of birth, height, weight, position and the player’s home
team for the past 4 seasons<br />
Stadiums: name, address, capacity, record league attendance, pitch size, building date<br />
Matches: Season, Date, result, home team and away teams, possession%, yellow cards,
red cards, goals, shots, and fouls conceded by each team, stadium where the match was
played.<br /> <br />
The system should also allow fans to store their reviews for each game through registering
on the system using their email addresses, and pick a username, gender, age, birthdate,
and their favorite team. After registering, the users can add their reviews for any game,
providing their rating (1-10) and a textual review.

### 2. Database Design & Implementation

I designed the sql database to be like this model:

![alt text](https://github.com/Mokhtar2121/DataBaseProject_premier_league/blob/f1f1fa3c263008b6d29ffb1834faf39deef5b180/Pics/Screenshot%202022-07-31%20205855.png?raw=true)


### 3. Web Crawling and Data Population and Hosting 


I used selenium by python to extract data from the original premier league site to save it in the sql database. 
You can view my program that I used to populate my database via this [repo.](https://github.com/Mokhtar2121/Premier_league_Setting_Up_the_sql_database.git)

### 4. Application Layer

 I designed a client application that is capable of connecting to the database hosted on a remote MySQL server. The application which based on Flask tech, have
the following functionalities: <br />

■ Add a new user review on a match <br />
■ View existing reviews on a given match<br />
■ Register a user<br />
■ Show all the players from a certain nationality and their home teams history<br />
■ Show the top 10 teams by matches won, home matches won, yellow cards, fouls,
and shots<br />
■ Show all the teams who won the most games by season<br />
■ Query and view a given team information<br />
■ Query and view a given player information (by their first and last name)<br />
■ Identify the home team for a given stadium name<br />
■ Show all the players who played a certain position<br />
■ Identify all the teams in a given city in the UK<br />


Finally, during doing this project I gained many skills in the following fields:

* Flask technology.
* HTML.
* Python.
* SQL.
* Selenium.
* Hosting databases.

