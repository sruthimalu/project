from method1 import meth1
from method2 import meth2
from method3 import meth3
from sklearn.ensemble import Ensemble

def training():
    e=Ensemble(meth1,meth2,meth3)
    e.model()


if __name__=="__main__":
    training()

