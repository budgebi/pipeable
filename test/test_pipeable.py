import unittest
import pipeable as p

class PipeableTest(unittest.TestCase):

    def test_sanity(self):
        """ Sanity check. """
        self.assertTrue(True)

    def test_single_use(self):
        """ Verify that the pipe decorator can only be used once. """
        @p.Pipe()
        def return_x(x):
            return x

        with self.assertRaises(Exception):
            @p.Pipe()
            def return_y(y):
                return y

    def test_execute(self):
        """ Test the execute function which could have a null transform. """
        x = '1'
        def id(x):
            return x
        self.assertEqual(p.Pipe()._Pipe__execute(id, None, x), x)
        self.assertEqual(p.Pipe()._Pipe__execute(id, int, x), 1)

if __name__ == '__main__':
    unittest.main()
