# Copyright 2024 Canonical Ltd.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Data models for `acct_gather.conf` configuration file."""

from slurmutils.models.core.base import BaseModel, clean, format_key, generate_descriptors, marshall_content, parse_line
from slurmutils.models.core.option import AcctGatherConfigOptionSet


class AcctGatherConfig(BaseModel):
    """`acct_gather.conf` data model."""

    def __init__(self, **kwargs) -> None:
        super().__init__(AcctGatherConfigOptionSet, **kwargs)

    @classmethod
    def from_str(cls, content: str) -> "AcctGatherConfig":
        """Construct AcctGatherConfig data model from acct_gather.conf format."""
        data = {}
        lines = content.splitlines()
        for index, line in enumerate(lines):
            config = clean(line)
            if config is None:
                continue

            data.update(parse_line(AcctGatherConfigOptionSet, config))

        return AcctGatherConfig.from_dict(data)

    def __str__(self) -> str:
        """Return AcctGatherConfig data model in acct_gather.conf format."""
        result = []
        result.extend(marshall_content(AcctGatherConfigOptionSet, self.dict()))
        return "\n".join(result)


for opt in AcctGatherConfigOptionSet.keys():
    setattr(AcctGatherConfig, format_key(opt), property(*generate_descriptors(opt)))
