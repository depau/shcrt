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
  ```
  git clone --recursive https://github.com/Depau/shcrt.git
  ```
- If you forgot about it...
  ```
  git submodule init
  git submodule update
  ```
- Simply run the script:
  ```
  ./shcrt
  ```

## Bugs

I expect it to be full of bugs; so should you.

Please report any bugs you find on GitHub :)
