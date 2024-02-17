import math as mt
import unittest as ut
import integracion_numerica as integral

class IntegrationTest(ut.TestCase):
    def test1(self):
        f = lambda x: x*(((x**2)+1)**0.5)
        self.assertEqual(integral.riemman(f,0,1,4), 0.4385527739940128)
        self.assertEqual(integral.riemman(f,0,1,10000), 0.6094049985049783)
        self.assertEqual(integral.trapecio(f,0,1,4),0.6153294692906497)
        self.assertEqual(integral.trapecio(f,0,1,10000),0.6094757091830971)

    def test2(self):
        f = lambda x: 3*x*mt.cos(x**2)
        self.assertEqual(integral.riemman(f,1,2,4), -1.6020877497586603)
        self.assertEqual(integral.riemman(f,1,2,10000), -2.3971330653828895)
        self.assertEqual(integral.trapecio(f,1,2,4), -2.2949338301069218)
        self.assertEqual(integral.trapecio(f,1,2,10000), -2.3974102038150362)

if __name__=="__main__":
    ut.main()