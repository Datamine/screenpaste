# screenpaste
Screenshot Pasting Utility for the Terminal

## What is the Motivation for Screenpaste?

When taking screenshots, most operating systems have two modes:

1. Take a screenshot and auto-save it under a timestamped name to a predetermined folder, like `Desktop/Screenshot 2024-01-30 at 9.02.51 PM.png`.
2. Take a screenshot and copy it to the clipboard, so you can open up a simple image editor and then save it to a place you like.

Both of these are inconvenient. If I want to take a quick screenshot for a project, I probably want it saved to a specific folder under a specific name.
I don't want to have to find it and move it, or wait ten seconds for an image editing program to open.

## What is Screenpaste?

The solution is screenpaste. Screenpaste is a command-line utility that will take the content from your image clipboard, and then save it to a name you specified, like this:

```
screenpaste foo
```

Will take the image in your clipboard, and then save it in your current directory as `foo.png`. Amazing!

## Setup

1. Don't make a virtualenv or pipenv for this. You want a global installation.
2. `pip install -r requirements.txt`
3. Edit your terminal profile (in my case, `~/.bashrc`) to include a function to run this script:
```
    scrp() {
        python3 ~/.screenpaste/script.py "$1";
    }
```
4. Reload your bash profile (e.g. `source ~/.bashrc`).

## Supported Environments

I've only tested this on OS X so far. I'll update the script as necessary for other operating systems.
