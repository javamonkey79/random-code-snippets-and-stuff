import re
input = """
My objective is to enable pragmatic and efficient software
designs, architectures and implementation solutions whatever the
environment or application domain. I achieve this with 
dedication, problem solving, outstanding personal skills and a 
commitment to engage an ever changing and dynamic technical 
field.
"""
line = ""

words = re.split("\\s+", input)
for w in words:
    if len(w) > 0:
        if len(line) + len(w) < 65:
            if len(line) > 0:
                line = line + " " + w
            else:
                line = w
        else:
            print(line)
            count = 0
            line = w

print(line)
