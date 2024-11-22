import asyncio
from typing import Optional, List
from enum import IntEnum
import typer
from pywizlight import wizlight, PilotBuilder, discovery

class WizScenes(IntEnum):
    """Mapping of Wiz light scenes to their integer values"""
    OCEAN = 1
    ROMANCE = 2
    SUNSET = 3
    PARTY = 4
    FIREPLACE = 5
    COZY = 6
    FOREST = 7
    PASTEL = 8
    WAKE_UP = 9
    BEDTIME = 10
    WARM_WHITE = 11
    DAYLIGHT = 12
    COOL_WHITE = 13
    NIGHT_LIGHT = 15
    FOCUS = 16
    RELAX = 17
    TRUE_COLORS = 18
    TV_TIME = 19
    PLANT_GROWTH = 20
    SPRING = 21
    SUMMER = 22
    FALL = 23
    DEEP_DIVE = 24
    JUNGLE = 25
    MOJITO = 26
    CLUB = 27
    CHRISTMAS = 28
    HALLOWEEN = 29
    CANDLELIGHT = 30
    GOLDEN_WHITE = 31
    PULSE = 32
    STEAMPUNK = 33

async def discover_lights() -> List[wizlight]:
    """Find all Wiz lights on the network"""
    bulbs = await discovery.discover_lights(broadcast_space="255.255.255.255")
    return bulbs

async def cleanup_bulbs(bulbs: List[wizlight]):
    """Properly cleanup bulb connections"""
    for bulb in bulbs:
        await bulb.async_close()

app = typer.Typer(help="Control your Wiz smart lights")

@app.command()
def on(ip: Optional[str] = None):
    """Turn on all lights or a specific light by IP address"""
    async def turn_on():
        try:
            if ip:
                light = wizlight(ip)
                await light.turn_on()
                await light.async_close()
            else:
                bulbs = await discover_lights()
                for light in bulbs:
                    await light.turn_on()
                await cleanup_bulbs(bulbs)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(turn_on())

@app.command()
def off(ip: Optional[str] = None):
    """Turn off all lights or a specific light by IP address"""
    async def turn_off():
        try:
            if ip:
                light = wizlight(ip)
                await light.turn_off()
                await light.async_close()
            else:
                bulbs = await discover_lights()
                for light in bulbs:
                    await light.turn_off()
                await cleanup_bulbs(bulbs)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(turn_off())

@app.command()
def brightness(level: int = typer.Argument(..., min=0, max=255), ip: Optional[str] = None):
    """Set brightness level (0-255) for all lights or a specific light"""
    async def set_brightness():
        try:
            if ip:
                light = wizlight(ip)
                await light.turn_on(PilotBuilder(brightness=level))
                await light.async_close()
            else:
                bulbs = await discover_lights()
                for light in bulbs:
                    await light.turn_on(PilotBuilder(brightness=level))
                await cleanup_bulbs(bulbs)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(set_brightness())

@app.command()
def fireplace(ip: Optional[str] = None):
    """Set lights to fireplace scene"""
    async def set_fireplace():
        try:
            if ip:
                light = wizlight(ip)
                # First ensure the light is on
                await light.turn_on()
                # Set scene 5 for fireplace (per official pywizlight scenes.py)
                pilot = PilotBuilder(
                    scene=5,  # Fireplace scene number
                    brightness=255,  # Full brightness
                    speed=50  # Medium animation speed
                )
                await light.turn_on(pilot)
                await light.async_close()
            else:
                bulbs = await discover_lights()
                for light in bulbs:
                    await light.turn_on()
                    pilot = PilotBuilder(
                        scene=5,
                        brightness=255,
                        speed=50
                    )
                    await light.turn_on(pilot)
                await cleanup_bulbs(bulbs)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(set_fireplace())

if __name__ == "__main__":
    app()
