# A simple terminal game

## Controls

| Key   | Action     |
| ----- | ---------- |
| w     | slow down  |
| s     | speed up   |
| UP    | move up    |
| DOWN  | move down  |
| LEFT  | move left  |
| RIGHT | move right |
| SPACE | stop       |



To select how much brake you want on use the number keys. 
1 is the smallest amount of brake and 9 is the highest amount of brake.

Top tip:

If you want to 'get high points' in this game then you can go into the code and take away the # infront of the code that says:

elif ch == 27:
    score = score + 1749

For some of you, you may have figured out what this will do.
If not, it will allow you to increase the score amount by 1749 every time you press the escape button (Button 27).
