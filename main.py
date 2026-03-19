import curses
from curses import *
from curses import wrapper
import random
import time
import string
import math
import pygame


def start_music(k):
    pygame.mixer.init()
    pygame.mixer.music.load(k)   
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)          
def stop_music():
        pygame.mixer.music.stop()

#main game meachanics That i have to workn on right now:
#this code here is inspired by the turotiral of best beginner python project(for wpm) ;
def ascii_plasma(stdscr, duration=3, speed=0.05): #inspired by youtube video ascci art and a asciiart website
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
            if 0 <= y < max_y - 1: #subtracting one since it was crashing due to not nice dimesnsions
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

   #since we want ki hame one single role chaiye iseleye and yeah using radmom dunction
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
                dy = (y - cy) / (max_y / 2)#aaaaaaaaaaaaaaaa
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
def load_sentences(path="sentences.txt"): #loading sentences from main file
    with open(path, "r") as f:
        sentences = [line.strip() for line in f if line.strip()]
    return sentences

def pick_sentence(sentences): #picking random sentences from the main file that we have hmm..
    return random.choice(sentences)
def draw_typing_screen(stdscr, state, player):
    h, w = stdscr.getmaxyx()
    target = state["target"]
    typed  = state["typed"]

    start_y = h // 2 - 1
    start_x = 4          #small left padding ig

    for i, char in enumerate(target):
        # wrap to next line if sentence is long or it would be hochpoch here
        row = start_y + (start_x + i) // w
        col = (start_x + i) % w

        if i < len(typed):
            color = curses.color_pair(11) if typed[i] == char else curses.color_pair(12)
            stdscr.addstr(row, col, char, color)
        elif i == len(typed):
            stdscr.addstr(row, col, char,
                          curses.color_pair(13) | curses.A_UNDERLINE)
        else:
            stdscr.addstr(row, col, char,
                          curses.color_pair(13) | curses.A_DIM)

def homepage(stdscr, state,player):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()

    while True:
        stdscr.erase()

        title = "U N D E R R U N"
        stdscr.addstr(h//2 - 4, w//2 - len(title)//2,
                      title, curses.color_pair(11) | curses.A_BOLD)

        sub = "press any key to begin"
        stdscr.addstr(h//2 - 2, w//2 - len(sub)//2,
                      sub, curses.color_pair(13) | curses.A_DIM)
        quit_msg = "[ESC to exit]"
        stdscr.addstr(h//2 - 1, w//2 - len(quit_msg)//2,
              quit_msg, curses.color_pair(13) | curses.A_DIM)


        if player.get("clan"):
            clan_text = f"clan: {player['clan']}"
            stdscr.addstr(h//2, w//2 - len(clan_text)//2,
                          clan_text, curses.color_pair(13))

        if state["wpm"] > 0:
            stats = f"last wpm: {state['wpm']}  |  level: {player['level']}"
            stdscr.addstr(h//2 + 2, w//2 - len(stats)//2,
                          stats, curses.color_pair(13))

        stdscr.refresh()
        stdscr.nodelay(False)
        key = stdscr.getkey()
        #if ord(key) == 27: 
        """if ord(key) == 27:
       ^^^^^^^^
TypeError: ord() expected a character, but string of length 8 found"""
        if key == "\x1b":
            return "quit"
        return "start"


def resolve_word(state, player):
    if state["start_time"] is None:

        return "continue" #a fgurad so it t doesn't go loop or crash
    
    elapsed = time.time() - state["start_time"]
    char_count = len(state["typed"])

    state["wpm"] = round((char_count/5)/(elapsed/60)) #https://www.typingtesttool.com/learn/how-is-wpm-calculated
    errors = sum(
    1 for i, ch in enumerate(state["typed"])
    if i < len(state["target"]) and ch != state["target"][i]
)
    if errors == 0:
        if(player.get("clan") == "Fire"):
            player["xp"] += 30 + state["wpm"] // 5
        elif(player.get("clan") == "Earth"):
            player["xp"] += 10 + state["wpm"]// 5
        else:
            player["xp"] += 20 + state["wpm"]//5


    else:
        if (player.get("clan") == "Fire"):
            damage = errors * 15
        elif(player.get("clan") == "Earth"):
            damage = errors*5
        else:
            damage = errors*7

        player["hp"] -= damage
        if player["hp"] <= 0:
            player["hp"] = 0
            return "dead"



    return "continue"



