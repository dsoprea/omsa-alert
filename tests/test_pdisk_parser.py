import os
import unittest
import subprocess
import json

import omsaalert.pdisk_parser
import omsaalert.utility

_APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_OACHECK_FILEPATH = os.path.join(_APP_PATH, 'omsaalert', 'resources', 'scripts', 'oa_check')
_ASSET_PATH = os.path.join(_APP_PATH, 'tests', 'assets')


class TestPdiskParser(unittest.TestCase):
    def test_run__ok(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_pdisk_controller1.ssv')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'pdisk']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        self.assertEquals(output, b'')
        self.assertEquals(p.returncode, 0)

    def test_run__error(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_pdisk_controller1.ssv.has_notok')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'pdisk', '-v']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        problems = json.loads(output.decode('utf8'))
        statuses = [disk['Status'] for disk in problems]

        self.assertEquals(statuses, ['NOT-OK'])
