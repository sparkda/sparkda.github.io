VERSION = "1.0"

# Made by SparKda
# cmi Repo : sparkda.github.io/cmi/

import webbrowser


_title = "Clex Browser"
_current_url = ""


def create(title="Clex Browser"):
    global _title

    _title = title

    return True



def goto(url):
    global _current_url

    _current_url = url

    webbrowser.open(url)



def show():
    return True



def back():
    return False



def forward():
    return False



def refresh():
    if _current_url:
        webbrowser.open(_current_url)



def get_url():
    return _current_url



def open_tab(url):
    global _current_url

    _current_url = url

    webbrowser.open_new_tab(url)