import unittest


# 'True'            --> True
# 'False'           --> False
# 'not True'        --> False
# 'not False'       --> True
# 'not not True'    --> True
# 'not not False'   --> False

def NotCount(s):
  result = eval(s.split()[-1])
  if len(s.split()) % 2 == 0:
    result = not result
  return result

class NotCountTest(unittest.TestCase):
  def testOn(self):
    self.failUnless(NotCount('True'))

  def testTwo(self):
    self.failIf(NotCount('False'))

  def testThree(self):
    self.failIf(NotCount('not True'))

  def testFour(self):
    self.failUnless(NotCount('not False'))

  def testFive(self):
    self.failUnless(NotCount('not not True'))

  def testSix(self):
    self.failIf(NotCount('not not False'))


def main():
  unittest.main()

if __name__ == '__main__':
  main()



