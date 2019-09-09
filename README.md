# shcrt

SecureCRT session browser for GNU/Linux and Windows Subsystem for Linux.

It should also work on macOS with some changes but YMMV.

At early stages, not heavily tested. Alpha quality.

## Features

- Browse SecureCRT sessions
- Search through them
- Parse SSH sessions and generate a OpenSSH command line
- Password is automatically copied to clipboard if found

## How to use

It should work both natively on GNU/Linux and on Windows under WSL, provided you have
`bash`, `python3`, `pycrypto` for Python3 and your favorite dialog tool
((c)`dialog` works everywhere).

- Clone it with `--recursive`
  ```bash
  git clone --recursive https://github.com/Depau/shcrt.git
  ```
- If you forgot about it...
  ```bash
  git submodule init
  git submodule update
  ```
- Simply run the script:
  ```bash
  ./shcrt
  ```
  
## Configuration

Configuration can be placed in `~/.shcrtrc`. It must be a sourceable by bash, use bash syntax.

### Custom GUI mode
```bash
export supermode=YOUR_CHOICE
```

It must be set to one of the GUI back-ends supported by [EasyBashGUI](https://github.com/BashGui/easybashgui/).

At the time of writing, supported modes are:

- `dialog`: ncurses terminal based GUI (good for WSL)
- `whiptail`: another terminal based GUI (good for WSL)
- `none`: uses internal shell-based EBG GUI, which uses `echo` and `read`
- `zenity`, `yad`, `gtkdialog`, `xdialog`: GTK-based GUIs for GNOME-based desktops
- `kdialog`: Qt5-based GUI for KDE or Qt-based desktops

Needless to say, unless you're using `none` the desired GUI back-end needs to be installed.

The script includes an experimental wrapper for [native Windows Zenity](https://github.com/kvaps/zenity-windows/) on WSL.
It displays but it doesn't actually work, probably due to Windows line endings needing to be fixed.

### Emojis
```bash
export emojis=YOUR_CHOIC
```

- `auto`: always display emojis on GNU/Linux, disabled on WSL because of crappy terminal
- `yes`, `no`: force enable/disable

## Bugs

I expect it to be full of bugs; so should you.

Please report any bugs you find on GitHub :)
