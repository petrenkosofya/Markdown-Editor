answer = ''


def header():
    global answer
    level = input("Level: > ")
    while (not level.isnumeric()) or int(level) < 1 or int(level) > 6:
        print("The level should be within the range of 1 to 6")
        level = input("Level: > ")
    level = int(level)
    text = input("Text: > ")
    if len(answer) != 0:
        answer += '\n'
    answer += '#' * level + ' ' + text + '\n'
    print(answer)


def plain():
    global answer
    text = input("Text: > ")
    answer += text
    print(answer)


def bold():
    global answer
    text = input("Text: > ")
    answer += '**' + text + '**'
    print(answer)


def italic():
    global answer
    text = input("Text: > ")
    answer += '*' + text + '*'
    print(answer)


def inline_code():
    global answer
    text = input("Text: > ")
    answer += '`' + text + '`'
    print(answer)


def new_line():
    global answer
    answer += '\n'
    print(answer)


def link():
    global answer
    label = input("Label: > ")
    url = input("URL: > ")
    answer += '[' + label + '](' + url + ')'
    print(answer)


def marklist(order=False):
    global answer
    cnt = input("Number of rows: > ")
    while not cnt.isnumeric() or int(cnt) <= 0:
        print("The number of rows should be greater than zero")
        cnt = input("Number of rows: > ")
    cnt = int(cnt)
    for i in range(1, cnt + 1):
        if order:
            answer += f"{i}. "
        else:
            answer += "* "
        answer += input(f"Row #{i}: > ")
        answer += '\n'
    print(answer)


while True:
    s = input("Choose a formatter: > ")
    if s not in ["plain", "bold", "italic", "header", "link", "inline-code", "new-line", "ordered-list",
                 "unordered-list", "!help", "!done"]:
        print("Unknown formatting type or command")
    elif s == "!help":
        print("Available formatters: plain bold italic header link inline-code new-line unordered-list ordered-list")
        print("Special commands: !help !done")
    elif s == "!done":
        f = open("output.md", mode='w')
        f.write(answer)
        f.close()
        exit()
    elif s == "header":
        header()
    elif s == "plain":
        plain()
    elif s == "bold":
        bold()
    elif s == "italic":
        italic()
    elif s == "inline-code":
        inline_code()
    elif s == "new-line":
        new_line()
    elif s == "link":
        link()
    elif s == "unordered-list":
        marklist()
    elif s == "ordered-list":
        marklist(True)
