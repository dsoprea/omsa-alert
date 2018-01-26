import os
import unittest
import subprocess
import json

import omsaalert.vdisk_parser

_APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_OACHECK_FILEPATH = os.path.join(_APP_PATH, 'omsaalert', 'resources', 'scripts', 'oa_check')
_ASSET_PATH = os.path.join(_APP_PATH, 'tests', 'assets')


class TestVdiskParser(unittest.TestCase):
    def test_run(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_vdisk.ssv')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'vdisk']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        self.assertEquals(output, b'')
        self.assertEquals(p.returncode, 0)

    def test_run__error(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_vdisk.ssv.has_notok')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'vdisk', '-v']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        self.assertEquals(p.returncode, 5)

        output = output.decode('utf8')

        problems = json.loads(output)
        statuses = [disk['Status'] for disk in problems]

        self.assertEquals(statuses, ['NOT-OK'])

    def test_run__error__command(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_vdisk.ssv.has_notok')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'vdisk', '-c', '/bin/true']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        output = output.decode('utf8')

        expected = """\
Command: /bin/true



"""

        self.assertEquals(output, expected)
        self.assertEquals(p.returncode, 5)

    def test_run__error__command_with_stdin(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_vdisk.ssv.has_notok')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'vdisk', '-cws', '/usr/bin/tee']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        self.assertEquals(p.returncode, 5)

        output = output.decode('utf8')

        expected = """\
Command: /usr/bin/tee

[
    {
        "Associated Fluid Cache State ": "Not Applicable",
        "Bus Protocol": "SAS",
        "Cache Policy": "Not Applicable",
        "Device Name": "/dev/sdb",
        "Disk Cache Policy": "Enabled",
        "Encrypted": "Not Applicable",
        "Hot Spare Policy violated": "Not Assigned",
        "ID": "0",
        "Layout": "RAID-60",
        "Media": "HDD",
        "Name": "group0",
        "Read Policy": "Adaptive Read Ahead",
        "Size": "7,450.00 GB (7999376588800 bytes)",
        "State": "Ready",
        "Status": "NOT-OK",
        "Stripe Element Size": "64 KB",
        "T10 Protection Information Status": "No",
        "Write Policy": "Write Through"
    }
]

"""

        self.assertEquals(output, expected)

    def test_run__error__email(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_vdisk.ssv.has_notok')
        with open(filepath, 'rb') as f:
            content = f.read()

        cmd = [_OACHECK_FILEPATH, 'vdisk', '-e', 'root']

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        output, _ = p.communicate(input=content)

        self.assertEquals(p.returncode, 5)

        output = output.decode('utf8')

        expected = """\
Notifying: ['root']
"""

        self.assertEquals(output, expected)