def game_loop(stdscr, state, player, sentences):
    state["target"]     = pick_sentence(sentences)
    state["typed"]      = []
    state["start_time"] = None
    
    TIME_LIMIT = 10   #since time limit for our game is 10 seconds for the first task.

    stdscr.nodelay(True)

    while True:
        stdscr.erase()
        draw_typing_screen(stdscr, state, player)

        
        if state["start_time"] is not None:
            elapsed = time.time() - state["start_time"]
            remaining = max(0, TIME_LIMIT - elapsed)

            #live wpm so you can see how cooked you are
            chars_typed = len(state["typed"])
            live_wpm = round((chars_typed / 5) / (elapsed / 60)) if elapsed > 0 else 0

            h, w = stdscr.getmaxyx()
            stdscr.addstr(2, 2,      f"WPM: {live_wpm}",          curses.color_pair(11))
            stdscr.addstr(2, w - 15, f"Time: {remaining:.1f}s",   curses.color_pair(13))

            # ── Time's up ─────────────────────────── buddy
            if remaining <= 0:
                return resolve_word(state, player)

        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except curses.error:
            continue

        if state["start_time"] is None and len(key) == 1:
            state["start_time"] = time.time() #first key and the timer go boom

        if key in ("KEY_BACKSPACE", "\x7f"):
            if state["typed"]:
                state["typed"].pop()

        elif len(key) == 1:
            if len(state["typed"]) < len(state["target"]):
                state["typed"].append(key)

        # sentence fully typed before time runs out becuase would it endd forever agar ye naho hota
        if len(state["typed"]) == len(state["target"]):
            return resolve_word(state, player)

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
    max_y , max_x = stdscr.getmaxyx()
    hp_bar = make_bar(player["hp"], player["max_hp"])
    xp_bar = make_bar(player["xp"], player["max_xp"])

    text = f"HP:{hp_bar}|XP:{xp_bar}"
    stdscr.addstr(0,0, text)

def make_bar(current, maximum , length=10):
    filled = int((current / maximum) * length) 
    empty = length - filled
    return "█" * filled + "░" * empty # making an health bar.

def main(stdscr):
    start_music("main.mp3")
    state = {
    "target":     "",
    "typed":      [],
    "start_time": None,
    "wpm":        0,
}   
    curses.start_color()   
    curses.init_pair(11, curses.COLOR_GREEN, curses.COLOR_BLACK)  #main game system for the wpm test
    curses.init_pair(12, curses.COLOR_RED,   curses.COLOR_BLACK)  
    curses.init_pair(13, curses.COLOR_WHITE, curses.COLOR_BLACK)  
    max_y, max_x = stdscr.getmaxyx()
    if max_y < 24 or max_x < 80:
        stdscr.addstr(0, 0, f"Terminal too small! Need 80x24, you have {max_x}x{max_y}")
        stdscr.addstr(1, 0, "Please resize your terminal and restart.")
        stdscr.refresh()
        stdscr.getch()
        return
    player={"hp":100, "xp":0, "max_hp":100, "max_xp":10000, "level":0, "clan":None}#right now we define it like this but after we could define in the dicotnary
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
    player["clan"] = clan
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
        matrix_rain(stdscr, duration=4, speed=0.04, density=0.7, char_set="glitch")
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
        #             
        ascii_tunnel(stdscr, duration=2.5, speed=0.08)
    sentences = load_sentences("sentences.txt")

    while True:
        result = homepage(stdscr, state, player)
        if result == "quit":
            break
        while True:
            result = game_loop(stdscr, state, player, sentences)
            if result == "dead":
               
               
               stdscr.clear()
               stdscr.addstr(max_y//2, max_x//2 - 5, "YOU DIED",
                          curses.color_pair(12) | curses.A_BOLD)
               stdscr.addstr(max_y//2 + 2, max_x//2 - 10, "press any key to try again",
                          curses.color_pair(13) | curses.A_DIM)
               stdscr.refresh()
               stdscr.getch()
            # reset hp for next round
               player["hp"] = player["max_hp"]
               break
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()
#wait i need to add the music, i would do by pygame.mixer from pygame library
    typewriter_wrap(stdscr, 5, 10, "It seems that you have had fun in your first task, or not, idk, but the system tells me that you want more, so why don't we give a all on round, where we type all our heart out.")
    stop_music()
wrapper(main)

