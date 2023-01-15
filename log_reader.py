# ========== Processing Log File for Increasing Readability ==========
import os


def backspace(line):
    """
    Deleting strings for each B, where B represents the Key.backspace

    Args:
        line [str]: The string that is going to be processed

    Returns:
        New line of characters with deleted letters
    """
    num_backspace = line.count('~')
    if num_backspace != 0:
        for i in range(len(line)):
            current_char = line[i]
            next_char = line[i+1]
            if next_char == '~':
                new_line = line[:i] + line[i+2:]
                return(backspace(new_line))
            if current_char == '~':
                new_line = line[i+1:]
                return(backspace(new_line))
    else:
        return line


def caps(line):
    """
    Turning letters into uppercase depending on the ~ value

    Args:
        line [str]: The string that is going to be processed

    Returns:
        New line of characters with upper case letters
    """
    new_line = ''
    capslock = 'off'
    for char in line:
        if char != '`':
            if capslock == 'on':
                try:
                    char = char.upper()
                    new_line += char
                except:
                    new_line += char
            else:
                new_line += char
        if char == '`' and capslock == 'on':
            capslock = 'off'
        elif char == '`' and capslock == 'off':
            capslock = 'on'
    return new_line


def createP(log_file):
    P = []
    for line in log_file:
        if 'INFO' in line and len(line) == 47 or len(line) == 48:
            P.append(1)
        else:
            P.append(0)
    P_copy = P.copy()
    for i in range(len(P)-2):
        f_char, s_char, t_char = P[i:i+3]
        if (f_char, s_char, t_char) == (1, 1, 1):
            P_copy[i+1] = -1
    return P_copy


logPATH = os.environ['appdata'] + r'\log.txt'
new_logPATH = os.environ['appdata'] + r'\log_readable.txt'


with open(logPATH, 'r') as log_file:
    P_copy = createP(log_file)
    log_file.close()


with open(logPATH, 'r') as log_file:
    with open(new_logPATH, 'w') as new_log_file:
        ind = 0
        for line in log_file:
            if P_copy[ind] != -1:
                new_log_file.write(backspace(caps(line)))
            ind += 1


log_file.close()
new_log_file.close()
