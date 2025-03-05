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

"""Data models for `slurmdbd.conf` configuration file."""

from slurmutils.models.core.base import BaseModel, clean, format_key, generate_descriptors, marshall_content, parse_line
from slurmutils.models.core.option import SlurmdbdConfigOptionSet


class SlurmdbdConfig(BaseModel):
    """`slurmdbd.conf` data model."""

    def __init__(self, **kwargs):
        super().__init__(SlurmdbdConfigOptionSet, **kwargs)

    @classmethod
    def from_str(cls, content: str) -> "SlurmdbdConfig":
        """Construct SlurmdbdConfig data model from slurmdbd.conf format."""
        data = {}
        lines = content.splitlines()
        for index, line in enumerate(lines):
            config = clean(line)
            if config is None:
                continue

            data.update(parse_line(SlurmdbdConfigOptionSet, config))

        return cls.from_dict(data)

    def __str__(self) -> str:
        """Return SlurmdbdConfig data model in slurmdbd.conf format."""
        result = []
        result.extend(marshall_content(SlurmdbdConfigOptionSet, self.dict()))
        return "\n".join(result)


for opt in SlurmdbdConfigOptionSet.keys():
    setattr(SlurmdbdConfig, format_key(opt), property(*generate_descriptors(opt)))
