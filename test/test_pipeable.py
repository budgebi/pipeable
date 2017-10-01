import unittest
import pipeable as p

class PipeableTest(unittest.TestCase):

    def test_sanity(self):
        """ Sanity check. """
        self.assertTrue(True)

    def test_single_use(self):
        """ Verify that the pipe decorator can only be used once. """
        @p.pipe()
        def return_x(x):
            return x

        with self.assertRaises(Exception):
            @p.pipe()
            def return_y(y):
                return y

if __name__ == '__main__':
    unittest.main()
