# 樱花树

import random
import turtle

Jess = turtle.Turtle()
Jess.hideturtle()
Jess.left(90)
Jess.penup()
Jess.goto(0, -100)
Jess.pendown()


# “画树”函数
# 参数分别是树枝长度、画笔
def tree(branchLen, t):
    if (branchLen > 3):
        if (8 <= branchLen and branchLen <= 12) :
            if (random.randint(0, 2) == 0) :
                Jess.pencolor('snow')
            else :
                Jess.pencolor('lightcoral')
            Jess.pensize((branchLen / 3))
        elif (branchLen < 8) :
            if (random.randint(0, 1) == 0) :
                Jess.pencolor('snow')
            else :
                Jess.pencolor('lightcoral')
            Jess.pensize((branchLen / 2))
        else :
            Jess.pencolor('sienna')
            Jess.pensize((branchLen / 10))
        Jess.forward(branchLen)
        a = (1.5 * (random.random()))
        Jess.right((20 * a))
        b = (1.5 * (random.random()))
        # 在tree函数内部调自己，这种方式叫递归调用
        # 递归可以大幅提升编程效率
        tree(branchLen - 10 * b, t)
        Jess.left((40 * a))
        tree(branchLen - 10 * b, t)
        Jess.right((20 * a))
        Jess.penup()
        Jess.backward(branchLen)
        Jess.pendown()

# 绘制树下花瓣，参数分别是画板数、画笔

def petal(m, t):
    for i in range(m):
        a = (200 - 400 * (random.random()))
        b = (10 - 20 * (random.random()))
        Jess.penup()
        Jess.forward(b)
        Jess.left(90)
        Jess.forward(a)
        Jess.pendown()
        Jess.pencolor('lightcoral')
        Jess.circle(1)
        Jess.penup()
        Jess.backward(a)
        Jess.right(90)
        Jess.backward(b)

def main():
    Jess = turtle.Turtle()
    Jess.hideturtle()
    Jess.speed(0)
    Jess.goto(0, 0)
    Jess.penup()
    Jess.backward(150)
    Jess.pendown()
    Jess.pencolor('sienna')
    tree(60, Jess)
    petal(100, Jess)
    turtle.done()

main()
