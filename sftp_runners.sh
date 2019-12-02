function get_port_from_args {
  local next_is_port=0
  for arg in "$@"; do
    if [[ "$next_is_port" == 1 ]]; then
      echo "$arg"
      return
    elif [[ "$arg" == "-p" ]]; then
      local next_is_port=1
    elif [[ "$arg" == -p* ]]; then
      echo ${"$arg"#-p}
      return
    fi
  done
}

function get_destination_from_args {
  local next_is_port=0
  for arg in "$@"; do
    if [[ "$next_is_port" == 1 ]]; then
      continue
    elif [[ "$arg" == "-p" ]]; then
      local next_is_port=1
    elif [[ "$arg" == -p* ]]; then
      continue
    else
      echo "$arg"
      return
    fi
  done
}

function sftp_uri_from_ssh_cmd {
  local port="$(get_port_from_args "$@")"
  local dest="$(get_destination_from_args "$@")"

  if [[ "$dest" == *@* ]]; then
    local user="$(echo "$dest" | cut -d "@" -f 1)"
    local host="$(echo "$dest" | cut -d "@" -f 2)"
  else
    local user=""
    local host=""
  fi

  if [[ "$host" == *:* ]]; then
    # Host is an IPv6 address (most likely)
    local host="[$host]"
  fi

  echo -n "sftp://"

  if [[ "$user" != "" ]]; then
    echo -n "${user}@"
  fi

  echo -n "$host"

  if [[ "$port" == "" ]]; then
    echo
  else
    echo ":$port"
  fi
}

function run_filezilla {
  if is_wsl; then
    if [ -f "/mnt/c/Program Files (x86)/FileZilla FTP Client/filezilla.exe" ]; then
      local fz_cmd="/mnt/c/Program Files (x86)/FileZilla FTP Client/filezilla.exe"
    else
      local fz_cmd="/mnt/c/Program Files/FileZilla FTP Client/filezilla.exe"
    fi
  else
    local fz_cmd="filezilla"
  fi

  local uri="$(sftp_uri_from_ssh_cmd "$@")"
  echo "\$" "$fz_cmd" "$uri"
  exec "$fz_cmd" "$uri"
}
