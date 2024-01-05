import unittest
from src.main.lab import posTaggingExercise

class TestPOSTaggingExercises(unittest.TestCase):
    def test_posTagging_exercise(self):
        result = posTaggingExercise()
        nn = False
        jj = False
        vb = False

        for tuple in result:
            nn = 'NN' in tuple if nn == False else nn
            jj = 'JJ' in tuple if jj == False else jj
            vb = 'VB' in tuple if vb == False else vb
        
        self.assertTrue(nn)
        self.assertTrue(jj)
        self.assertTrue(vb)

if __name__ == '__main__':
    unittest.main()