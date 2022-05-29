# GoogleDinoBot

![me](https://github.com/Tsarevskay/GoogleDinoBot/blob/main/dino_gifs.gif?raw=true)

A bot for a mini-game with a jumping dinosaur in the Google Chrome browser. The game page opens when the internet connection is interrupted. For convenience, a website - [`chrome://dino`](chrome://dino/) was used to access the game, even if you have internet.

## Rules of the game
To jump a dinosaur, press the space bar.
After the game starts, the dinosaur will start running. To jump over the cacti, you need to press the "space bar" again.
The speed of the game will gradually increase, and it is more difficult to jump over cacti. In this version of the game, the flying dinosaurs — pterodactyls - have disappeared.
The dinosaur's name is T-Rex, which is the name of the only tyrannosaur species — Tyrannosaurus rex. Rex is Latin for king.

## The goal of the game
The goal of the game is to survive as long as possible. As the game progresses, the background color will change from light to dark and vice versa (day and night change). In the browser-embedded game, T-Rex will stop not only if the player cannot avoid the next obstacle, but also when the Internet signal is restored.

## Getting Started
1.  Clone the repository or download and unzip the zip file for this repository.
2.  Open the terminal in the folder where the project is saved and enter the command: ` $ pip install -r requirements.txt `.
3.  This code is intended for a display with a **1920 x 1080** extension. If you have other parameters, then in the [file](https://github.com/Tsarevskay/GoogleDinoBot/blob/main/play.py) you need to select the parameters in the *coord_search, x_start , x_end* and *y_search_cactus*.
4.  In the Google Chrome browser, open the [website](chrome://dino/).
5.  Run the file [play.py](https://github.com/Tsarevskay/GoogleDinoBot/blob/main/play.py) and open the window with the game, if you want to stop code execution, just press `q` on the keyboard.



## Libraries used
* pyautogui, PIL, mss - to take a screenshot (so much because I wanted to explore different libraries);
* keyboard - to interact with the keyboard;
* time - to measure the time;
* math - to round up the time;


## Bot Logic
We take a screenshot of the screen and check the specified area with the background to see if there is an obstacle in front of us or not. There are also 2 files ([screenshot_markup.py](https://github.com/Tsarevskay/GoogleDinoBot/blob/main/screenshot_markup.py) and [location.py](https://github.com/Tsarevskay/GoogleDinoBot/blob/main/location.py)) that help to output the coordinates of a given area. 
To speed up the program, we start checking the area from the end, checking the color of the pixels with the background. 
As the game time increases, the speed also increases. To solve this problem, we increase the obstacle search area by 5 pixels every second.
All sizes were revealed empirically.
