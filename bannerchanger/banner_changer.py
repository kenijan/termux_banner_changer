import subprocess as sub
import os

# ANSI color codes for dark colors
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE ='\033[37m'
name = 'Kenijan'

def title_banner():
    # Clear the Termux window
    sub.run('clear', shell=True)

    # Get the terminal width using tput
    columns = int(sub.check_output('tput cols', shell=True).decode().strip())

    # Define the ASCII art
    ascii_art = """
██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
--------------------------------[Ternet㉿Changer]---
    """
    # Print the banner
    # Split the ASCII art into lines
    lines = ascii_art.strip().split('\n')

    # Center each line individually
    centered_art = '\n'.join([line.center(columns) for line in lines])
    # Run the command to display the centered ASCII art with lolcat
    sub.run(f"echo \"\n{centered_art}\" | lolcat", shell=True)
    command = f"figlet -c -f term 'Ather ㉿{name}' | lolcat"
    sub.run(command, shell=True)

# Define the global variables
# Define source and backup paths
source_file = '/data/data/com.termux/files/usr/etc/bash.bashrc'
backup_dir = '/data/data/com.termux/files/usr/etc/back_up/'
backup_file = backup_dir + 'bash.bashrc'  # Backup file path

def backup():
        try:
            # Ensure the backup directory exists
            sub.run(f'mkdir -p {backup_dir}', shell=True, check=True)

            # Remove the existing backup file in the backup directory if it exists
            sub.run(f'rm -f {backup_file}', shell=True, check=True)

            # Check if the source file exists
            sub.run(f'[ -f {source_file} ]', shell=True, check=True)

            # Copy the file to the backup directory
            sub.run(f'cp {source_file} {backup_dir}', shell=True, check=True)

            # List the contents of the backup directory
            output_ls = sub.check_output(f'ls {backup_dir}', shell=True, text=True)
            if 'bash.bashrc' in output_ls:
                print(f"{CYAN}\n  Successfully added backup file to {WHITE}\n  {backup_dir}")
            else:
                print(f"{RED}\n  Something went wrong. Check the directory: \n  {backup_dir}{WHITE}")

        except sub.CalledProcessError as e:
            print(f"{RED}\n  An error occurred: {e}{WHITE}")

def reset_banner():
  
  print(f"{YELLOW}  The reset will work only if a backup file has been saved first.{WHITE}")
  out_opt = input(f"{BLUE}\n  You already save (y/n) : {WHITE}").strip().lower()

  if out_opt == 'y':
    try:
      # Remove the current source file
      sub.run(f'rm -f {source_file}', shell=True, check=True)

      # Copy the backup file to the original source file path
      sub.run(f'cp {backup_file} {source_file}', shell=True, check=True)
      print(f"{GREEN}\n  Successfully reset to back up banner.{WHITE}")
    except sub.CalledProcessError as e:
      print(f"{RED}\n  An error occurred: {e}{WHITE}")

  elif out_opt == 'n':
    return

  else:
    print(f"{RED}  Invalid input. Please enter 'y' or 'n'.{WHITE}")
    return

