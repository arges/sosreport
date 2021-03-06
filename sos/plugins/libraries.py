### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin

class libraries(Plugin, RedHatPlugin, UbuntuPlugin):
    """information on shared libraries
    """

    option_list = [('ldconfigv', 'the name of each directory as it is scanned, and any links that are created.',
                    "slow", False)]

    def setup(self):
        self.add_copy_specs(["/etc/ld.so.conf", "/etc/ld.so.conf.d"])
        if self.get_option("ldconfigv"):
            self.add_cmd_output("ldconfig -v -N -X")
        self.add_cmd_output("ldconfig -p -N -X")
