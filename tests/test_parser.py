import os
import unittest

import omsaalert.parser

_APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_ASSET_PATH = os.path.join(_APP_PATH, 'tests', 'assets')


class TestParser(unittest.TestCase):
    def test_ssv_gen__vdisk(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_vdisk.ssv')
        with open(filepath) as f:
            content = f.read()

        p = omsaalert.parser.ParserBase()
        gen = p.ssv_gen(content)

        blocks = list(gen)

        expected = [
            [{'Status': 'Ok', 'Hot Spare Policy violated': 'Not Assigned', 'Bus Protocol': 'SATA', 'Layout': 'RAID-6', 'Name': 'boot', 'Write Policy': 'Write Through', 'Disk Cache Policy': 'Enabled', 'Encrypted': 'Not Applicable', 'Stripe Element Size': '64 KB', 'T10 Protection Information Status': 'No', 'State': 'Ready', 'Media': 'HDD', 'Associated Fluid Cache State ': 'Not Applicable', 'Device Name': '/dev/sda', 'Read Policy': 'Adaptive Read Ahead', 'Cache Policy': 'Not Applicable', 'ID': '1', 'Size': '4,094.75 GB (4396704333824 bytes)'}],
            [{'Status': 'Ok', 'Hot Spare Policy violated': 'Not Assigned', 'Bus Protocol': 'SAS', 'Layout': 'RAID-60', 'Name': 'group0', 'Write Policy': 'Write Through', 'Disk Cache Policy': 'Enabled', 'Encrypted': 'Not Applicable', 'Stripe Element Size': '64 KB', 'T10 Protection Information Status': 'No', 'State': 'Ready', 'Media': 'HDD', 'Associated Fluid Cache State ': 'Not Applicable', 'Device Name': '/dev/sdb', 'Read Policy': 'Adaptive Read Ahead', 'Cache Policy': 'Not Applicable', 'ID': '0', 'Size': '7,450.00 GB (7999376588800 bytes)'}],
        ]

        self.assertEquals(blocks, expected)

    def test_ssv_gen__pdisk(self):
        filepath = os.path.join(_ASSET_PATH, 'omreport_storage_pdisk_controller1.ssv')
        with open(filepath) as f:
            content = f.read()

        p = omsaalert.parser.ParserBase()
        gen = p.ssv_gen(content)

        blocks = list(gen)

        expected = [
            [
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:0",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:0",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE5AAACA8CF",
                    "Sector Size": "512B",
                    "Serial No.": "60012875",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:1",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:1",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE5AAACB7EB",
                    "Sector Size": "512B",
                    "Serial No.": "60013555",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:2",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:2",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE5AAACA923",
                    "Sector Size": "512B",
                    "Serial No.": "60012383",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:3",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:3",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE500020473",
                    "Sector Size": "512B",
                    "Serial No.": "60016424",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:4",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:4",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE50002079B",
                    "Sector Size": "512B",
                    "Serial No.": "60016692",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:5",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:5",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE50002071F",
                    "Sector Size": "512B",
                    "Serial No.": "60016889",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:6",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:6",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE555574F37",
                    "Sector Size": "512B",
                    "Serial No.": "60043942",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "No",
                    "ID": "0:0:7",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:7",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE55557620F",
                    "Sector Size": "512B",
                    "Serial No.": "60013791",
                    "State": "Online",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "Global",
                    "ID": "0:0:8",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:8",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE5AAACB3CE",
                    "Sector Size": "512B",
                    "Serial No.": "60016322",
                    "State": "Ready",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                },
                {
                    "Available RAID Disk Space": "0.00 GB (0 bytes)",
                    "Bus Protocol": "SAS",
                    "Capable Speed": "Not Available",
                    "Capacity": "1,862.50 GB (1999844147200 bytes)",
                    "Certified": "Not Applicable",
                    "Device Write Cache": "Not Applicable",
                    "Disk Cache Policy": "Not Applicable",
                    "Driver Version": "Not Applicable",
                    "Encrypted": "Not Applicable",
                    "Encryption Capable": "No",
                    "Failure Predicted": "No",
                    "Form Factor ": "Not Available",
                    "Hot Spare": "Global",
                    "ID": "0:0:9",
                    "ISE Capable": "No",
                    "Manufacture Day": "Not Available",
                    "Manufacture Week": "Not Available",
                    "Manufacture Year": "Not Available",
                    "Media": "HDD",
                    "Mirror Set ID": "Not Applicable",
                    "Model Number": "Not Applicable",
                    "Name": "Physical Disk 0:0:9",
                    "Negotiated Speed": "Not Available",
                    "Non-RAID HDD Disk Cache Policy": "Not Applicable",
                    "PCIe Maximum Link Width": "Not Applicable",
                    "PCIe Negotiated Link Width": "Not Applicable",
                    "Part Number": "Not Available",
                    "Part of Cache Pool": "Not Applicable",
                    "Power Status": "Not Applicable",
                    "Product ID": "WD2001FYYG-01SL3",
                    "Progress": "Not Applicable",
                    "Remaining Rated Write Endurance": "Not Applicable",
                    "Revision": "VR02",
                    "SAS Address": "50014EE50001F816",
                    "Sector Size": "512B",
                    "Serial No.": "60006588",
                    "State": "Ready",
                    "Status": "Ok",
                    "Sub Vendor": "Not Available",
                    "T10 PI Capable": "No",
                    "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
                    "Vendor ID": "WD"
                }
            ]
        ]

        self.assertEquals(blocks, expected)
