
# Show the banner using figlet and lolcat
figlet -c -f slant "kenijan" | lolcat

shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
PROMPT_DIRTRIM=2

# Custom PS1 prompt
PS1='\n\[\e[1;34m\]┌─[\[\e[1;31m\]\T\[\e[1;34m\]]──[\e[1;32mroot㉿bom\e[0m\e[1;34m]>\[\e[0m\] '

clear