--------
Overview
--------

The Dell OMSA (OpenManage Server Administrator) command-line tools are a suite of stateless tools for querying or reconfiguring your Dell server hardware, including PERC controllers, virtual disks, and physical disks. This tool is able to take "omreport vdisk" and "omreport pdisk" output, check for the existence of problems (non-OK statuses on your physical disks or virtual disks), and take action if it finds anything.

It can send one or more emails or call one or more commands. You can also choose to forward information about the problematic device to one or more commands.

Feel free to submit pull-requests with any missing features that might increase usefulness.


-------
Install
-------

Use PyPI::

    $ pip install omsa-alert


-------
Example
-------

If there's an error::

    $ omreport storage pdisk controller=1 -fmt ssv | oa_check pdisk -e root@localhost -e dustin@localhost
    Notifying: ['root@localhost', 'dustin@localhost']

An example of such an email::

    Return-Path: <omsaalert@localhost>
    X-Original-To: root@localhost
    Delivered-To: root@localhost
    Received: from mlll2664.magicleap.ds (mlll2664.magicleap.ds [IPv6:::1])
        by mlll2664.magicleap.ds (Postfix) with ESMTP id CC8E71720D2C
        for <root@localhost>; Fri, 26 Jan 2018 05:40:48 -0500 (EST)
    Content-Type: text/plain; charset="us-ascii"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Subject: OMSA Reported a Problem
    From: omsaalert@localhost
    To: root@localhost, dustin@localhost
    Message-Id: <20180126104048.CC8E71720D2C@mlll2664.magicleap.ds>
    Date: Fri, 26 Jan 2018 05:40:48 -0500 (EST)

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
            "Status": "NOT-OK",
            "Sub Vendor": "Not Available",
            "T10 PI Capable": "No",
            "Used RAID Disk Space": "1,862.50 GB (1999844147200 bytes)",
            "Vendor ID": "WD"
        }
    ]

NOTE: This is a contrived example. The disk information is based on a perfectly healthy disk. Real failures will look different.

See the command-line help for full documentation on parameters.


--------
Features
--------

- May send messages to many email recipients.
- May call many separate commands and optionally pass the information for the problematic devices via STDIN.
- Turn on verbosity to print the problem information to the screen (useful with Crontab).
- Will fail with a return-code of (5) when it encounters a problem (by default) unless you tell it not to.


-----
Tests
-----

There is a complete testing suite::

    $ ./test.sh
