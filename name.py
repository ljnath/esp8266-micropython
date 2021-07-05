"""
MIT License

Copyright (c) 2021 Lakhya Jyoti Nath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Micropython code to display letters in a 7-segment LED display.
Tested this code on ESP8266

Author: Lakhya Jyoti Nath
Date: 6th July 2021

7segment LED display

        A    
    o--------o
    |        | B
  F |   G    |
    o--------o
    |        | C
  E |        |
    o--------o
        D

"""
import machine
import time

# creating segment based on my pin out
A = machine.Pin(5, machine.Pin.OUT)     # GPIO5     = D1
B = machine.Pin(13, machine.Pin.OUT)    # GPIO13    = D7
C = machine.Pin(12, machine.Pin.OUT)    # GPIO12    = D6
D = machine.Pin(14, machine.Pin.OUT)    # GPIO14    = D5
E = machine.Pin(2, machine.Pin.OUT)     # GPIO2     = D4
F = machine.Pin(4, machine.Pin.OUT)     # GPIO4     = D2
G = machine.Pin(15, machine.Pin.OUT)    # GPIO15    = D8

all_segments = [A, B, C, D, E, F, G]

def get_segments(letter):
    segments = []
    if letter == 'A':
        segments = [A, B, C, E, F, G]
    elif letter == 'B':
        segments = [C, D, E, F, G]
    elif letter == 'C':
        segments = [A, D, E, F]
    elif letter == 'D':
        segments = [B, C, D, E, G]
    elif letter == 'E':
        segments = [A, D, E, F, G]
    elif letter == 'F':
        segments = [A, E, F, G]
    elif letter == 'G':
        segments = [A, C, D, E, F]
    elif letter == 'H':
        segments = [C, E, F, G]
    elif letter == 'I':
        segments = [B, C]
    elif letter == 'J':
        segments = [B, C, D, E]
    elif letter == 'K':
        segments = [B, D, E, F, G]
    elif letter == 'L':
        segments = [D, E, F]
    elif letter == 'M':
        segments = [A, C, E]
    elif letter == 'N':
        segments = [C, E, G]
    elif letter == 'O':
        segments = [C, D, E, G]
    elif letter == 'P':
        segments = [A, B, E, F, G]
    elif letter == 'Q':
        segments = [A, B, C, F, G]
    elif letter == 'R':
        segments = [E, G]
    elif letter == 'S':
        segments = [A, C, D, F, G]
    elif letter == 'T':
        segments = [D, E, F, G]
    elif letter == 'U':
        segments = [C, D, E]
    elif letter == 'V':
        segments = [B, F, G]
    elif letter == 'W':
        segments = [B, D, F]
    elif letter == 'X':
        segments = [B, C, E, F, G]
    elif letter == 'Y':
        segments = [B, C, D, F, G]
    elif letter == 'Z':
        segments = [A, B, D, E, G]
    return segments


def main():
    while True:
        word = 'abcdefghijklmnopqrstuvwxyz'
        
        # word = 'ljnath'
        
        for character in word:
            # turning off all segements
            [segment.off() for segment in all_segments]
            
            # getting all segments that needs to be lit up based on the counter value
            segments_to_lit = get_segments(character.upper())
            
            # liting up all the segments
            [segment.on() for segment in segments_to_lit]
            
            # sleeping for 1s to simulation an elapse of 1s
            time.sleep(.5)
        
if __name__ == '__main__':
    main()

