# DoriWorld
Pygame Project DoriWorld

## Author
Yingyi He

## Description
This repo remains all files of a shooting game. It made by pygame and Flask.

## Instruction
  1. Open web page "app.py"
  2. Run the game "main.py"
  
  Note: if run the game only, without open the web page, it cannot send the user score to the web page, which means user won't have the score.
  
## Screen
- Welcome page
  - The first page of the game, which is also its home page with User Login function
  
    <img width="1045" alt="Home-Menu-page" src="https://user-images.githubusercontent.com/100324443/210211406-2d11ee83-b738-43de-9686-f64ab426d94f.png">
    
    <img width="400" alt="Login" src="https://user-images.githubusercontent.com/100324443/210211674-b8ab8230-8dd0-4fa1-af3b-30e9b172b0b4.png">

- Menu score page
  - To check the user scores with user's score history and its updates
  
    <img width="784" alt="Score-page" src="https://user-images.githubusercontent.com/100324443/210211693-bbe0400f-55a8-44fd-8875-b877a9899c46.png">

- Prepare page
  - To let user practice the keyboard actions to get ready for the game
  
    <img width="1042" alt="Game-Introduction-page" src="https://user-images.githubusercontent.com/100324443/210211839-32801b43-dee3-4ebf-816e-eb1449fe9ba1.png">

- Game page
     
    <img width="1047" alt="Game-Page" src="https://user-images.githubusercontent.com/100324443/210211938-7ab054b2-379c-43ca-ad18-87dd13f5df45.png">

- Gameover page
  - To show the final score of the previous round to user
  
    <img width="1045" alt="User-Score" src="https://user-images.githubusercontent.com/100324443/210212013-a2214156-25a4-4d6f-bfc1-502eaee51361.png">

- Flask Web app of user scores
  - To start the web server and store the user score from response
  
    <img width="349" alt="Flask-Page" src="https://user-images.githubusercontent.com/100324443/210212154-d4fd0cda-b08a-48b3-8b23-91110b0de9aa.png">



## Skill
- python class uility
- python flask uility
- python pygame uility

## Principle
- Use python class to manage user information in a dictionary including username and scores.
- Use python Flask to post request of username and score and put them back to a dictionary
- Use python Pygame to write all game screens including display screen mode, draw, update and so on.
- Use python Pygame to design operations of the game including killing enemies, killing character and so on.
- Use python Pygame to manage background music playing and font display.


  
