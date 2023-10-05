#!/usr/bin/python3
'''program that prints all the names defined by the compiled module'''

if __name__ == "__main__":
    import hidden_4

    module_name = dir(hidden_4)
    for name in module_name:
        if name[:2] != "__":
            print(name)
