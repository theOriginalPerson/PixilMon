# PixilMon

## Intro
Welcome to the Py-games course! Here we will develop a PixilArt Monster Battle game (PixilMon) using PixilArt and the Pygame engine. Feel free to use the <code>main.py</code> file contents to develop the game along the way if you're feeling stuck or are unsure about something.

## How to reproduce this
<ol>
    <li>Create your PixilArt graphics (i.e. battle background, player character, opponent character, lifespan bars)</li>
    <li>Start your <code>main.py</code> file by copying and pasting lines 1-13 from the <code>main.py</code> template we've provided for you in this repository</li>
    <li>Create a "screen" variable that stores the size of your window. Make sure this corresponds to your background image's size (i.e. if your background image is 2000x1500, make sure the window is a similar size)</li>
    <li>Set the caption of the game to "PixilMon"</li>
    <li>Add a clock variable so the framerate can be made using <code>pygame.time.Clock()</code></li>
    <li>Add all of your graphics (through variables) into the game using <code>pygame.image.load("insert image file path here")</code></li>
    <li>Create your font by using <code>pygame.font.Font(None, <i>insert font size integer here</i>)</code></li>
    <li>For each image, excluding the background, add a rectangle using the <code>[image variable name].get_rect(midbottom=(x_val, y_val))</code>. Make sure to use the <code>midbottom</code> command in order to grab the image from the middle bottom point and drag it according to that!</li>
    <li>Make sure to render a "You win" and "You lose" quote (as shown in lines 42-43) in the <code>main.py</code> template</li>
    <li>We want live commentary to come from our console, so make sure to create the functions that print to the console whether your player or the opponent made a hit or miss!</li>
    <li>Copy lines 98-104 in our <code>main.py</code> template. Also copy lines 150-151 and place them 1 linebreak underneath the previous lines, indented under the <code>while</code> loop</li>
    <li>Go back to where you initialized your Pygame engine and add variables indicating that a) the game is still on, b) whose turn it is to play, c) who the winner is by using booleans (True or False). Follow what your instructor says and if you're confused, simply copy lines 17-19 into your <code>main.py</code> file</li>
    <li>Create two conditions where if the game is still on (if it's True), it does something (we can just pass this for now), and if the game is NOT still on (so False), then it does something else (again, just type <code>pass</code> for this part for now)</li>
    <li>If the game is still on (in the <code>game_still_on</code> condition), use the <code>screen.blit</code> command to "blit" your graphics onto the screen according to the coordinates you've set for them (you can copy and paste your variables from before into the appropriate parameters)</li>
    <li>Add a "chance" variable that returns a random integer between 0 and 10 by using the <code>random.randint(a, b)</code> method</li>
    <li>Add another variable that holds your keys (for when a key gets pressed)</li>
    <li>Set the key you want to be pressed to the space-bar (use <code>pygame.K_SPACE</code>) for this part. If you wish to use a different key, refer to the Pygame documentation here and use the appropriate key: http://www.pygame.org/docs/ref/key.html</li>
    <li>Now add your player turn conditions (<code>if player_turn is True</code> and <code>if player_turn is False</code>). Use <code>pass</code> for both now</li>
    <li>Add a condition in the "player_turn is True" condition stating that if the chance integer is higher than 5 and the key you selected is pressed, call the <code>player_hit()</code> function, and blit your opponent's empty lifespan. If these conditions are not met, then call the <code>player_miss()</code> function and switch the turn over to the other player by flipping the boolean value of the <code>player_turn</code> variable. Don't forget to "blit" the winner quote to the screen here (from step 9)</li>
    <li>Repeat steps 18-19 but for the other player now (if the player_turn is False)</li>
    <li>Go to the condition where you made the game_still_on variable False, and add a time delay of 1000 milliseconds (or more if you wish) so the game can process what just happened and allow for the changing images to pop up</li>
    <li>Fill the screen using <code>screen.fill</code> to a different color and blit the winner's name or winning quote to the screen</li>
    <li>Run the game and if something is wrong, try to look through the steps and see where you might have slipped up. Don't worry if doesn't look like the template, all of our graphics and their positions onscreen are going to be completely unique</li>
    <li>If you made it this far without problems! Congratulations! You made your first Pygame!</li>
</ol>

## How to use it
Run the Python code, or double-click on the <code>main.py</code> file to open the game. When it loads, press the space-bar to deliver an attack, and if it lands, congratulations! You've won. If it doesn't land, you've lost.