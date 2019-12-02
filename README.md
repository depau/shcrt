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

### Arch Linux (including Arch on WSL)

AUR package: https://aur.archlinux.org/packages/shcrt-git/

### Other distributions (including WSL)

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
- `zenity`: GTK-based GUI for GNOME-base desktops, with a Windows port (see below)
- `yad`, `gtkdialog`, `xdialog`: other GTK-based GUIs for GNOME-based desktops
- `kdialog`: Qt5-based GUI for KDE or Qt-based desktops

Needless to say, unless you're using `none`, the desired GUI back-end needs to be installed.

If you're using WSL and you don't want to use a terminal-based GUI, you need an X11 server such as [VcXsrv](https://sourceforge.net/projects/vcxsrv/).
Otherwise you can use Zenity for Windows.

#### Zenity on Windows

The script includes an experimental wrapper for [native Windows Zenity](https://github.com/maravento/winzenity) on WSL.

To make it work, you need to:
- Download WinZenity: https://github.com/maravento/winzenity
- Place it somewhere in your Windows drive (i.e. `C:\Program Files\zenity.exe`)
- Add this line to your `~/.shcrtrc`:
  ```bash
  alias zenity.exe="'/mnt/c/path/to/your/zenity.exe'"
  # for example
  alias zenity.exe="'/mnt/c/Program Files/zenity.exe'"
  ```
- Notice how you need to put double quotes to take into account for the spaces in the file path.
 
### Emojis
```bash
export emojis=YOUR_CHOICE
```

Force enable/disable emojis. Emojis are enabled by default on GNU/Linux, and disabled on WSL.
If you're using a custom terminal that supports emojis you can force-enable them on Windows too.

- `auto`: always display emojis on GNU/Linux, disabled on WSL because of crappy terminal
- `yes`, `no`: force enable/disable

### Custom SecureCRT config path
```bash
export crtconfig="/path/to/your/Config"
```

Overrides default SecureCRT config paths:
- GNU/Linux: `~/.vandyke/SecureCRT/Config`
- Windows: `%APPDATA%/VanDyke/Config` (⇒ usually `/mnt/c/Users/your.user/AppData/VanDyke/Config`)

### SFTP client helper

In order to run an SFTP client, a helper script/function must be provided.
The helper needs to accept a ssh-like command line. It can be provided as a bash function or as a binary in `$PATH`.

By default, if nothing is provided the program will display an error message.

A FileZilla helper is provided and it should work on GNU/Linux and Windows on WSL.
To enable it, add the following to your `.shcrtrc`:

```bash
function sftp_client_runner {
  run_filezilla "$@";
}
```

The FileZilla helper source code can be found in `sftp_runners.sh`

### Default session action
```bash
export default_action="ask"
```

Sets an action that will always be run immediately when selecting a session.
Default is `ask`. Available options are:

- `ask`: let user pick an action from a menu
- `print`: print session details to console and exit
- `exec_ssh`: execute ssh
- `exec_sftp`: execute SFTP helper (it needs to be provided)

## Bugs

I expect it to be full of bugs; so should you.

Please report any bugs you find on GitHub :)
