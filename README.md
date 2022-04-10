# Project_work

## PREMIER LEAGUE FOOTBALL APP 

### AUTHOR: ART ALIU

#### Brief

The brief provided to us for this project sets the following out as its overall objective: "To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training."

I propose to create an app that allows the user to find out information on football players and the clubs they play for in the Premier League. Users will thus be able to input details for the players they choose to know information about including their football team, player age and player number.

The implicit CRUD functionality of this app will include:

CREATE:
- add players
- add football teams

READ:
- view players
- view football teams

UPDATE:
Edit the details of the items in the database

DELETE:
Remove any item from the database

## Planning, Design and Project Tracking

## ERD

I started with a basic entity relationship diagram designed around the relationships I expected these entities to have. My initial design looked like this:

![image](https://user-images.githubusercontent.com/101266740/162502102-90bdfc58-c818-4f0c-803a-fef1d6557dfe.png)

As shown in the ERD, the app models a one to many relationship between the football players and thier football clubs.This allows the user to see the relationship between the two which will show the football clubs having many different players.

## Risk Assessment

![image](https://user-images.githubusercontent.com/101266740/161800431-4227ea6f-369f-428a-8930-f8a55291ea9d.png)

## Project Tracking

I used Trello to track the progress of the project as seen with the image below.
The link to the Trello board can found here: https://trello.com/b/JVckaOOB/trello-board

![image](https://user-images.githubusercontent.com/101266740/162619016-bb99fe76-b86d-4a65-bd5a-dd48d2792906.png)

My project board is showing each of the stages of my project. As seen by the above illustration, I have broken it down into six parts:
- Project Resources
- User Stories
- To Do Tasks
- Issues/Risks
- Testing
- Done
Each of these six sections, showing the different elements of the project.

## Front End

The entry point for the app takes you to the home page via a very simple url. The home page directs the user to firstly use the menu option 'Add Football Team' to add a team. The navigation bar was done throught bootstrap.

![image](https://user-images.githubusercontent.com/101266740/162620179-47783531-0167-4622-9c9f-3a852171cfe9.png)

Page asking you to add a football team

![image](https://user-images.githubusercontent.com/101266740/162619955-45419dfd-2520-418e-a8af-51e2232da6c8.png)

Page displaying football team has been added

![image](https://user-images.githubusercontent.com/101266740/162619966-e48ee641-1908-4aeb-81fe-8ca539c010cd.png)

From this page, the user can now add a player name and correspond it to a football team of their choice which they added in the page before.

![image](https://user-images.githubusercontent.com/101266740/162619986-3bf6c9d0-292a-4bd0-b788-4aa00afe1383.png)

Details are inputed

![image](https://user-images.githubusercontent.com/101266740/162619998-5c52e713-d057-497c-92ca-3034f75a49c7.png)

From this page the user can now see the current list of players that have been added. There is also the option to delete a player off the list if the user wishes

![image](https://user-images.githubusercontent.com/101266740/162620009-493ee78b-8b7c-4fe8-afca-bb09c34bc89e.png)

From this page the user can now see the current list of football teams that have been added. The page also provides the option to edit if the user wants to edit the football team name their added

![image](https://user-images.githubusercontent.com/101266740/162620025-c01550b6-1a33-4e0a-b1e6-ec2be9e3ea52.png)

## Testing and Automation

As seen below, the app passes all the tests run. The tests can be found in the tests folder of the directory.

![image](https://user-images.githubusercontent.com/101266740/162623464-d929227e-ef35-454c-819b-5bc7ce57f670.png)


## Future Improvements

> Allow the user to implement different information about the football team/player other than just their names
- for example: adding player number, manager of the club, etc
> Make the app more appealing and eye-catching. The aesthetics of an app are very important as it also makes it easier for the user to understand.
- this could have been done by being more creative with the use of bootstrap
> Use famous football imagery to add an extra dimension to the app by making it more aesthetically pleasing


