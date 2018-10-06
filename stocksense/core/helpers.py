from pyfiglet import figlet_format

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def log(string, color, font="slant", figlet=False, on_color=None):
    if colored:
        if not figlet:
            if on_color:
                print(colored(string, color, on_color))
            else:
                print(colored(string, color))
        else:
            if on_color:
                print(
                    colored(figlet_format(string, font=font), color, on_color))
            else:
                print(colored(figlet_format(string, font=font), color))
    else:
        print(string)
