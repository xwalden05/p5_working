# test_runner.py
import xmlrunner
import unittest

from test_simplecaesar import SCCipherTest

def runner(output = 'python_tests_xml'):
	return xmlrunner.XMLTestRunner(output = output)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SCCipherTest)
    runner().run(suite)
