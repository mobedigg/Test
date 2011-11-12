import random
import unittest

import quiz

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))
        self.num = 5

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestQuizFunctions(unittest.TestCase):

    def test_addition(self):
        add5 = quiz.addition(5)
        self.assertEqual(add5(3), 8)
        self.assertEqual(add5(10), 15)

    def test_addition_lambda(self):
        add8 = quiz.addition_lambda(8)
        self.assertEqual(add8(10), 18)

    def test_image(self):
        img = quiz.Image()
        img.height = 340
        self.assertEqual(img.height, 340)
        img.path = '/tmp/x00.jpeg'
        #self.assertRaises(TypeError, img.path = 320)

    def test_observable(self):
        class X(quiz.Observable):
            pass
        x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
        self.assertEqual(x.foo, 1)
        self.assertEqual(x.name, 'Amok')

    def test_dict_attr(self):
        datr = quiz.DictAttr(foo = 1, bar = 'string')
        self.assertEqual(datr.foo, datr['foo'])
        self.assertEqual(datr.get('fo', 12), 12)
        datr['new'] = 15
        self.assertEqual(datr.get('new'), 15)

if __name__ == '__main__':
    unittest.main()
