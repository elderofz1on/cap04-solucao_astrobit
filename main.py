def on_gesture_shake():
    global brincar
    if brincar >= 10:
        brincar += -10
        basic.show_leds("""
            # # . # #
                        # # . # #
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        basic.pause(500)
        basic.clear_screen()
    else:
        basic.show_leds("""
            # # . . .
                        # # . # #
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        basic.pause(500)
        basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

brincar = 0
brincar = 0

def on_forever():
    global brincar
    if brincar <= 50:
        basic.pause(1000)
        brincar += 1
    else:
        basic.show_leds("""
            . # . # .
                        # # . # #
                        . . . . .
                        # # # # #
                        . . . . .
        """)
        soundExpression.sad.play_until_done()
        basic.show_leds("""
            . . . . .
                        # # . # #
                        . . . . .
                        . # # # .
                        # . . . #
        """)
        basic.pause(500)
basic.forever(on_forever)
