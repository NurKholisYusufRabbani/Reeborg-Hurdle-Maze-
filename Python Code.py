from library import kanan_kosong

turn_left()

while not at_goal():  
    if right_is_clear():
        kanan_kosong()
        if front_is_clear():
            move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()