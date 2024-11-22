# CozyLights

A command-line tool to control WiZ smart lights on your local network.

## Features

- Discover WiZ lights on your network
- Control individual lights by IP address or all lights at once
- Turn lights on/off
- Adjust brightness levels
- Set special scenes like fireplace mode

## Installation

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install cozylights
poetry add cozylights
```

## Usage

### Discover Lights
Find all WiZ lights on your network:
```bash
cozylights discover
```

### Basic Controls

Turn lights on/off:
```bash
# Turn all lights on
cozylights on

# Turn specific light on
cozylights on --ip 192.168.1.100

# Turn all lights off
cozylights off

# Turn specific light off
cozylights off --ip 192.168.1.100
```

### Brightness Control

Adjust brightness (0-255):
```bash
# Set all lights to 50% brightness
cozylights brightness 128

# Set specific light brightness
cozylights brightness 128 --ip 192.168.1.100
```

### Scene Control

Set special scenes:
```bash
# Set fireplace mode
cozylights fireplace

# Set fireplace for specific light
cozylights fireplace --ip 192.168.1.100
```

## License

MIT License
