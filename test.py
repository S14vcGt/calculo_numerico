import math as mt
import unittest as ut
import integracion_numerica as integral
import newton_raphson as nr
import biseccion as bc
class IntegrationTest(ut.TestCase):#test de los metodos de integracion
    def test1(self):
        f = lambda x: x*(((x**2)+1)**0.5)#funcion que prueba este test

        self.assertEqual(integral.riemman(f,0,1,4), 0.4385527739940128)
        self.assertEqual(integral.riemman(f,0,1,10000), 0.6094049985049783)

        self.assertEqual(integral.trapecio(f,0,1,4),0.6153294692906497)
        self.assertEqual(integral.trapecio(f,0,1,10000),0.6094757091830971)

    def test2(self):
        f = lambda x: 3*x*mt.cos(x**2)

        self.assertEqual(integral.riemman(f,1,2,4), -1.6020877497586603)
        self.assertEqual(integral.riemman(f,1,2,10000), -2.3971330653828895)

class NewtonTest(ut.TestCase):# test del metodo de Newton-Raphson
    def test1(self):
        dfx = lambda  x: -2*x*(mt.e**(-x**2))-2
        fx  = lambda  x: (mt.e**(-x**2))-2*x+1
   
        punto,error,tabla =  nr.newton_raphson(2,0.001,fx,dfx)
        self.assertEqual(punto,0.7744627493872464)
        self.assertEqual(error,1.8561324865995488e-07)

class BiseccionTest(ut.TestCase):#test del metodo de biseccion
    def test1(self):
        f= lambda x: mt.e**x - 3*(x)**2

        punto, error, iteraciones = bc.biseccion(f,(0,1),0.04,6)
        self.assertEqual(punto,0.90625)
        self.assertEqual(error,0.034482758620689655)
        self.assertEqual(iteraciones,5)
        
if __name__=="__main__":
    ut.main()