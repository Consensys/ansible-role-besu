#! /usr/bin/env python

from typing import Union, List


def besu_opts_format(besu_env_opts: Union[str, List[str]]):
    if isinstance(besu_env_opts, str):
        besu_env_opts = besu_env_opts.split()

    escaped_besu_env_opts = [item.replace('"', '\\"') for item in besu_env_opts]

    return f'''"{'" "'.join(escaped_besu_env_opts)}"'''


class FilterModule(object):
    def filters(self):
        return {
            'besu_opts_format': besu_opts_format,
        }
