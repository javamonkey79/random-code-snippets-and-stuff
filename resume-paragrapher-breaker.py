import re, sys

max_line_len = 65
if len(sys.argv) > 1:
    # assuming the user is smart enough to pass an int...
    max_line_len = int(sys.argv[1])

input = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
if len(sys.argv) > 2:
    input = sys.argv[2]

line = ""
words = re.split("\\s+", input)
for w in words:
    if len(w) > 0:
        # 1 accounting for space
        if len(line) + len(w) + 1 < max_line_len:
            if len(line) > 0:
                line = line + " " + w
            else:
                line = w
        else:
            print(line)
            count = 0
            line = w

print(line)
