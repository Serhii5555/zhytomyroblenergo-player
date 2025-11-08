# Zhytomyroblenergo player

A video converter that prepares and displays video content in the table on Zhytomyroblenergo’s website.

## Installation
To use it you need python and ffmpeg.

### Python dependencies
```
pip install -r requirements.txt
```

### Ffmpeg installation

Windows:
```
winget install ffmpeg
```

Linux (Debian/Ubuntu):
```
sudo apt install ffmpeg
```

## How to use

Move your video file to source folder, rename it to _input.mp4_.
Run _video-converter.py_:
```
python video-converter.py
```
Launch local server:
```
python -m http.server 5050
```
Go to this link:
http://localhost:5050

And start playback by pressing ```Ctrl + Alt + M```

Have fun!