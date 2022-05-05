import os
import sys
import webbrowser

path = 'metadata.txt'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'


def read_meta(_path):
    f = open(_path, 'r')
    _lines = f.readlines()
    f.close()
    return _lines


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(sys.executable))
    lines = read_meta(current_path + '/' + path)
    browser = None
    for num, line in enumerate(lines):
        if num == 0:
            continue

        if line.find(".") == -1:
            browser = line
            continue

        print(line)
        if browser is not None:
            webbrowser.get(using=chrome_path).open_new_tab(line.replace('\n', ''))
        else:
            webbrowser.open(line.replace('\n', ''))
