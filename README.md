# Noise Detector

## Receive notifications when a noise is detected above a threshold.

The noise detector is designed to run on a Raspberry Pi with a USB microphone. It uses Bash and Python scripts to detect noise levels above a certain threshold and trigger a notification from the [Pushover](https://pushover.net) service. The actual sound is not streamed. 

The scripts are called using a command line alias for the following:
`bash /path/to/babymonitor.sh | /path/to/monitor.py`

You may need to change the `THRESHOLD` constant so that the detector is calibrated to trigger at an appropriate noise level.  
