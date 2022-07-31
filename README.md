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

I designed the sql database to be like this 
