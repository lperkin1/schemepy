__author__ = 'perkins'


from scheme.parser import Parser
import scheme.processer
processer = scheme.processer.processer
import sys

def repl(f=sys.stdin, prompt='schemepy> ', of=sys.stdout):
    global parser
    parser = Parser(f)
    while True:
        sys.stdout.write(prompt)
        ast = parser.ast
        if ast:
            r = processer.process(ast)
            if r is not None and of:
                print >> of, r
        else:
            break