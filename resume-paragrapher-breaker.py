### I'm building out an ascii resume, in the process, I could not find a suitable tool to break sentences on whitespace at a given length, so, what is a programmer to do?
import re
test = """
My objective is to enable pragmatic and efficient software
designs, architectures and implementation solutions whatever the
environment or application domain. I achieve this with
dedication, problem solving, outstanding personal skills and a
commitment to engage an ever changing and dynamic technical
field.
"""
line = ""
count = 0
words = re.split("\\s+", test)
for w in words:
  if len(w) > 0:
    print(w)
    #print(count)
    if count + len(w) < 65:
      if len(line) > 0:
        line = line + " " + w
      else:
        line = w
      count = count + len(w)
    else:
      #print(line)
      count = 0
      line = w
     
print(line)    