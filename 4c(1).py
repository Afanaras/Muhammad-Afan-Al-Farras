def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def bagi(a, b):
    return a/b

def kali(a, b):
    return a*b

def modulus(a, b):
    return a % b

def pangkat(a, b):
    return a ** b

def akar(a):
    return a ** 0.5

def maksimum(a, b):
        return max(a, b)

def minimum(a, b):
     return min(a, b)

def rata_rata(a, b):
     return (a + b) / 2

import unittest 

class TestAll(unittest.TestCase):

    def test_tambah(self):
            self.assertEqual(tambah(6, 1), 7)

    def test_kurang(self):
        self.assertEqual(kurang(3, 2), 1)

    def test_bagi(self):
        self.assertEqual(bagi(4, 2), 2)

    def test_kali(self):
        self.assertEqual(kali(2, 2), 4)

    def test_modulus(self):
        self.assertEqual(modulus(4, 3), 1)

    def test_pangkat(self):
        self.assertEqual(pangkat(2, 2), 4)

    def test_akar(self):
        self.assertEqual(akar(16), 4)

    def test_maksimum(self):
        self.assertEqual(max(3, 4), 4)

    def test_minimum(self):
        self.assertEqual(min(3, 9), 3)

    def test_rata_rata(self):
        self.assertEqual(rata_rata(4, 4), 4)

if __name__ == "__main__":
     unittest.main()