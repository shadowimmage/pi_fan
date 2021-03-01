# pi_fan

Python Service on a Raspberry Pi to control a Fan using a transistor circuit.


## Requirements

- python3
- python3-rpi.gpio (via apt)
- git (optional)

## Install

1. Clone repository to user home (`/home/pi/`).
2. cd to repository folder (`cd pi_fan`)
3. Copy the service file to `/etc/systemd/system`:

> `$ sudo cp pi_fan.service /etc/systemd/system/pi_fan.service`

4. Start the service

> `$ sudo systemctl start pi_fan.service`

## References

https://blog.driftking.tw/en/2019/11/Using-Raspberry-Pi-to-Control-a-PWM-Fan-and-Monitor-its-Speed/
https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/
https://pinout.xyz/#
