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

    $ pip install omsa_alert


-------
Example
-------

If there's an error::

    $ omreport storage pdisk controller=1 -fmt ssv | oa_check pdisk -e root@localhost -e dustin@localhost
    Notifying: ['root@localhost', 'dustin@localhost']

See the command-line help for full documentation on the parameters.


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
