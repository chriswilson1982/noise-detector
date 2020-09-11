#!/bin/bash
trap break INT
while true; do
    arecord --device=hw:1,0 --format S16_LE --rate 44100 -d 2 /dev/shm/tmp_rec.wav ; sox -t .wav /dev/shm/tmp_rec.wav -n stat 2>&1 | grep "RMS     amplitude" | tail -c 9
done