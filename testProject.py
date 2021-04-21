
import unittest
from project import * 

class TestProject(unittest.TestCase):

	def test_top_Points(self):

		self.assertEqual(maxPoints, 36.1)

	def test_top_Rebs(self):

		self.assertEqual(maxReb, 15.6)	

	def test_top_Assists(self):

		self.assertEqual(maxAssist, 11.6)

	def test_top_Blocks(self):

		self.assertEqual(maxBlocks, 2.9)

	def test_top_PER(self):

		self.assertEqual(maxPER, 31.94)

	def test_PPG_Leader(self):

		self.assertEqual(myTopFive[0], "James Harden")

	def test_RPG_Leader(self):

		self.assertEqual(myTopFive[1], "Andre Drummond")

	def test_APG_Leader(self):

		self.assertEqual(myTopFive[2], "Steve Nash")

	def test_BPG_Leader(self):

		self.assertEqual(myTopFive[3], "Tim Duncan")

	def test_PER_Leader(self):

		self.assertEqual(myTopFive[4], "Giannis Antetokounmpo")

	def test_MVP0(self):

		self.assertEqual(theMVPList[0], "Kevin Garnett")

	def test_MVP1(self):

		self.assertEqual(theMVPList[1], "Steve Nash")

	def test_MVP2(self):

		self.assertEqual(theMVPList[2], "Steve Nash")

	def test_MVP3(self):

		self.assertEqual(theMVPList[3], "Dirk Nowitzki")

	def test_MVP4(self):

		self.assertEqual(theMVPList[4], "Kobe Bryant")

	def test_MVP5(self):

		self.assertEqual(theMVPList[5], "Derrick Rose")

	def test_MVP6(self):

		self.assertEqual(theMVPList[6], "Kevin Durant")

	def test_MVP7(self):

		self.assertEqual(theMVPList[7], "Stephen Curry")

	def test_MVP8(self):

		self.assertEqual(theMVPList[8], "Stephen Curry")

	def test_MVP9(self):

		self.assertEqual(theMVPList[9], "Russell Westbrook")

	def test_MVP10(self):

		self.assertEqual(theMVPList[10], "James Harden")

	def test_MVP11(self):

		self.assertEqual(theMVPList[11], "Giannis Antetokounmpo")

	def test_MVP12(self):

		self.assertEqual(theMVPList[12], "Giannis Antetokounmpo")


if __name__ == '__main__':
	unittest.main()












