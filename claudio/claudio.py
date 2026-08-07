import pygame
import struct
import math

VERSION = "1.0"
# Made by SparKda
# cmi Repo : sparkda.github.io/cmi/

_initialized = False



def _init():
    global _initialized

    if not _initialized:
        pygame.mixer.init()
        _initialized = True


def init():
    _init()


def quit():
    global _initialized

    if _initialized:
        pygame.mixer.quit()
        _initialized = False



def play(filename, loops=0):
    _init()

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops)

    return True


def stop():
    _init()
    pygame.mixer.music.stop()


def pause():
    _init()
    pygame.mixer.music.pause()


def resume():
    _init()
    pygame.mixer.music.unpause()


def rewind():
    _init()
    pygame.mixer.music.rewind()


def is_playing():
    _init()
    return pygame.mixer.music.get_busy()


def volume(value):
    _init()

    value = max(0.0, min(1.0, float(value)))

    pygame.mixer.music.set_volume(value)


def set_volume(value):
    volume(value)




def sound(filename):

    _init()

    s = pygame.mixer.Sound(filename)
    s.play()

    return s


def stop_all():
    _init()

    pygame.mixer.stop()
    pygame.mixer.music.stop()



def bytebeat(expression, duration=10, sample_rate=8000, volume=0.5):


    _init()

    duration = float(duration)
    sample_rate = int(sample_rate)
    volume = max(0.0, min(1.0, float(volume)))

    total_samples = int(duration * sample_rate)

    data = bytearray()

    safe_globals = {
        "__builtins__": {},
        "math": math,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "abs": abs,
        "int": int,
        "min": min,
        "max": max
    }

    try:
        code = compile(
            expression,
            "<bytebeat>",
            "eval"
        )
    except Exception as e:
        raise ValueError(
            "Invalid ByteBeat expression: " + str(e)
        )

    for t in range(total_samples):

        try:
            value = eval(
                code,
                safe_globals,
                {
                    "t": t
                }
            )

            value = max(
                0,
                min(255, int(value))
            )

        except Exception as e:
            raise ValueError(
                "ByteBeat error at t="
                + str(t)
                + ": "
                + str(e)
            )

        # Convert 0-255 ByteBeat to signed 16-bit audio
        sample = int(
            (value - 128)
            * 256
            * volume
        )

        sample = max(
            -32768,
            min(32767, sample)
        )

        data += struct.pack(
            "<h",
            sample
        )

    s = pygame.mixer.Sound(
        buffer=bytes(data)
    )

    s.play()

    return s


def bytebeat_loop(
    expression,
    sample_rate=8000,
    volume=0.5
):


    _init()

    duration = 4

    total_samples = int(
        duration * sample_rate
    )

    data = bytearray()

    safe_globals = {
        "__builtins__": {},
        "math": math,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "abs": abs,
        "int": int,
        "min": min,
        "max": max
    }

    try:
        code = compile(
            expression,
            "<bytebeat>",
            "eval"
        )
    except Exception as e:
        raise ValueError(
            "Invalid ByteBeat expression: "
            + str(e)
        )

    for t in range(total_samples):

        value = eval(
            code,
            safe_globals,
            {
                "t": t
            }
        )

        value = max(
            0,
            min(255, int(value))
        )

        sample = int(
            (value - 128)
            * 256
            * volume
        )

        sample = max(
            -32768,
            min(32767, sample)
        )

        data += struct.pack(
            "<h",
            sample
        )

    s = pygame.mixer.Sound(
        buffer=bytes(data)
    )

    s.play(-1)

    return s



def tone(
    frequency=440,
    duration=1.0,
    volume=0.5,
    sample_rate=44100
):

    _init()

    frequency = float(frequency)
    duration = float(duration)
    volume = max(0.0, min(1.0, float(volume)))

    samples = int(
        duration * sample_rate
    )

    data = bytearray()

    for i in range(samples):

        value = math.sin(
            2
            * math.pi
            * frequency
            * i
            / sample_rate
        )

        sample = int(
            value
            * 32767
            * volume
        )

        data += struct.pack(
            "<h",
            sample
        )

    s = pygame.mixer.Sound(
        buffer=bytes(data)
    )

    s.play()

    return s


def beep(
    frequency=440,
    duration=0.2,
    volume=0.5
):
    return tone(
        frequency,
        duration,
        volume
    )