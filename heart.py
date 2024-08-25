import turtle as t
import random

color = ("red", "orange", "blue", "green", "white", "yellow", "indigo", "pink")
t.bgcolor("black")
t.speed(0)

# 하트 그리기 함수
def draw_heart(size):
    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size * 0.5, 200)
    t.right(140)
    t.circle(size * 0.5, 200)
    t.forward(size)
    t.left(50)
    t.end_fill()

for x in range(20):
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.down()
    t.color(random.choice(color))
    heart_size = random.randint(10, 30)
    draw_heart(heart_size)
    t.right(50)  # 각 하트가 서로 다른 각도로 그려지게 회전

t.done()
