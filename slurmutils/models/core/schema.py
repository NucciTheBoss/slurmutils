# Copyright 2024-2025 Canonical Ltd.
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

"""JSON schemas for validating Slurm data models."""

__all__ = [
    "GRES_NAME_SCHEMA",
    "GRES_NODE_SCHEMA",
    "GRES_NAME_MAPPING_SCHEMA",
    "GRES_NODE_MAPPING_SCHEMA",
]

_GLOBAL_SCHEMA_VERSION = "https://json-schema.org/draft/2020-12/schema"

# `acct_gather.conf` data model schema.

ACCT_GATHER_CONFIG_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {},
    "additionalProperties": False,
}

# `cgroup.conf` data model schema.

CGROUP_CONFIG_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {},
    "additionalProperties": False,
}

# `gres.conf` data model schemas.

GRES_NAME_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "AutoDetect": {"type": "string"},
        "Count": {"type": "string"},
        "Cores": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
        "File": {"type": "string"},
        "Flags": {"type": "array", "items": {"type": "string"}, "uniqueItems": True},
        "Links": {"type": "array", "items": {"type": "string"}},
        "MultipleFiles": {"type": "string"},
        "Name": {"type": "string"},
        "Type": {"type": "string"},
    },
    "additionalProperties": False,
}

GRES_NODE_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "NodeName": {"type": "string"},
        **GRES_NAME_SCHEMA["properties"],
    },
    "additionalProperties": False,
}

GRES_NAME_MAPPING_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "patternProperties": {
        "^.+$": {
            "type": "array",
            "items": {
                "$ref": "#/$defs/GRESName",
            },
            "uniqueItems": True,
        },
    },
    "$defs": {"GRESName": GRES_NAME_SCHEMA},
}

GRES_NODE_MAPPING_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "patternProperties": {
        "^.+$": {
            "type": "array",
            "items": {"$ref": "#/$defs/GRESNode"},
            "uniqueItems": True,
        }
    },
    "$defs": {
        "GRESNode": GRES_NODE_SCHEMA,
    },
}

GRES_CONFIG_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "AutoDetect": {"type": "string"},
        "Names": {"$ref", "#/$defs/GRESNameMapping"},
        "Nodes": {"$ref", "#/$defs/GRESNodeMapping"},
    },
    "additionalProperties": False,
    "$defs": {
        "GRESNameMapping": GRES_NAME_MAPPING_SCHEMA,
        "GRESNodeMapping": GRES_NODE_MAPPING_SCHEMA,
    },
}

# `slurm.conf` data model schemas.

NODE_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "NodeName": {"type": ...},
        "NodeHostname": {"type": ...},
        "NodeAddr": {"type": ...},
        "BcastAddr": {"type": ...},
        "Boards": {"type": ...},
        "CoreSpecCount": {"type": ...},
        "CoresPerSocket": {"type": ...},
        "CpuBind": {"type": ...},
        "CPUs": {"type": ...},
        "CpuSpecList": {"type": ...},
        "Features": {"type": ...},
        "Gres": {"type": ...},
        "MemSpecLimit": {"type": ...},
        "Port": {"type": ...},
        "Procs": {"type": ...},
        "RealMemory": {"type": ...},
        "Reason": {"type": ...},
        "Sockets": {"type": ...},
        "SocketsPerBoard": {"type": ...},
        "State": {"type": ...},
        "ThreadsPerCore": {"type": ...},
        "TmpDisk": {"type": ...},
        "Weight": {"type": ...},
    },
    "additionalProperties": False,
}

DOWN_NODE_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "DownNodes": {"type", ...},
        "Reason": {"type", ...},
        "State": {"type", ...},
    },
    "additionalProperties": False,
}

FRONTEND_NODE_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "FrontendName": {"type", ...},
        "FrontendAddr": {"type", ...},
        "AllowGroups": {"type", ...},
        "AllowUsers": {"type", ...},
        "DenyGroups": {"type", ...},
        "DenyUsers": {"type", ...},
        "Port": {"type", ...},
        "Reason": {"type", ...},
        "State": {"type", ...},
    },
    "additionalProperties": False,
}

NODESET_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "NodeSet": {"type", ...},
        "Feature": {"type", ...},
        "Nodes": {"type", ...},
    },
    "additionalProperties": False,
}

PARTITION_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {
        "PartitionName": {"type", ...},
        "AllocNodes": {"type", ...},
        "AllowAccounts": {"type", ...},
        "AllowGroups": {"type", ...},
        "AllowQos": {"type", ...},
        "Alternate": {"type", ...},
        "CpuBind": {"type", ...},
        "Default": {"type", ...},
        "DefaultTime": {"type", ...},
        "DefCpuPerGPU": {"type", ...},
        "DefMemPerCPU": {"type", ...},
        "DefMemPerGPU": {"type", ...},
        "DefMemPerNode": {"type", ...},
        "DenyAccounts": {"type", ...},
        "DenyQos": {"type", ...},
        "DisableRootJobs": {"type", ...},
        "ExclusiveUser": {"type", ...},
        "GraceTime": {"type", ...},
        "Hidden": {"type", ...},
        "LLN": {"type", ...},
        "MaxCPUsPerNode": {"type", ...},
        "MaxCPUsPerSocket": {"type", ...},
        "MaxMemPerCPU": {"type", ...},
        "MaxMemPerNode": {"type", ...},
        "MaxNodes": {"type", ...},
        "MaxTime": {"type", ...},
        "MinNodes": {"type", ...},
        "Nodes": {"type", ...},
        "OverSubscribe": {"type", ...},
        "OverTimeLimit": {"type", ...},
        "PowerDownOnIdle": {"type", ...},
        "PreemptMode": {"type", ...},
        "PriorityJobFactor": {"type", ...},
        "PriorityTier": {"type", ...},
        "QOS": {"type", ...},
        "ReqResv": {"type", ...},
        "ResumeTimeout": {"type", ...},
        "RootOnly": {"type", ...},
        "SelectTypeParameters": {"type", ...},
        "State": {"type", ...},
        "SuspendTime": {"type", ...},
        "SuspendTimeout": {"type", ...},
        "TRESBillingWeights": {"type", ...},
    },
    "additionalProperties": False,
}

SLURM_CONFIG_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {},
    "additionalProperties": False,
}

# `slurmdbd.conf` data model schema.

SLURMDBD_CONFIG_MODEL_SCHEMA = {
    "$schema": _GLOBAL_SCHEMA_VERSION,
    "type": "object",
    "properties": {},
    "additionalProperties": False
}
