import curses
from curses import *
from curses import wrapper
import random
import time
import string
import math

#main game meachanics That i have to workn on right now:
#this code here is inspired by the turotiral of best beginner python project ;D


def ascii_plasma(stdscr, duration=3, speed=0.05):
    max_y, max_x = stdscr.getmaxyx()
    curses.start_color()
    # Define color pairs for plasma
    curses.init_pair(5, curses.COLOR_RED,     curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW,  curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_GREEN,   curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_CYAN,    curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_BLUE,    curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    color_pairs = [5, 6, 7, 8, 9, 10]
    chars = " .:;+*#@░▒▓█"

    t = 0
    end_time = time.time() + duration
    while time.time() < end_time:
        for y in range(max_y - 1):
            for x in range(max_x - 1):
                # Plasma formula — overlapping sine waves
                value = (
                    math.sin(x / 3.0 + t) +
                    math.sin(y / 3.0 + t) +
                    math.sin((x + y) / 6.0 + t) +
                    math.sin(math.sqrt(x*x + y*y) / 4.0)
                )
                # Normalize -4..4 → 0..1
                norm = (value + 4) / 8.0
                char_idx  = int(norm * (len(chars) - 1))
                color_idx = int(norm * (len(color_pairs) - 1))

                try:
                    stdscr.addstr(y, x, chars[char_idx],
                                  curses.color_pair(color_pairs[color_idx]))
                except:
                    pass

        stdscr.refresh()
        time.sleep(speed)
        t += 0.15  # controls animation speed
    stdscr.clear()
def matrix_rain(stdscr, duration = 3, speed = 0.05, density = 1, char_set = "matrix"):
    max_y, max_x = stdscr.getmaxyx()
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    sets = {
        "matrix":  "abcdefghijklmnopqrstuvwxyz01234567890@#$%",
        "binary":  "01",
        "symbols": "@#$%&*!?><[]{}",
        "glitch":  "アイウエオカキクケコ01@#$"  #i love japanese lol 
    }

    chars = sets.get(char_set, sets["matrix"])
    active_cols = random.sample(range(max_x - 1), int((max_x - 1) * density)) 
    cols = {x: random.randint(0, max_y) for x in active_cols}

    end_time = time.time() + duration
    while time.time() < end_time:
        for x,y in cols.items():
            char = random.choice(chars)
            if 0 <= y < max_y - 1:
                stdscr.addstr(y, x, char, curses.color_pair(3) | curses.A_BOLD)
            if 0 <= y - 1 < max_y - 1:
                stdscr.addstr(y - 1, x, char, curses.color_pair(2))
            if 0 <= y - 4 < max_y - 1:
                stdscr.addstr(y - 4, x, " ")
            cols[x] = (cols[x] + 1) % (max_y + 5)

        stdscr.refresh()
        time.sleep(speed)
    stdscr.clear()




def roll_clan(stdscr):
    clans = ["Fire", "Earth", "Water"]
    max_y, max_x = stdscr.getmaxyx()
    mid_y = max_y // 2
    col1, col2, col3 = max_x // 4, max_x // 2, (max_x * 3) // 4
    positions = {"Fire": col1, "Earth": col2, "Water": col3}

   #since we want ki hame one single role chaiye iseleye.
    chosen = random.choice(clans)

    stdscr.clear()
    stdscr.addstr(mid_y, col1, "Fire")
    stdscr.addstr(mid_y, col2, "Earth")
    stdscr.addstr(mid_y, col3, "Water")
    stdscr.addstr(mid_y, positions[chosen], chosen, curses.A_BOLD | curses.A_REVERSE)
    stdscr.addstr(mid_y + 2, col1, f"You got: {chosen} Clan!")
    stdscr.addstr(mid_y + 4, col1, "> Press any key to continue")
    stdscr.refresh()
    stdscr.getch()

    return chosen
def get_typed_input(stdscr, y, x):
    typed = ""
    while(True):
        key  = stdscr.getch()

        if(key == 10):
            break
        elif (key == 27):
            break
        elif(key == 263):
            typed = typed[:-1]
        else:
            typed += chr(key)

        #if the typing speed could be cacluated simulatoenly then we could think og making it to a nice game where woe could highlight in green and red the mistakes of the users
    #making this function so that we can see the typing speed in real life, but i 
    #have to work on the random generation of the sentences tpp.


def ascii_tunnel(stdscr, duration=3, speed=0.1):
    max_y, max_x = stdscr.getmaxyx()
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    
    
    rings = ["@", "#", "*", "+", ":", ".", " "]
    frame = 0
    
    end_time = time.time() + duration
    while time.time() < end_time:
        stdscr.clear()
        cy, cx = max_y // 2, max_x // 2  
        
        for y in range(max_y - 1):
            for x in range(max_x - 1):
                #elispese shape equations
                dy = (y - cy) / (max_y / 2)
                dx = (x - cx) / (max_x / 4)  # divide by 4 for wide terminal saw this in yt video
                dist = int((dy**2 + dx**2) ** 0.5 * len(rings))
                
                
                ring_idx = (dist + frame) % len(rings)
                char = rings[ring_idx]
                
                try:
                    stdscr.addstr(y, x, char, curses.color_pair(4))
                except:
                    pass
        
        stdscr.refresh()
        time.sleep(speed)
        frame += 1
    
    stdscr.clear()


def typewriter(stdscr, y, x, text, delay=0.03, color=None):
    stdscr.nodelay(True)   
    for i, char in enumerate(text):
     
        key = stdscr.getch()
        if key == 27:     
            stdscr.addstr(y, x + i, text[i:])
            stdscr.refresh()
            stdscr.nodelay(False) 
            return
        if color:
            stdscr.addstr(y, x + i, char, color)
        else:
            stdscr.addstr(y, x + i, char)
        stdscr.refresh()
        time.sleep(delay)
    stdscr.nodelay(False)  

def typewriter_wrap(stdscr, y, x, text, delay=0.03, prefix=">> "):
    max_y, max_x_screen = stdscr.getmaxyx()
    max_x = max_x_screen - x - len(prefix) - 2  
    words = text.split()
    line = ""
    lines = []
    
    for word in words:
        if len(line) + len(word) + 1 > max_x:
            lines.append(line)
            line = word
        else:
            line += (" " if line else "") + word
    if line:
        lines.append(line)
    
    stdscr.nodelay(True)
    for i, l in enumerate(lines):
        if y + i >= max_y - 1:
            break
        
        tag = prefix if i == 0 else " " * len(prefix)
        for j, char in enumerate(tag + l):
            if stdscr.getch() == 27:
                for ri, rl in enumerate(lines[i:]):
                    t = prefix if (i + ri) == 0 else " " * len(prefix)
                    stdscr.addstr(y + i + ri, x, t + rl)
                stdscr.nodelay(False)
                stdscr.refresh()
                return
            stdscr.addstr(y + i, x + j, char)
            stdscr.refresh()
            time.sleep(delay)
    stdscr.nodelay(False)



def get_name(stdscr, y, x, color = None):
    curses.echo()
    curses.curs_set(1)
    stdscr.addstr(y,x, ">")
    stdscr.refresh()
    name = stdscr.getstr(y, x+2, 20)
    curses.noecho()
    curses.curs_set(0)
    return name.decode()
"""def clan_name(stdscr, y, x, color = None):
    curses.echo()
    curses.curs_set(1)
    stdscr.addstr(y,x, ">")
    stdscr.refresh()
    name = stdscr.getstr(y, x+2, 20)
    curses.noecho()
    curses.curs_set(0)
    return name.decode()
"""  #earlier thought of using this method but i was so retarded lol
def gain_xp(player, amount):
    player["xp"] += amount
    if player["xp"] >= player["max_hp"]:
        player["xp"] =0
        player["level"] += 1
        player["max_hp"] += 10
def draw_status(stdscr , player):
    max_y = max_x = stdscr.getmaxyx()
    hp_bar = make_bar(player["hp"], player["max_hp"])
    xp_bar = make_bar(player["xp"], player["max_xp"])

    text = f"HP:{hp_bar}|XP:{xp_bar}"
    stdscr.addstr(0,0, text)

def make_bar(current, maximum , length=10):
    filled = int(current/maximum )*length
    empty = length - filled
    return "█" * filled + "░" * empty # making an health bar.

def main(stdscr):
    max_y, max_x = stdscr.getmaxyx()
    if max_y < 24 or max_x < 80:
        stdscr.addstr(0, 0, f"Terminal too small! Need 80x24, you have {max_x}x{max_y}")
        stdscr.addstr(1, 0, "Please resize your terminal and restart.")
        stdscr.refresh()
        stdscr.getch()
        return
    player={"hp":100, "xp":0, "max_hp":100, "max_xp":10000, "level":0}
    #just a simple dictonary for the player stats.
    draw_status(stdscr, player) 
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.bkgd(' ', curses.color_pair(1))

    stdscr.clear()
    draw_status(stdscr, player) 
    #now i am gonna make a typerwriter effect.
    typewriter(stdscr, 5, 10, "Welcome to the world of UnderRun, Player....")
    stdscr.addstr(7, 10, "[Press any key to continue]")
    stdscr.refresh()
    stdscr.getch()  

    stdscr.clear()
    draw_status(stdscr, player)
    typewriter(stdscr, 6, 10, "Oh so you are the chosen one, may I know your name?")
    #okay why is this bugging like why is this getting like hmm, like you know 

    player_name = get_name(stdscr, 8, 10)
    stdscr.clear()
    draw_status(stdscr, player)
    typewriter_wrap(stdscr, 5, 10, f"Welcome {player_name}, I suppose you have a clan, if not on the next screen you may role for one since they provide you with special abilities and better buff for your assisination tasks")
    stdscr.getch()
    stdscr.clear()
    draw_status(stdscr, player)
    stdscr.refresh()
    typewriter_wrap(stdscr, 5, 10,f"{player_name}, You must remember that the rolling of clan can only be done for a single time, if you quit this game now your data would be lost, and all your progress would be gone, which i don't think you want that, so good luck.")
    typewriter(stdscr, 9, 10, "There are 3 well know clans, Earth, Fire and Water")
   
   #how do i make this ???
    color= curses.color_pair(1)
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()
    draw_status(stdscr, player)
    max_y, max_x = stdscr.getmaxyx()
    mid_y = max_y//2
    col1 = max_x // 4
    col2 = max_x // 2
    col3 = (max_x * 3) // 4


    stdscr.addstr(mid_y,col1, "Fire")
    stdscr.addstr(mid_y,col2, "Earth")
    stdscr.addstr(mid_y,col3, "Water")

    stdscr.addstr(mid_y+3, col1, "> Press any button to roll your clan")
    clan = roll_clan(stdscr)
    stdscr.getch()
    typewriter_wrap(stdscr, 5, 10, f"Congratulations {player_name}, you rolled {clan}")
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()
    draw_status(stdscr, player)
    if(clan == "Fire"):
        gain_xp(player, 30)
        draw_status(stdscr, player)
        typewriter_wrap(stdscr, 5, 10, f"The fire clan, is a respectable clan since it provides you +10% buffs on your experience points and also +20% buffs on you hp bar")

        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        draw_status(stdscr, player)
        typewriter_wrap(stdscr, 5, 10, f"Here is your first task player, i recommend you to full screen this, to enjoy this experience to the fullest.")
        stdscr.getch()
        typewriter_wrap(stdscr, 8, 10 , "Now your journey begins as a ninja from a little fire village, try your best to survive these harsh 10 seconds for your first trial")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        ascii_plasma(stdscr, duration=3, speed=0.04)
        


#hmm this is acutally cool cause here we haven't actually seems this.
    elif(clan == "Earth"):
        typewriter_wrap(stdscr, 5, 10, f"You are chosen by Earth, One of the most respectable and grounded clan, this clan could increase your hp by 30% and experience points by 5%")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        draw_status(stdscr, player)
        typewriter_wrap(stdscr, 5, 10, f"{player_name}, Now you journey begins as a Earth member clan, the first task consist of a 10 second survival drill, where you neeed to survive and maximise you experience points.")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        matrix_rain(stdscr, duration=4, speed=0.04, density=0.7, char_set="binary")

       
        #after this there would be the starting effect in terminal of the user, hmm i thouhg of doing matrix but yeah we can do any :D

    else:
        typewriter_wrap(stdscr, 5, 10, f"You are chosen by Water, one of the most peaceful and loved clan, people here are overpowerful, since this clan could increase your hp by 20% and also your experience points by 10% which provides a significant balance.")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        draw_status(stdscr, player)
        typewriter_wrap(stdscr, 5, 10, f"{player_name}, Now you journey begins as a Water member clan, the first task consist of a 10 second survival drill, where you neeed to survive and maximise you experience points.")
        stdscr.refresh()
        stdscr.getch()
        stdscr.clear()
        ascii_tunnel(stdscr, duration=2.5, speed=0.08)
        
    #so usually i would be making only 3 fire water and earth a
    #so like this is being a good scenario and our game is coming.
    #writing my plan for the fire clan.
    
#now the mains game part would contain first and initial speed typing game of 10 second which is worked for an assasin and
"""as he has to speed type 
and also in his first mission he has to cool it off."""

wrapper(main)
