# move_cursor_using_fingers

Allows you to move your cursor and click (or hold) your Left Mouse Button using your fingers.

The cursor jumps like crazy because mediapipe's hand recognition isn't stable, so it's more about fun than practical use. (Also it works pretty bad overall, sometimes losing your hand or becoming "blind" for some time.)


## How to launch

**YOU NEED <ins>64-BIT</ins> PYTHON 3.7+!!!**

Install the dependencies using `pip install -r requirements.txt`, then just run the code by double-clicking the file or running `python move_cursor_using_fingers.py` in your console


## How to move your cursor

Bring the end of your thumb to the end of your index finger (as if making an "ok" sign) and move your hand.

If you want to hold LMB, bring the end of your thumb to the end of your middle finger.

If you want to unhold LMB, stop doing the thing mentioned above.

Rules mentioned above can work together, but they are working bad, maybe because it's hard for mediapipe to distinguish two fingers that are close, I'm too lazy to check. Also mediapipe sometimes thinks that strange looking hand isn't a hand and can't recognize it.

If it doesn't work, try to increase `MINIMUM_DISTANCE_BETWEEN_FINGERS` in `move_cursor_using_fingers.py`.

If it works even when fingers are far from each other, try to decrease the variable mentioned above.

To change the cursor's speed, change `CURSOR_MOVEMENT_MULTIPLIER` variable.

Currently this program supports one hand and this is enough, I think. By the way, mediapipe has some troubles handling two hands.

It works offline btw
