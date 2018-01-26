import logging

import omsaalert.parser

_LOGGER = logging.getLogger(__name__)


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
                if virtualdisk['Status'].lower() != 'ok':
                    problems.append(virtualdisk)

        return problems
