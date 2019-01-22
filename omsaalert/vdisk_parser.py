import logging

import omsaalert.parser
import omsaalert.utility

_LOGGER = logging.getLogger(__name__)

_HEALTHY_VALUES = {
    'Status': ['Ok'],
    'State': ['Ready'],
}


class VdiskParser(omsaalert.parser.ParserBase):
    def check_for_problems(self, content):
        blocks = self.ssv_gen(content)
        blocks = list(blocks)

        assert \
            blocks, \
            "We did not find any virtualdisk data:\n{}".format(blocks)

        problems = []
        for virtualdisks in blocks:
            for virtualdisk in virtualdisks:
                error_message = \
                    omsaalert.utility.check_expected_values(
                        virtualdisk,
                        _HEALTHY_VALUES)

                if error_message is not None:
                    problems.append((error_message, virtualdisk))

        return problems
