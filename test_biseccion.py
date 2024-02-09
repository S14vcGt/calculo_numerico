import math as mt
import unittest as ut
import biseccion as bc
class test(ut.TestCase):
    def test(self):
        f= lambda x: mt.e**x - 3*(x)**2
        self.assertEqual(bc.biseccion(f,(0,1),0.04,6),(0.90625,0.03,5))

if __name__ == "__main__":
    ut.main()