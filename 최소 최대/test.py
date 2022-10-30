import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(input):
    # print(input)
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        input = read_file('최소 최대/input.txt')
        answer = read_file('최소 최대/output.txt')
        self.assertEqual(main(input), answer)


if __name__ == '__main__':
    unittest.main()