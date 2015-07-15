# Copyright (C) 2013,2015 Claudio "nex" Guarnieri (@botherder), Accuvant, Inc. (bspengler@accuvant.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class GetProductID(Signature):
    name = "antisandbox_productid"
    description = "Retrieves Windows ProductID, probably to fingerprint the sandbox"
    severity = 3
    categories = ["anti-sandbox"]
    authors = ["nex", "Accuvant"]
    minimum = "1.2"

    def run(self):
        indicators = [
            ".*\\\\Microsoft\\\\Windows\\ NT\\\\CurrentVersion\\\\ProductId$",
            ".*\\\\Microsoft\\\\Internet\\ Explorer\\\\Registration\\\\ProductId$",
        ]
        for indicator in indicators:
            if self.check_read_key(pattern=indicator, regex=True):
                return True
        return False