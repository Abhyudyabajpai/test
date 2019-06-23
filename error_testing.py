class SomeTests(unittest.TestCase):
    def test_for_error(self):
        """error test"""
        with self.assertRaises(IndexError):
            l = [1,3,4]
            l[100]
