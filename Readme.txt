1.  The main output of the TruncatedSVD is the file save_corr_mat.p (which is a 'pickle' file).  This matrix has all the information in order to compute 'cosine similarity' between any two books.

2.  In order to access this matrix, we have 5 critical functions that access the matrix - all 5 of these files are contained in the module with filename 'AModule.py'.

3.  The file 'MyUnitTest.py' is a file with a class definition 

class OptionsTestCases(unittest.TestCase)

This class contains 5 member functions, one each to test each of the 5 critical functions that access the matrix

4.  You can run the unit testing from a command line via:

'python MyUnitTests.py'
