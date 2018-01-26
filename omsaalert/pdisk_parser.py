import logging

import omsaalert.parser

_LOGGER = logging.getLogger(__name__)


class PdiskParser(omsaalert.parser.ParserBase):
    def check_for_problems(self, content):
        blocks = self.ssv_gen(content)
        blocks = list(blocks)

        assert \
            len(blocks) == 1, \
            "Expected exactly one block of physical-disk data in the output:\n{}".format(blocks)

        disks = blocks[0]

        problems = []
        for disk in disks:
            if disk['Status'].lower() != 'ok':
                problems.append(disk)

        return problems
