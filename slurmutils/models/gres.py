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

"""Data models for `gres.conf` configuration file."""

__all__ = ["GRESConfig", "GRESName", "GRESNode", "GRESNodeMapping", "GRESNameMapping"]

from abc import ABC
from collections.abc import MutableMapping, Sequence
from itertools import chain
from typing import Any

from jsonschema import ValidationError, validate

from slurmutils.models.core.base import BaseMapping, BaseModel, clean, marshall_content, parse_line
from slurmutils.models.core.option import GRESConfigOptionSet, GRESNameOptionSet, GRESNodeOptionSet
from slurmutils.models.core.schema import (
    GRES_NAME_MAPPING_SCHEMA,
    GRES_NAME_SCHEMA,
    GRES_NODE_MAPPING_SCHEMA,
    GRES_NODE_SCHEMA,
)


def _gres_name_decoder(o: Any) -> Any:
    """Decode `gres.conf` data model within JSON object.

    Args:
        o: JSON object to decode.
    """
    try:
        validate(o, schema=GRES_NAME_SCHEMA)
        return GRESName.from_dict(o)
    except ValidationError:
        pass

    return o


def _gres_node_decoder(o: Any) -> Any:
    """Decode `gres.conf` node data model within a JSON object.

    Args:
        o: JSON object in to decode.
    """
    try:
        validate(o, schema=GRES_NODE_SCHEMA)
        return GRESNode.from_dict(o)
    except ValidationError:
        pass

    return o


class GRESName(BaseModel):
    """`gres.conf` name data model."""

    def __init__(self, **kwargs) -> None:  # noqa N803
        super().__init__(GRESNameOptionSet, **kwargs)

    @classmethod
    def from_str(cls, content: str) -> "GRESName":
        """Construct `GRESName` data model from a gres.conf configuration line."""
        return cls(**parse_line(GRESNameOptionSet, content))

    def __str__(self) -> str:
        """Return `GRESName` data model as a gres.conf configuration line."""
        return " ".join(marshall_content(GRESNameOptionSet, self.data))

    @property
    def auto_detect(self) -> str | None:
        """Hardware detection mechanism to enable for automatic GRES configuration.

        Warnings:
            * Setting this option will override the configured global automatic
                hardware detection mechanism for this generic resource.
        """
        return self.data.get("AutoDetect", None)

    @auto_detect.setter
    def auto_detect(self, value: str) -> None:
        self.data["AutoDetect"] = value

    @auto_detect.deleter
    def auto_detect(self) -> None:
        try:
            del self.data["AutoDetect"]
        except KeyError:
            pass

    @property
    def count(self) -> str | None:
        """Number of resources of this name/type available on the node."""
        return self.data.get("Count", None)

    @count.setter
    def count(self, value: str) -> None:
        self.data["Count"] = value

    @count.deleter
    def count(self) -> None:
        try:
            del self.data["Count"]
        except KeyError:
            pass

    @property
    def cores(self) -> list[str] | None:
        """Core index numbers for the specific cores which can use this resource."""
        return self.data.get("Cores", None)

    @cores.setter
    def cores(self, value: Sequence[str]) -> None:
        self.data["Cores"] = value

    @cores.deleter
    def cores(self) -> None:
        try:
            del self.data["Cores"]
        except KeyError:
            pass

    @property
    def file(self) -> str | None:
        """Fully qualified pathname of the device files associated with a resource."""
        return self.data.get("File", None)

    @file.setter
    def file(self, value: str) -> None:
        self.data["File"] = value

    @file.deleter
    def file(self) -> None:
        try:
            del self.data["File"]
        except KeyError:
            pass

    @property
    def flags(self) -> list[str] | None:
        """Flags to change the configured behavior of the generic resource."""
        return self.data.get("Flags", None)

    @flags.setter
    def flags(self, value: Sequence[str]) -> None:
        self.data["Flags"] = value

    @flags.deleter
    def flags(self) -> None:
        try:
            del self.data["Flags"]
        except KeyError:
            pass

    @property
    def links(self) -> list[str] | None:
        """Numbers identifying the number of connections between this device and other devices."""
        return self.data.get("Links", None)

    @links.setter
    def links(self, value: Sequence[str]) -> None:
        self.data["Links"] = value

    @links.deleter
    def links(self) -> None:
        try:
            del self.data["Links"]
        except KeyError:
            pass

    @property
    def multiple_files(self) -> str | None:
        """Fully qualified pathname of the device files associated with a resource.

        Warnings:
            * Uses `files` instead if not using GPUs with multi-instance functionality.
            * `files` and `multiple_files` cannot be used together.
        """
        return self.data.get("MultipleFiles", None)

    @multiple_files.setter
    def multiple_files(self, value: str) -> None:
        self.data["MultipleFiles"] = value

    @multiple_files.deleter
    def multiple_files(self) -> None:
        try:
            del self.data["MultipleFiles"]
        except KeyError:
            pass

    @property
    def name(self) -> str:
        """Name of generic resource."""
        return self.data.get("Name")

    @name.setter
    def name(self, value: str) -> None:
        self.data["Name"] = value

    @property
    def type(self) -> str | None:
        """Arbitrary string identifying the type of the generic resource."""
        return self.data.get("Type", None)

    @type.setter
    def type(self, value: str) -> None:
        self.data["Type"] = value

    @type.deleter
    def type(self) -> None:
        try:
            del self.data["Type"]
        except KeyError:
            pass


