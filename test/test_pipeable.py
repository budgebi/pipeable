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

    # def test_pipe_returns_decorator(self):
    #     """ Verify that the pipe function returns a decorator. """
    #     self.assertTrue(callable(p.pipe()))

if __name__ == '__main__':
    unittest.main()
