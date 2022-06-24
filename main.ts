input.onGesture(Gesture.Shake, function () {
    if (brincar >= 10) {
        brincar += -10
        basic.showLeds(`
            # # . # #
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.pause(500)
        basic.clearScreen()
    } else {
        basic.showLeds(`
            # # . . .
            # # . # #
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.pause(500)
        basic.clearScreen()
    }
})
let brincar = 0
brincar = 0
basic.forever(function () {
    if (brincar <= 50) {
        basic.pause(1000)
        brincar += 1
    } else {
        basic.showLeds(`
            . # . # .
            # # . # #
            . . . . .
            # # # # #
            . . . . .
            `)
        soundExpression.sad.playUntilDone()
        basic.showLeds(`
            . . . . .
            # # . # #
            . . . . .
            . # # # .
            # . . . #
            `)
        basic.pause(500)
    }
})
