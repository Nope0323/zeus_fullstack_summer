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
        conn= psycopg2.connect(
            dbname = "turtle_db",
            user= "postgres",
            password= "",
            host= "localhost",
            port= "5432"
        )
        cur= conn.cursor
        sql1 = "SELECT id, ovog_ner,email,utas FROM students"
        cur.execute(sql1)

        sql_insert = "INSERT INTO high_score (player_name,final_score)VALUES(%s,%s)" 

        cur.execute(sql_insert,(player_name, final_score))
        conn.commit()
        print(f" Score for {player_name}({final_score}) saved successfully")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f" Error while saving score:{error}")
    finally:
        if conn is not None:
            conn.close()

# def get_high_score_from_db():
#     """Connects to the DB and retrieves the all-time high score."""
#     conn = None
#     high_score = 0 # Default high score is 0
#     try:
#         print("Fetching high score from the database...")
#         conn = psycopg2.connect(
#             dbname = "turtle_db",
#             user= "postgres",
#             password= "",
#             host= "localhost",
#             port= "5432"
#         )
#         cur = conn.cursor()
#         # TODO - SQL SELECT statement to get the maximum score
#         # 1. SQL MAX Aggregate function ашиглах эсвэл
#         sql1= SELECT MAX(score) AS max_score FROM table_name;
#         # 2. SQL Order By ашиглах
#         # Fetch the result
#         # TODO - fetchone ашиглан үр дүнг авах
#         # The result will be (None,) if the table is empty
#         if result and result[0] is not None:
#         high_score = result[0]
#         print(f"🏆 All-time high score is: {high_score}")
#         cur.close()
#         except (Exception, psycopg2.DatabaseError) as error:
#         print(f"❌ Error while fetching high score: {error}")
#         finally:
#             if conn is not None:
#                 conn.close()
#                 print("Database connection closed.")
#         return high_score

#       def move_up():
#             y = player.ycor()
#         if y < SCREEN_HEIGHT / 2 - 20:
#             player.sety(y + 20)
#         def move_down():
#             # TODO - доошоо хөдөлгөх үйлдэл
#         def move_left():
#             # TODO - зүүн тийшээ хөдөлгөх үйлдэл
#         def move_right():
#             # TODO - баруун тийшээ хөдөлгөх үйлдэл
#         def is_collision(t1, t2):
# # TODO - хоёр объектын зайг шалгах distance ашиглах
# # Хэрэв зай 20-с бага бол мөргөлдсөн гэж үзнэ  
#         def update_score():
#             score_pen.clear()
#             score_pen.write(
#             f"Score: {score} | Time: {time_left}",
#             align="center",
#             font=("Courier", 24, "normal")
#             )
#         def countdown():
#             global time_left
#             time_left -= 1
#             update_score()
#             if time_left > 0:
#             screen.ontimer(countdown, 1000)
#             else:
#             end_game()

#         def end_game():
#             """Ends the game, saves score, and displays final and high
#             scores."""
#             player.hideturtle()
#             # TODO - хоолыг нуух
#             # TODO - онооны самбарыг цэвэрлэх
#             # Display final score
#             score_pen.goto(0, 40)
#             score_pen.write(
#             f"Game Over! Final Score: {score}",
#             align="center",
#             font=("Courier", 24, "normal")
#             )
#             # Save the current player's score to the database
#             # TODO - тоглогчийн нэр болон оноог хадгалах функц дуудах
#             # Get and display the all-time high score from the database
#             high_score = # TODO - мэдээллийн сангаас хамгийн өндөр оноог авах
#             функц дуудах датаг хадгалах
#             score_pen.goto(0, -20)
#             score_pen.write(
#             f"All-Time High Score: {high_score}",
#             align="center",
#             font=("Courier", 20, "normal")
#             )
#alham5 hurtel huusan bn end !!!!!!!!!!!!!!!!!!!!!!!!!!!!