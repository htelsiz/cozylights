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

# Clone the repository
git clone https://github.com/yourusername/cozylights.git
cd cozylights

# Install dependencies
poetry install
```

## Usage

### Discover Lights
Find all WiZ lights on your network:
```bash
poetry run cozylights discover
```

### Basic Controls

Turn lights on/off:
```bash
# Turn all lights on
poetry run cozylights on

# Turn specific light on
poetry run cozylights on --ip 192.168.1.100

# Turn all lights off
poetry run cozylights off

# Turn specific light off
poetry run cozylights off --ip 192.168.1.100
```

### Brightness Control

Adjust brightness (0-255):
```bash
# Set all lights to 50% brightness
poetry run cozylights brightness 128

# Set specific light brightness
poetry run cozylights brightness 128 --ip 192.168.1.100
```

### Scene Control

Set special scenes:
```bash
# Set fireplace mode
poetry run cozylights fireplace

# Set fireplace for specific light
poetry run cozylights fireplace --ip 192.168.1.100
```

## License

MIT License
