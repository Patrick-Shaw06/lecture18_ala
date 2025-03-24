function playHalf(note: number) {
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
}

function playQuarter(note: number) {
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
}

function playTriplet(note1: number, note2: number, note3: number) {
    music.play(music.tonePlayable(note1, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note1, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(note2, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note2, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
    music.play(music.tonePlayable(note3, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note3, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
}

function playEighth(note: number) {
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(note, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.rest(music.beat(BeatFraction.Eighth))
}

function restWhole() {
    music.rest(music.beat(BeatFraction.Breve))
}

function restHalf() {
    music.rest(music.beat(BeatFraction.Double))
}

function restQuarter() {
    music.rest(music.beat(BeatFraction.Whole))
}

function restEighth() {
    music.rest(music.beat(BeatFraction.Half))
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.setTempo(140)
    //  restWhole()
    //  restWhole()
    //  restWhole()
    restHalf()
    for (let i = 0; i < 2; i++) {
        restEighth()
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.E)
        restHalf()
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.B3)
        restHalf()
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.E)
        restQuarter()
        playEighth(Note.E)
        playEighth(Note.E)
        restEighth()
        playEighth(Note.E)
        playEighth(Note.E)
        playEighth(Note.FSharp)
        playEighth(Note.GSharp)
        playEighth(Note.FSharp)
        restEighth()
    }
    restHalf()
})
basic.forever(function on_forever() {
    basic.showLeds(`
        # # # . .
        # . . # .
        # # # . .
        # . . . .
        # . . . .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . . # . .
        . . # . .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # . . . #
        # # . . #
        # . # . #
        # . . # #
        # . . . #
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # # .
        # . . . #
        # . . . #
        # . . . #
        # # # # .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # . .
        # . . # .
        # # # . .
        # . . # .
        # . . # .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # # .
        # . . . .
        # # # . .
        # . . . .
        # # # # .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        `)
    pause(1000)
    basic.clearScreen()
    basic.showLeds(`
        # . . . #
        # # . . #
        # . # . #
        # . . # #
        # . . . #
        `)
    pause(1000)
})
