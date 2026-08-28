# PiPlayer

PiPlayer is a simple MP3 music player for a **Raspberry Pi Zero 1** running **Raspberry Pi OS Desktop** with a small **240×240 touchscreen/display**.

The interface is built with **Pygame**. Music playback is handled by **VLC/libVLC through python-vlc**.

## Why VLC for audio?

The original version of PiPlayer used:

- Pygame 1.9.6
- SDL 1.2.15
- `pygame.mixer.music`

This resulted in a clearly audible difference in audio quality compared with VLC Media Player. Some tracks, especially tracks with a lot of bass, produced audible crackling.

A test using `python-vlc` on the same Raspberry Pi showed that the same MP3 files could be played without quality loss and without the crackling.

PiPlayer therefore now uses:

```text
MP3
 ↓
libVLC
 ↓
ALSA
 ↓
Raspberry Pi audio output
```

Pygame remains responsible for the graphical interface.

## Main features

- MP3 playback
- Play / pause
- Previous track
- Next track
- Automatic playback of the next track
- Display track information
- Display artist
- Display album
- Display album artwork when embedded in the MP3
- Display playback position
- 240×240 interface
- Fullscreen display
- Simple GUI to keep CPU usage low on the Raspberry Pi Zero
- VLC/libVLC as the audio engine

## Hardware

The project was originally developed for:

- Raspberry Pi Zero 1
- Raspberry Pi OS Desktop
- 240×240 display
- Raspberry Pi audio output

The audio outputs used during testing is:

```text
bcm2835 Headphones
```
```text
Bluetooth Headphones and Speaker
```



## Software

### Python

PiPlayer uses Python 3.

### Pygame

Pygame is used for:

- the graphical user interface
- drawing the album artwork
- text
- buttons
- mouse/touch input
- the main application loop

The version used during testing was:

```text
pygame 1.9.6
SDL 1.2.15
```

### VLC / python-vlc

`python-vlc` is used as the Python interface for VLC/libVLC.

Install VLC and the Python binding with:

```bash
sudo apt update
sudo apt install vlc python3-vlc
```

Then check the installation with:

```bash
python3 -c "import vlc; print(vlc.__version__)"
```

## Installation

Clone or copy the project to the Raspberry Pi.

Install the required software:

```bash
sudo apt update
sudo apt install vlc python3-vlc
```

If necessary, install the Python libraries:

```bash
pip3 install pygame mutagen pillow
```

Start PiPlayer, for example, with:

```bash
python3 "/home/User/Desktop/PiPlayer/main.py"
```

If the folder path contains spaces, the complete path must be enclosed in quotation marks.

You can also escape spaces with `\`:


## Music files

The music folder is currently configured in `music.py`:

```python
MUSIC_FOLDER = "/home/User/Music"
```

All files with the `.mp3` extension are automatically detected.

The files are sorted alphabetically.

### Using a different music folder

Change the following line in `music.py`:

```python
MUSIC_FOLDER = "/home/User/Music"
```

For example:

```python
MUSIC_FOLDER = "/home/User/Music/Albums"
```

## Project structure

```text
PiPlayer/
├── main.py
├── player.py
├── music.py
├── metadata.py
├── cover.py
├── gui.py
├── splash.py
├── config.py
└── test_metadata.py
```

### `main.py`

The main application.

Responsible for:

- initializing Pygame
- loading the music list
- starting the GUI
- processing touch/mouse events
- automatically starting the next track
- running the main loop

The GUI intentionally runs at:

```python
clock.tick(1)
```

This was done to reduce CPU usage on the Raspberry Pi Zero.

### `player.py`

Contains the `MusicPlayer` class.

This class creates and controls the VLC player and handles functions such as:

- `load()`
- `play()`
- `pause()`
- `resume()`
- `stop()`
- `toggle()`
- `get_position()`

Audio playback is no longer handled by `pygame.mixer.music`.

### `music.py`

Searches for MP3 files in the configured music folder.

### `metadata.py`

Reads MP3 metadata using **Mutagen**:

- title
- artist
- album
- album artwork

The track duration is also determined here.

### `cover.py`

Loads album artwork from the MP3 and scales it to:

```text
120 × 120 pixels
```

### `gui.py`

Draws the PiPlayer interface, including:

- album artwork
- title
- artist
- album
- playback progress
- time
- previous button
- play/pause button
- next button
- exit button

### `splash.py`

Draws the PiPlayer startup screen.

### `config.py`

Contains general settings such as:

```python
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240
```

and the interface colors.

## Audio quality

Audio quality was extensively tested during development.

The same MP3 was played using:

1. VLC Media Player
2. a simple Python test using `python-vlc`
3. the original Pygame audio playback

The VLC-based solutions produced no audible quality loss and no crackling during heavy bass passages.

The original Pygame 1.9.6 audio playback produced crackling, particularly at low frequencies.

VLC is therefore now used as the PiPlayer audio engine.

## CPU usage

The graphical interface originally ran at a higher frame rate. This resulted in relatively high CPU usage on the Raspberry Pi Zero 1.

By reducing the GUI frame rate to:

```python
clock.tick(1)
```

CPU usage during normal operation was reduced to approximately **35%**.

The 1 FPS setting is therefore intentional.

## Testing

A simple VLC test can be used to verify that VLC/libVLC plays audio correctly on the system:

```python
import vlc
import time

sound_file = vlc.MediaPlayer(
    "/home/User/Music/example.mp3"
)

sound_file.play()

time.sleep(10)
```

This can be useful for checking VLC/libVLC audio playback independently of PiPlayer.

## Troubleshooting

### `ModuleNotFoundError: No module named 'vlc'`

Install:

```bash
sudo apt install python3-vlc
```

Then check:

```bash
python3 -c "import vlc; print(vlc.__version__)"
```

### `ModuleNotFoundError: No module named 'pygame'`

Install:

```bash
pip3 install pygame
```

or, depending on the Raspberry Pi OS version:

```bash
sudo apt install python3-pygame
```

### `ModuleNotFoundError: No module named 'mutagen'`

Install:

```bash
pip3 install mutagen
```

### `ModuleNotFoundError: No module named 'PIL'`

Install:

```bash
pip3 install pillow
```

### The program does not start because the path contains spaces

Use quotation marks:

```bash
python3 "/home/daan/Desktop/PiPlayer VLC/main.py"
```

### No sound

First check the available audio devices:

```bash
aplay -l
```

Then check the ALSA mixer:

```bash
amixer
```

The test system had, among others:

```text
card 0: bcm2835 HDMI 1
card 1: bcm2835 Headphones
```

Also check that the master volume is not muted.

## Future improvements

Possible future features:

- volume control through the interface
- seek/progress bar
- improved album and artist display
- playlist management
- shuffle
- repeat
- music search
- automatic startup of PiPlayer
- touchscreen optimization
- improved animations
- equalizer
- support for additional audio formats
- settings menu

## Version

**PiPlayer Version 1.0**

This version provides the foundation for a Raspberry Pi-based  music player using VLC/libVLC for reliable audio playback.

## License

This project is intended as a personal/educational Raspberry Pi project.

When distributing the project, you must mention the name of this reposetory.
