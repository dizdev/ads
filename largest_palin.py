import unittest
from time import time

def is_palin(num):
    num_len =len(num)
    # print num_len/2
    for i in range(0, num_len/2):
        if num[i]!=num[num_len-i-1]:
            return False
    return True

class TestIsPalin(unittest.TestCase):
    """ This class is for checking if is_palin fuction works well for one palin and
        one not palindrome  """

    def setUp(self):
        self.palins=['312343213', '312433213']
        
    def tearDown(self):
        self.paling_right, self.palin_wrong = None, None
        
    def test_is_palin(self):
        self.assertEqual(is_palin(self.palins[0]), True)
        self.assertEqual(is_palin(self.palins[1]), False) 

''' TEST SUITE DEF '''
def suite():
    tests = ['test_is_palin']

    return unittest.TestSuite(map(TestIsPalin, tests))

''' RUNNING TESTS '''
#suite = unittest.TestLoader().loadTestsFromTestCase(TestIsPalin)
test_suite = suite()
unittest.TextTestRunner(verbosity=1).run(test_suite)

''' PROGRAM '''
input_num = raw_input("Give a digit count to check:")
powered = int(input_num)
max_palin=int('1'+'0'*(powered*2-2)+'1');
# print max_palin
now = time()
for i in range(int('9'*powered), 10**(powered-1)-1, -1):
    for j in range(int('9'*powered), 10**(powered-1)-1, -1):
        if is_palin(str(i*j)) and max_palin<i*j:
            max_palin=i*j
            print i,j
done = time()
print max_palin, (done-now)*1000