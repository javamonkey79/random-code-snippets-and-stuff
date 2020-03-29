import re, sys

max_line_len = 65
if len(sys.argv) > 1:
    # assuming the user is smart enough to pass an int...
    max_line_len = int(sys.argv[1])

input = input("--> ")

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
            line = w

print(line)
