#!/bin/bash
trap break INT
while true; do
    arecord --device=hw:1,0 --format S16_LE --rate 44100 -d 2 |
        sox -t .wav - -n stat 2>&1 |
        grep "RMS *amplitude" |
        cut -d: -f2
done
