import math as m
import unittest as ut
import newton_raphson as nr

class Test(ut.TestCase):
    def test(self):
       
        dfx = lambda  x: -2*x*(m.e**(-x**2))-2
        fx  = lambda  x: (m.e**(-x**2))-2*x+1
   
        X,Y,Z =  nr.newton_raphson(2,0.001,fx,dfx)
        self.assertEqual(X,0.7744627493872464)
        self.assertEqual(Y,1.8561324865995488e-07)

if __name__ == "__main__":
    ut.main()