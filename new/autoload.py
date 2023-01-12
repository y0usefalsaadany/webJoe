
import sys


def autoload(class_name):
    sys.path.insert(0, 'data-sploit')
    import class_name
    class_name()

print (autoload('Run.py'))
