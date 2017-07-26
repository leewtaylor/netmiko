from __future__ import unicode_literals
import re
from netmiko.cisco_base_connection import CiscoSSHConnection


class BrocadeServerironAdxSSH(CiscoSSHConnection):
    """Brocade Serveriron ADX support."""
    def enable(self, cmd='enable', pattern='user name:', re_flags=re.IGNORECASE):
        """Enter enable mode."""
        output = ""
        if not self.check_enable_mode():
            self.write_channel(self.normalize_cmd(cmd))
            output += self.read_until_prompt_or_pattern(pattern=pattern, re_flags=re_flags)
            self.write_channel(self.normalize_cmd(self.username))
            output += self.read_until_prompt_or_pattern(pattern='password:', re_flags=re_flags)
            self.write_channel(self.normalize_cmd(self.secret))
            output += self.read_until_prompt()
            if not self.check_enable_mode():
                raise ValueError("Failed to enter enable mode.")
        return output
