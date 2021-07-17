# Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(6):
    hurdle()
        
# Hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
        hurdle()
        
# Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
        
# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
        