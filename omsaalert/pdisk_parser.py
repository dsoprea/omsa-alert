import logging

import omsaalert.parser
import omsaalert.utility

_LOGGER = logging.getLogger(__name__)

_HEALTHY_VALUES = {
    'Status': ['Ok'],
    'State': ['Online'],
}


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
            error_message = \
                omsaalert.utility.check_expected_values(
                    disk,
                    _HEALTHY_VALUES)

            if error_message is not None:
                problems.append((error_message, disk))

        return problems
