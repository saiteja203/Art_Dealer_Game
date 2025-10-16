# Art Dealer Game

Art Dealer Game is a fun, educational simulation designed to help K-8 students learn the basics of computation, logic, and pattern recognition through an interactive card game.

In this game, the player acts as an art seller, while the computer plays the role of the art dealer.  
The dealer buys certain paintings (represented by playing cards), and the student's goal is to figure out what pattern the dealer is using to make those purchases!


Game Concept:
- Each round, the student lays out four cards.
- The art dealer (computer) chooses to buy or reject cards based on a hidden pattern.
- The player observes and guesses the pattern.
- If the player guesses correctly - balloons fly and the player wins!
- If the guess is wrong, the player can try again (up to 3 attempts per round).


Learning Levels:
 Grade Range  Description
 K      2        Simple visual and color-based patterns like "all red", "all black", or "all hearts."
 K      3-5      Slightly harder logic such as "cards that add to 9" or "all prime numbers." 
 K      6-8      Complex patterns - multiple rules, poker combinations, or even player-vs-player mode. 

Each level looks similar so students can easily progress as they grow - keeping the interface familiar but the logic more challenging.


Technologies Used:
- Python


Project Structure:
art-dealer-game/
    docs/            SRS, design, and user guide
    src/             game source code (K-2, 3-5, 6-8)
    assets/          images, audio, icons
    tests/           test scripts
    releases/        final executable builds
    README.md        this file


How to Run:
# create a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# install dependencies
pip install -r requirements.txt

# run the game
python src/main.py


Features:
* Audio prompts and instructions for young students
* Visual feedback (balloons/confetti on success)
* Simple and fun interface with large buttons
* Teacher mode to review student attempts
* Optional 2-player mode for older students


Documentation:


Project Details:

This project is developed as part of the Software Engineering course at Lewis University under the guidance of Professor Fadi Wedyan.
The simulation aims to engage students in computational thinking through playful learning.


Team Members:

* Saiteja Mudragada
* 


Contact:

For issues or suggestions, feel free to open a GitHub issue or reach out to the team.
* Let's make learning computation fun - one card at a time!
