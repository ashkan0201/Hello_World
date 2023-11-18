from string import ascii_lowercase
from colorama import Fore, Style
from time import sleep

ascii_lowercase += " "
text = "hello world my name is ashkan"
x = ""

def print_green_text(text):
    colored_text = Fore.GREEN + text + Style.RESET_ALL
    return(colored_text)

def print_red_text(text):
    colored_text = Fore.RED + text + Style.RESET_ALL
    return(colored_text)

for i in text:
    for j in ascii_lowercase:
        if i == j:
            x+=j
            print(f"\r{print_green_text(x)}", end = '')
            sleep(0.0666)
            break
        else:
            print(f"\r{print_green_text(x)+print_red_text(j)}", end = '')
            sleep(0.0666)
