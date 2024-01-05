import unittest
from src.main.lab import posTaggingExercise

class TestPOSTaggingExercises(unittest.TestCase):
    def test_posTagging_exercise(self):
        result = posTaggingExercise()
        nn = False
        jj = False
        vb = False

        for tuple in result:
            nn = tuple[1] == 'NN' if nn == False else nn
            jj = tuple[1] == 'JJ' if jj == False else jj
            vb = tuple[1] == 'VB' if vb == False else vb
        
        self.assertTrue(nn)
        self.assertTrue(jj)
        self.assertTrue(vb)

if __name__ == '__main__':
    unittest.main()