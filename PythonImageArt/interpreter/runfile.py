MAIN_INSERTION_INDEX = 12
SIZE_INSERTION_INDEX = 7

# LOAD TEMPLATE
with open("template", 'r') as tf:
    t_content = tf.readlines()
    tf.close()

# LOAD DRAW FILE FROM INPUT
with open("run.txt", 'r') as df:
    d_content = [e for e in df.readlines() if e != '\n']  # Skip blank lines

# WRITE RUN FILE
if d_content[0][:4] == "SIZE":  # Size argument
    for i in range(1, len(d_content)):  # Skip first line
        d_content[i] = "        " + d_content[i]
    t_content[SIZE_INSERTION_INDEX] = d_content[0]
    t_content.insert(MAIN_INSERTION_INDEX, d_content[1:])

else:  # No size argument
    for i in range(len(d_content)):
        d_content[i] = "        " + d_content[i]
    t_content.insert(MAIN_INSERTION_INDEX, d_content)

r_content = []
for elem in t_content:
    if type(elem) == list:
        for sub_elem in elem:
            r_content.append(sub_elem)
    else:
        r_content.append(elem)

with open("run.py", 'w') as rf:
    for line in r_content:
        rf.write(line)

# RUN RUN FILE
try:
    exec(open("run.py").read())
except Exception as e:
    print("The following error was encountered during runtime:", e)
