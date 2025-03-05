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

"""Callbacks for parsing and marshalling Slurm data models."""

__all__ = [
    "Callback",
    "CommaSeparatorCallback",
    "ColonSeparatorCallback",
    "EnergyIPMIPowerSensorsCallback",
    "SlurmDictCallback",
    "QuoteCallback",
]

from typing import Any, Callable, Dict, List, NamedTuple, Optional


class Callback(NamedTuple):
    """Callbacks for parsing and marshalling Slurm data model values.

    Args:
        parser: Callback that parses the value as read in from Slurm configuration.
        marshaller: Callback that marshals the value back into a valid Slurm configuration value.
    """

    parser: Optional[Callable[[str], Any]] = None
    marshaller: Optional[Callable[[Any], str]] = None


def from_slurm_dict(value: str) -> Dict[str, Any]:
    """Create dictionary from Slurm dictionary.

    Notes:
        key=value,key2 -> {"key": "value", "key2": True}
    """
    result = {}
    for opt in value.split(","):
        if "=" not in opt:
            result[opt] = True
            continue

        k, v = opt.split("=", maxsplit=1)
        result[k] = v

    return result


def to_slurm_dict(value: Dict[str, Any]) -> str:
    """Convert dictionary into Slurm dictionary.

    Notes:
        {"key": "value", "key2": True} -> key=value,key2
    """
    result = []
    for k, v in value.items():
        if isinstance(v, bool) and v:
            result.append(k)
            continue

        result.append(f"{k}={v}")

    return ",".join(result)


CommaSeparatorCallback = Callback(lambda v: v.split(","), lambda v: ",".join(v))
ColonSeparatorCallback = Callback(lambda v: v.split(":"), lambda v: ":".join(v))
SlurmDictCallback = Callback(from_slurm_dict, to_slurm_dict)
# Ensure that config values that allow spaces are properly escaped with quotes (")
# when dumped into a string or file.
QuoteCallback = Callback(None, lambda v: f'"{v}"')


def from_energy_ipmi_power_sensors(value: str) -> Dict[str, List[str]]:
    """Assemble and return the power sensors dict."""
    result = {}
    for opt in value.split(";"):
        k, v = opt.split("=", maxsplit=1)
        result[k] = v.split(",")

    return result


def to_energy_ipmi_power_sensors(value: Dict[str, List[str]]) -> str:
    """Assemble and return the power sensors string."""
    result = []
    for k, v in value.items():
        result.append(f"{k}={','.join(v)}")

    return ";".join(result)


EnergyIPMIPowerSensorsCallback = Callback(
    from_energy_ipmi_power_sensors, to_energy_ipmi_power_sensors
)
