info() {
  printf "%s - [INFO] %s\n" "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >&2
}

error() {
  printf "%s - [ERROR] %s\n" "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >&2
}

quit() {
  echo "$1"
}
