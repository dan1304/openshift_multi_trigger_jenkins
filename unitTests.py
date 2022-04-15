import unittest

from releaseUtils import *

class releaseUtilsTestCases(unittest.TestCase):
    def setUp(self):
        self.testJenkinsApiTrigger = jenkinsApiTrigger("voucher", "4.41", "staging")
    
    def testPreparePromote(self):
        """Test trigger for prepare promote"""
        trigger_cmd = self.testJenkinsApiTrigger.preparePromote()
        print(trigger_cmd)
        self.assertEqual(trigger_cmd, "200 OK")
    
    def testPromote(self):
        """Test trigger for promote"""
        trigger_cmd = self.testJenkinsApiTrigger.promote()
        print(trigger_cmd)
        self.assertEqual(trigger_cmd, "[TRIGGERED][voucher 4.41]: https://jenkins-equator.cicd.mn1.ocp.ascendmoney-dev.internal/job/equator-cicd/job/equator-cicd-voucher-promote-to-staging")

if __name__ == '__main__':
    unittest.main()