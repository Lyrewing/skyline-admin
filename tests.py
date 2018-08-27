from cmd import Cmd


def test_add():
    assert 3 * 4 == 12


class Cli(Cmd):
    def __init__(self):
        Cmd.__init__(self)

    def do_hello(self, line):
        print("hello" + line)


def test_cmd():
    cli = Cli()
    try:
        cli.cmdloop()
    except:
        exit()


test_cmd()