class GRESNode(GRESName):
    """`gres.conf` node data model."""

    def __init__(self, **kwargs):  # noqa N803
        # Want to share `GRESName` descriptors, but not constructor.
        BaseModel.__init__(self, GRESNodeOptionSet, **kwargs)

    @classmethod
    def from_dict(cls, data: MutableMapping[str, Any]) -> "GRESNode":
        """Construct `GRESNode` data model from dictionary object."""
        return cls(**data)

    @classmethod
    def from_str(cls, content: str) -> "GRESNode":
        """Construct `GRESNode` data model from a gres.conf configuration line."""
        return cls(**parse_line(GRESNodeOptionSet, content))

    def __str__(self) -> str:
        """Return `GRESNode` data model as a gres.conf configuration line."""
        return " ".join(
            [f"NodeName={self.node_name}"]
            + marshall_content(GRESNodeOptionSet, self._slice(["NodeName"]))
        )

    @property
    def node_name(self) -> str:
        """Node(s) the generic resource configuration will be applied to.

        Format of the value for `NodeName` can be in the Slurm hostlist specification format.
        """
        return self.data["NodeName"]

    @node_name.setter
    def node_name(self, value: str) -> None:
        self.data["NodeName"] = value


class _GRESBaseMapping(BaseMapping, ABC):
    """Base `gres.conf` data model mapping."""

    def __str__(self) -> str:
        """Return `gres.conf` data model mapping as gres.conf configuration block."""
        return "\n".join(str(gres) for gres in chain.from_iterable(self.values()))


class GRESNameMapping(_GRESBaseMapping):
    """Map of generic resource names to `gres.conf` name data models."""

    @property
    def _decoder(self) -> Any:
        return _gres_name_decoder

    @property
    def _schema(self) -> dict[str, Any]:
        return GRES_NAME_MAPPING_SCHEMA


class GRESNodeMapping(_GRESBaseMapping):
    """Map of node names to list of `gres.conf` node data models."""

    @property
    def _decoder(self) -> Any:
        return _gres_node_decoder

    @property
    def _schema(self) -> dict[str, Any]:
        return GRES_NODE_MAPPING_SCHEMA


class GRESConfig(BaseModel):
    """`gres.conf` data model."""

    def __init__(
        self,
        *,
        Names: MutableMapping[str, Sequence[GRESName]] | None = None,  # noqa N803
        Nodes: MutableMapping[str, Sequence[GRESNode]] | None = None,  # noqa N803
        **kwargs,
    ) -> None:
        super().__init__(GRESConfigOptionSet, **kwargs)
        self.data["Names"] = GRESNameMapping(Names)
        self.data["Nodes"] = GRESNodeMapping(Nodes)

    @classmethod
    def from_str(cls, content: str) -> "GRESConfig":
        """Construct `gres.conf` data model from a gres.conf configuration file."""
        config = {"Names": GRESNameMapping(), "Nodes": GRESNodeMapping()}
        for line in [clean(line) for line in content.splitlines()]:
            if line is None:
                continue

            if line.startswith("Name"):
                new = GRESName.from_str(line)
                config["Names"][new.name] = config["Names"].get(new.name, []) + [new]
            elif line.startswith("NodeName"):
                new = GRESNode.from_str(line)
                config["Nodes"][new.node_name] = config["Nodes"].get(new.node_name, []) + [new]
            else:
                config.update(parse_line(GRESConfigOptionSet, line))

        return GRESConfig(**config)

    def __str__(self) -> str:
        """Return `gres.conf` data model in gres.conf configuration format."""
        out = []
        if self.auto_detect:
            out.append(f"AutoDetect={self.auto_detect}")
        if self.names:
            out.append(str(self.names))
        if self.nodes:
            out.append(str(self.nodes))

        return "\n".join(out) + "\n"

    @property
    def auto_detect(self) -> str | None:
        """Get global `AutoDetect` configuration in `gres.conf`.

        Warnings:
            * Setting this option will configure the automatic hardware detection mechanism
                globally within `gres.conf`. Inline `AutoDetect` can be set used on
                `GRESNode` and`GRESName` to override the global automatic hardware
                detection mechanism for specific nodes or resource names.
        """
        return self.data.get("AutoDetect")

    @auto_detect.setter
    def auto_detect(self, value: str) -> None:
        self.data["AutoDetect"] = value

    @auto_detect.deleter
    def auto_detect(self) -> None:
        try:
            del self.data["AutoDetect"]
        except KeyError:
            pass

    @property
    def names(self) -> GRESNameMapping:
        """Get map of configured generic resources."""
        return self.data.get("Names")

    @names.setter
    def names(self, value: GRESNameMapping) -> None:
        self.data["Names"] = value

    @names.deleter
    def names(self) -> None:
        self.data["Names"] = GRESNameMapping()

    @property
    def nodes(self) -> GRESNodeMapping:
        """Get map of node names with configured generic resources."""
        return self.data.get("Nodes")

    @nodes.setter
    def nodes(self, value: GRESNodeMapping) -> None:
        self.data["Nodes"] = value

    @nodes.deleter
    def nodes(self) -> None:
        self.data["Nodes"] = GRESNodeMapping()
