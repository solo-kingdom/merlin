#!/bin/sh
cat <<EOF
MM          MM   EEEEEEEEEEEEEE   RRRRRRRRRRRRRR   LL               II   NN          NN
MMMM      MMMM   EE               RR          RR   LL               II   NNNN        NN
MM  MM  MM  MM   EE               RRRRRRRRRRRRRR   LL               II   NN  NN      NN
MM    MM    MM   EEEEEEEEEEEEEE   RRRR             LL               II   NN    NN    NN
MM          MM   EE               RR   RR          LL               II   NN      NN  NN
MM          MM   EE               RR      RR       LL               II   NN        NNNN
MM          MM   EEEEEEEEEEEEEE   RR        RRRR   LLLLLLLLLLLLLL   II   NN          NN
EOF

D_URL='http://meta.srv.wii.pub/d/merlin/merlin.tar.gz'

MERLIN_HOME="$HOME/.merlin"
MERLIN_BIN="$HOME/.merlin/bin"
PROFILE_ZSH="$HOME/.zshrc"
PROFILE_BASH="$HOME/.bash_profile"
PROFILE_BASH_RC="$HOME/.bashrc"

[ ! -e "$MERLIN_HOME" ] && mkdir -p "$MERLIN_HOME"
cd "$MERLIN_HOME" || exit
wget -c $D_URL -qO - | tar -xz
# shellcheck disable=SC2039
if [[ "$PATH" =~ "merlin" ]]; then
  echo "skip set PATH"
else
  if [ -e "$PROFILE_ZSH" ]; then
    echo "export PATH=\$PATH:$MERLIN_BIN" >>"$PROFILE_ZSH"
  fi
  if [ -e "$PROFILE_BASH" ]; then
    echo "export PATH=\$PATH:$MERLIN_BIN" >>"$PROFILE_BASH"
  fi
  if [ -e "$PROFILE_BASH_RC" ]; then
    echo "export PATH=\$PATH:$MERLIN_BIN" >>"$PROFILE_BASH_RC"
  fi
fi
