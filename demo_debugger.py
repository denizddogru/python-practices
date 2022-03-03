import json
"""
# JSON is text, written with JavaScript object notation.
# often used when data is sent from a server to a web page


# we can insert breakpoints
which is the flexible and newer version of debugging


# essential pdb Commands

p: print the value fo an expression
n: continue execution until the next line in the current funciton is reached
s: execute the current line and stop when the function is called
c: continue execution and only stop when a breakpoint is occurred.
h: see a list of available commands
q : quit the debugger


print
"""
# Javascript object notation,

def path_to_dict(path):
    """open file at provided path and return as dictionary."""
    with open(path) as json_file:
        json_dict = json.load(json_file)

def print_values(input_dict):
    """Loop through dict and print values."""
    for k, v in input_dict.items():
        print('{0}: {1}'.format(k, v))

def main():
    #breakpoint()
    import pdb; pdb.set_trace()
    """Entrypoint to application."""

    sample_dict = path_to_dict('sample.json')
    print_values(sample_dict)

if __name__ == '__main__':
    main()