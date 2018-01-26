import logging

_LOGGER = logging.getLogger(__name__)


class ParserBase(object):
    def ssv_gen(self, content):
        """Parse SSV-formated files.

        Has some junk lines followed by a row with headings and then data rows.

        Example 1:

            List of Physical Disks on Controller PERC 6/E Adapter (Slot 3)

            Controller PERC 6/E Adapter (Slot 3)

            ID;Status;Name;State;Power Status;Bus Protocol;Media;Part of Cache Pool;Remaining Rated Write Endurance;Failure Predicted;Revision;Driver Version;Model Number;T10 PI Capable;Certified;Encryption Capable;Encrypted;Progress;Mirror Set ID;Capacity;Used RAID Disk Space;Available RAID Disk Space;Hot Spare;Vendor ID;Product ID;Serial No.;Part Number;Negotiated Speed;Capable Speed;PCIe Negotiated Link Width;PCIe Maximum Link Width;Sector Size;Device Write Cache;Manufacture Day;Manufacture Week;Manufacture Year;SAS Address;Non-RAID HDD Disk Cache Policy;Disk Cache Policy;Form Factor ;Sub Vendor;ISE Capable
            0:0:0;Ok;Physical Disk 0:0:0;Online;Not Applicable;SAS;HDD;Not Applicable;Not Applicable;No;VR02;Not Applicable;Not Applicable;No;Not Applicable;No;Not Applicable;Not Applicable;Not Applicable;1,862.50 GB (1999844147200 bytes);1,862.50 GB (1999844147200 bytes);0.00 GB (0 bytes);No;WD;WD2001FYYG-01SL3;60012875;Not Available;Not Available;Not Available;Not Applicable;Not Applicable;512B;Not Applicable;Not Available;Not Available;Not Available;50014EE5AAACA8CF;Not Applicable;Not Applicable;Not Available;Not Available;No
            0:0:1;Ok;Physical Disk 0:0:1;Online;Not Applicable;SAS;HDD;Not Applicable;Not Applicable;No;VR02;Not Applicable;Not Applicable;No;Not Applicable;No;Not Applicable;Not Applicable;Not Applicable;1,862.50 GB (1999844147200 bytes);1,862.50 GB (1999844147200 bytes);0.00 GB (0 bytes);No;WD;WD2001FYYG-01SL3;60013555;Not Available;Not Available;Not Available;Not Applicable;Not Applicable;512B;Not Applicable;Not Available;Not Available;Not Available;50014EE5AAACB7EB;Not Applicable;Not Applicable;Not Available;Not Available;No
            0:0:2;Ok;Physical Disk 0:0:2;Online;Not Applicable;SAS;HDD;Not Applicable;Not Applicable;No;VR02;Not Applicable;Not Applicable;No;Not Applicable;No;Not Applicable;Not Applicable;Not Applicable;1,862.50 GB (1999844147200 bytes);1,862.50 GB (1999844147200 bytes);0.00 GB (0 bytes);No;WD;WD2001FYYG-01SL3;60012383;Not Available;Not Available;Not Available;Not Applicable;Not Applicable;512B;Not Applicable;Not Available;Not Available;Not Available;50014EE5AAACA923;Not Applicable;Not Applicable;Not Available;Not Available;No

        Example 2:

            List of Virtual Disks in the System

            Controller PERC 6/i Integrated (Embedded)

            ID;Status;Name;State;Hot Spare Policy violated;Encrypted;Layout;Size;T10 Protection Information Status;Associated Fluid Cache State ;Device Name;Bus Protocol;Media;Read Policy;Write Policy;Cache Policy;Stripe Element Size;Disk Cache Policy
            1;Ok;boot;Ready;Not Assigned;Not Applicable;RAID-6;4,094.75 GB (4396704333824 bytes);No;Not Applicable;/dev/sda;SATA;HDD;Adaptive Read Ahead;Write Through;Not Applicable;64 KB;Enabled

            Controller PERC 6/E Adapter (Slot 3)

            ID;Status;Name;State;Hot Spare Policy violated;Encrypted;Layout;Size;T10 Protection Information Status;Associated Fluid Cache State ;Device Name;Bus Protocol;Media;Read Policy;Write Policy;Cache Policy;Stripe Element Size;Disk Cache Policy
            0;Ok;group0;Ready;Not Assigned;Not Applicable;RAID-60;7,450.00 GB (7999376588800 bytes);No;Not Applicable;/dev/sdb;SAS;HDD;Adaptive Read Ahead;Write Through;Not Applicable;64 KB;Enabled
        """

        lines = content.split("\n")

        i = 0
        len_ = len(lines)
        while i < len_:
            block, i = self._parse_ssv_at_line(lines, i)
            i += 1

            # Skip any blocks consisting of one line.
            if len(block) < 2:
                continue

            headings, rows = block[0], block[1:]

            # Return a dictionary like:
            #
            # [
            #     {'Status': 'Ok', 'Hot Spare Policy violated': 'Not Assigned', 'Bus Protocol': 'SATA', 'Layout': 'RAID-6', 'Name': 'boot', 'Write Policy': 'Write Through', 'Disk Cache Policy': 'Enabled', 'Encrypted': 'Not Applicable', 'Stripe Element Size': '64 KB', 'T10 Protection Information Status': 'No', 'State': 'Ready', 'Media': 'HDD', 'Associated Fluid Cache State ': 'Not Applicable', 'Device Name': '/dev/sda', 'Read Policy': 'Adaptive Read Ahead', 'Cache Policy': 'Not Applicable', 'ID': '1', 'Size': '4,094.75 GB (4396704333824 bytes)'}
            # ]
            #
            yield [dict(zip(headings, row)) for row in rows]

    def _parse_ssv_at_line(self, lines, i):
        """Recursively parse the next line, collecting all lines starting from
        the current one that have the exact same number of columns. We also
        return the last line-number checked. So that we can move from block to
        block.
        """

        line_count = len(lines)
        if i > line_count:
            return [], i

        line = lines[i].strip()
        if line == '':
            return [], i

        parts = line.split(';')
        len_ = len(parts)

        next_lines, reached_line = self._parse_ssv_at_line(lines, i + 1)

        if next_lines and len(next_lines[0]) == len_:
            return [parts] + next_lines, reached_line
        else:
            return [parts], reached_line

    def check_for_problems(self, content):
        raise NotImplementedError()
