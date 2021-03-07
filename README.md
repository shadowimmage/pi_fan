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

`$ sudo cp pi_fan.service /etc/systemd/system/pi_fan.service`

4. Start the service

`$ sudo systemctl start pi_fan.service`

5. Set the service to start up on reboot

`$ sudo systemctl enable pi_fan.service`

## Uninstall

1. Disable and stop pi_fan service

```sh
$ sudo systemctl disable pi_fan.service
$ sudo systemctl stop pi_fan.service
```

2. Remove service file

`$ sudo rm /etc/systemd/system/pi_fan.service`

3. (optional) delete pi_fan directory

`$ rm -r -d /home/pi/pi_fan`

## References

- https://blog.driftking.tw/en/2019/11/Using-Raspberry-Pi-to-Control-a-PWM-Fan-and-Monitor-its-Speed/
- https://www.instructables.com/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/
- https://pinout.xyz/#
- https://raspberrypi.stackexchange.com/questions/77738/how-to-exit-a-python-daemon-cleanly
- https://www.element14.com/community/servlet/JiveServlet/downloadImage/102-92640-8-726998/GPIO-Pi4.png