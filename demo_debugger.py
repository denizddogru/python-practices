import json
"""
# JSON is text, written with JavaScript object notation.
# often used when data is sent from a server to a web page


# we can insert breakpoints
which is the flexible and newer version of debugging

# three main python debugger commands:
1: next
2: step (step into the next line)
3: continue

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
    import pdb; pdb.set_trace()
    """Entrypoint to application."""

    sample_dict = path_to_dict('sample.json')
    print_values(sample_dict)

if __name__ == '__main__':
    main()