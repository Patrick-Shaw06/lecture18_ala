def playHalf(note):
    music.play(music.tone_playable(note, music.beat(BeatFraction.WHOLE)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note, music.beat(BeatFraction.EIGHTH)), music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))

def playQuarter(note):
    music.play(music.tone_playable(note, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note, music.beat(BeatFraction.EIGHTH)), music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))

def playTriplet(note1, note2, note3):
    music.play(music.tone_playable(note1, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note1, music.beat(BeatFraction.EIGHTH)), music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(note2, music.beat(BeatFraction.HALF)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note2, music.beat(BeatFraction.EIGHTH)), music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play(music.tone_playable(note3, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note3, music.beat(BeatFraction.EIGHTH)), music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))

def playEighth(note):
    music.play(music.tone_playable(note, music.beat(BeatFraction.QUARTER)), music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(note, music.beat(BeatFraction.EIGHTH)), music.PlaybackMode.UNTIL_DONE)
    music.rest(music.beat(BeatFraction.EIGHTH))

def restWhole():
    music.rest(music.beat(BeatFraction.BREVE))

def restHalf():
    music.rest(music.beat(BeatFraction.DOUBLE))

def restQuarter():
    music.rest(music.beat(BeatFraction.WHOLE))

def restEighth():
    music.rest(music.beat(BeatFraction.HALF))

def on_button_pressed_a():
    music.set_tempo(140)
    
    # restWhole()
    # restWhole()
    # restWhole()
    restHalf()
    for i in range(2):
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
        playEighth(Note.FSHARP)
        playEighth(Note.GSHARP)
        playEighth(Note.FSHARP)
        restEighth()
    restHalf()


input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_leds("""
        # # # . .
        # . . # .
        # # # . .
        # . . . .
        # . . . .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . . # . .
        . . # . .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # . . . #
        # # . . #
        # . # . #
        # . . # #
        # . . . #
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # # .
        # . . . #
        # . . . #
        # . . . #
        # # # # .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # . .
        # . . # .
        # # # . .
        # . . # .
        # . . # .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # # .
        # . . . .
        # # # . .
        # . . . .
        # # # # .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # # # # #
        . . # . .
        . . # . .
        . . # . .
        # # # # #
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        # . . . #
        . # # # .
        """)
    pause(1000)
    basic.clear_screen()
    basic.show_leds("""
        # . . . #
        # # . . #
        # . # . #
        # . . # #
        # . . . #
        """)
    pause(1000)
basic.forever(on_forever)
