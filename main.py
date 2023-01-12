import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()

    if snake.head.distance(food) <= 11:
        score.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.xcor() > 280:
        score.reset()
        snake.reset()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 9:
            score.reset()
            snake.reset()


screen.exitonclick()
