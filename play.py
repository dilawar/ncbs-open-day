#!/usr/bin/env python
import sys
import os
import subprocess
import time

def play(n, delay=0.05):
    wavfile = os.path.join( 'wav', '%s.wav' % n.lower() )
    subprocess.Popen( [ 'aplay', '-q', wavfile ] )
    time.sleep(delay)

if len(sys.argv) == 2:
    play( sys.argv[1] )
else:
    for n in sys.argv[1:]:
        if n != '+':
            play( n, 0.5 )
        else:
            time.sleep(0.5)
