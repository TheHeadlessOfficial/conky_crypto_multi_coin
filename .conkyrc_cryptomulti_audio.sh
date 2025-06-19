#!/bin/bash
LOCKFILE="/home/hiro/.conky/multicrypto/audio_lock.lock"

while [ -f "$LOCKFILE" ]; do
    sleep 0.2
done

touch "$LOCKFILE"
ffplay -nodisp -autoexit "$1" > /dev/null 2>&1
[ -f "$LOCKFILE" ] && rm "$LOCKFILE"
#rm "$LOCKFILE"
