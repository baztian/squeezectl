# Control Logitech Media Server and Squeezebox from command line

Control Logitech Media Server and Squeezebox from command line.

## Setup

    sudo apt install python3-venv
    python3 -m venv --system-site-packages ~/squeezectl
    . ~/squeezectl/bin/activate
    pip install squeezectl
    squeezectl host port

## Usage

On the command line

    $ squeezectl host port --player=player_id arg1 arg2 --kwarg1=val1 --kwarg2=val2

## Develop

    pip install bump2version
    bumpversion patch
    git push && git push --tags
