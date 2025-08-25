import turtle 
import random
import psycopg2 
import time



"""DB_CONFIG ={
    "dbname" = "turtle_db",
    "user"= "postgres",
    "password"= "",
    "host"= "localhost",
    "port"= "5432"
}"""

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_DURATION = 20 #Game lasts for 20 seconds
score = 0
time_left = GAME_DURATION

def save_score_to_db(player_name,final_score):

    """Connects to the PostgreSQL database and saves the score."""
    conn= None
    try:
        print("Connecting to the PostgreSQL database to save score...")
        conn= psycopg2.connect(**DB_CONFIG)
        cur= conn.cursor
        
        cur.execute("SELECT id, ovog_ner,email,utas FROM students")

        sql= INSERT 

        cur.execute(sql,(player_name, final_score))
        conn.commit()
        print(f" Score for {player_name}({final_score}) saved successfully")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f" Error while saving score:{error}")
    finally:
        if conn is not None:
            conn.close()

def get_high_score_from_db():
    """Connect"""
    conn = None
    high_score = 0
    try:
        print("Fetching high score from the database...")
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        if result and result[0] is not None:
            conn.close()
            print("Database connection close.")
        return high_score
    
def move_up():
    y = player.ycor()
    if y < SCREEN_HEIGHT/2 -20:
        player.sety(y+20)

def move_down():

def move_right():