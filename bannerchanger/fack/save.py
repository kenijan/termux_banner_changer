GNU nano 8.1                      back_up/bash.bashrc
clear
shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
PROMPT_DIRTRIM=2
PS1='\n\[\e[1;34m\]┌─[\[\e[1;31m\]\T\[\e[1;34m\]]──[\e[1;32mroot㉿kenijan\e[0m\e[1;34m]──[\e[1;33m\W\[\e[1;34m\]]──[\e[1;30m\#\[\e[1;34m]\n|\n\e[1;34m└───►\e[1;31m # \e[1;39m'
clear
cat <<EOF > banner.txt
              ##################################################
              ##                                              ##
              ##  88      a8P         db        88        88  ##
              ##  88    .88'         d88b       88        88  ##
              ##  88   88'          d8''8b      88        88  ##
              ##  88 d88           d8'  '8b     88        88  ##
              ##  8888'88.        d8YaaaaY8b    88        88  ##
              ##  88P   Y8b      d8''''''''8b   88        88  ##
              ##  88     '88.   d8'        '8b  88        88  ##
              ##  88       Y8b d8'          '8b 888888888 88  ##
              ##                                              ##
              ####  ###### HanderX #############################
EOF
cat banner.txt# | lolcat
echo ""
echo "                    [㉿] Wellcome kenijan in our terminal"| lolcat