def add_banner():

    def check_pkg():
        def check_and_install_package(package_name, install_command):
            try:
                # Check if the package is installed
                result = sub.run(['pkg', 'list-installed', package_name], capture_output=True, text=True)

                if result.returncode == 0 and package_name in result.stdout:
                    print(f"{GREEN}  {package_name} is already installed.{WHITE}")
                else:
                    print(f"{YELLOW}  {package_name} is not installed. Installing now...{WHITE}")
                    # Suppress the output of the installation process
                    install_result = sub.run(install_command, shell=True, stdout=sub.DEVNULL, stderr=sub.DEVNULL)
                    if install_result.returncode == 0:
                        print(f"{GREEN}  {package_name} installed successfully.{WHITE}")
                    else:
                        print(f"{RED}  Failed to install {package_name}.{WHITE}")
            except Exception as e:
                print(f"{RED}  An error occurred: {e}{WHITE}")

        # Check and install Ruby
        check_and_install_package('ruby', 'pkg install ruby')
        # Check and install lolcat
        check_and_install_package('lolcat', 'gem install lolcat')
        # Check and install figlet
        check_and_install_package('figlet', 'pkg install figlet -y')

    check_pkg()
    
    def get_fonts():
       # Get the directory of Figlet fonts
       font_dir = sub.check_output('figlet -I2', shell=True, text=True).strip()
       # List all font files in the directory
       font_files = sub.check_output(f'ls {font_dir}/*.flf', shell=True, text=True).splitlines()
       # Extract font names by removing the directory path and extension
       fonts = [font.split('/')[-1].replace('.flf', '')   for font in font_files]
       return fonts

    def display_all_fonts(name, fonts):
       # Display the name using all available fonts
       for index, font in enumerate(fonts, start=1):
          print(f"\n  {BLUE}[{index}]{WHITE}. Using font: {font}{WHITE}")
          sub.run(f'figlet -f {font} "{name}"', shell=True)

    def display_selected_font_with_lolcat(banner_name, font,user_name):
       # The new content to add to the bash.bashrc file
       new_bashrc_content = f"""

shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth
PROMPT_DIRTRIM=2

# Custom PS1 prompt
PS1='\n\[\e[1;32m\]┌───(\[\e[1;34m\]root㉿{user_name}\[\e[0m\]\[\e[1;32m\])-[\[\e[0m\[\e[1;37m\]\w\[\e[0m\]\[\e[1;32m\]]\n|\n\[\e[1;32m\]└───\[\e[1;34m\]$ \[\e[1;39m\]'

clear
# Show the banner using figlet and lolcat
figlet -c -f {font} "{banner_name}" | lolcat
"""

       # Path to save the new bash.bashrc file
       bashrc_path = "/data/data/com.termux/files/usr/etc/bash.bashrc"

       # Use subprocess to create or overwrite the bash.bashrc file
       with open(bashrc_path, 'w') as file:
            file.write(new_bashrc_content)
        
    def main_figlet():
       # Get the user's name
       banner_name = input(f"\n  {BLUE}Enter your title of banner: {WHITE}")
       user_name = input(f"\n  {BLUE}Enter your name: {WHITE}")

       # Get the list of fonts
       fonts = get_fonts()

       # Display the name in all fonts
       display_all_fonts(banner_name, fonts)

        # Prompt the user to select a font by number
       while True:
        try:
            selected_number = int(input(f"\n  {BLUE}  Enter the number of the font you want to use with banner: {WHITE}"))
            if 1 <= selected_number <= len(fonts):
                selected_font = fonts[selected_number - 1]  # Get the selected font name
                print(f"\n  {GREEN}you selected successfully {WHITE}")
                break
            else:
                print(f"{YELLOW}  Please enter a number between 1 and {len(fonts)}.{WHITE}")
        except ValueError:
            print(f"{RED}  Invalid input. Please enter a valid number.{WHITE}")

        # Display the name using the selected font with lolcat
       sub.run(f'figlet -c -f {selected_font} "{banner_name}" | lolcat', shell=True)
       display_selected_font_with_lolcat(banner_name, selected_font,user_name)

    main_figlet()

#option menu create main()
def main():

  title_banner()

  while True:
    
    print(f"{GREEN}\n   1. Add banner{WHITE}")
    print(f"{GREEN}   2. Backup{WHITE}")
    print(f"{GREEN}   3. Reset to Default{WHITE}")
    print(f"{GREEN}   4. Exit{WHITE}")

    choice = input(f"{BLUE}\n  Enter your choice: {WHITE}")

    if choice == "1":
      add_banner()
    elif choice == "2":
      backup()
    elif choice == "3":
      reset_banner()
    elif choice == "4":
      print(f"{YELLOW}\n  Exiting...{WHITE}")
      break
    else:
      print(f"{RED}\n  Invalid choice. Please try again.{WHITE}")
      return

main()
# Forcefully kill the Termux process
os.kill(os.getppid(), 9)
