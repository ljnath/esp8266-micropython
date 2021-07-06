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


Micropython code to display counter from 0 to 9 in a 7-segment LED display.
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

ALL_SEGMENTS = (A, B, C, D, E, F, G)

DIGITS = {
    0 : (A, B, C, D, E, F),
    1 : (B, C),
    2 : (A, B,  D, E, G),
    3 : (A, B, C, D, G),
    4 : (B, C, F, G),
    5 : (A, C, D, F, G),
    6 : (A, C, D, E, F, G),
    7 : (A, B, C),
    8 : (A, B, C, D, E, F, G),
    9 : (A, B, C, D, F, G)
}

def main():
    counter = 0
    while True:
        
        # turning off all segements
        [segment.off() for segment in ALL_SEGMENTS]
        
        # getting all segments that needs to be lit up based on the counter value
        segments_to_lit = DIGITS[counter]
        
        # liting up all the segments
        [segment.on() for segment in segments_to_lit]
        
        # increasing counter value
        counter += 1
        
        # resetting counter if counter is greater then 10 as it cannot be displayed in a single 7segment LCD display
        if counter >= 10:
            counter = 0
        
        # sleeping for 1s to simulation an elapse of 1s
        time.sleep(1)
        
if __name__ == '__main__':
    main()
        
    
    
    



