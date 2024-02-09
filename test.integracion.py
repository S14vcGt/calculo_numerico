import unittest as ut
import integracion_numerica as integral

class IntegrationTest(ut.TestCase):
    def test(self):
        f = lambda x: x*(((x**2)+1)**0.5)
        self.assertEqual(integral.integracion(f,0,1,4), 0.4385527739940128)
        self.assertEqual(integral.integracion(f,0,1,10000), 0.6094049985049783)

if __name__=="__main__":
    ut.main()