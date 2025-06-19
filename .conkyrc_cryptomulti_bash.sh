#!/bin/bash

HOMENAME = "$HOME"
FLAG_FILE="$HOMENAME/.conky/multicrypto/-conky_user_data.flag"
CONKY_CONFIG="/home/hiro/.conkyrc_cryptomulti"

cleanup() {
    echo "Executing cleanup..."
    if [ -f "$FLAG_FILE" ]; then
        echo "Conky killed. Removing $FLAG_FILE"
        rm -f "$FLAG_FILE"
    else
        echo "Flag file not found."
    fi
}

trap cleanup EXIT

# Load Conky (this time not in background)
conky -c "$CONKY_CONFIG" &
LAUNCHER_PID=$!
echo "Conky loaded with process PID: $LAUNCHER_PID"

# Get real Conky PID (if daemonizzed)
sleep 1  # Give time to Conky to start
CONKY_PID=$(pgrep -f "conky.*$CONKY_CONFIG")

if [ -z "$CONKY_PID" ]; then
    echo "Error: impossible to find Conky process."
    exit 1
fi

echo "Real Conky in execution with PID: $CONKY_PID"

# Polling every 2 seconds till exists
while kill -0 "$CONKY_PID" 2>/dev/null; do
    sleep 2
done

# Automatic cleanup thanks to trap
