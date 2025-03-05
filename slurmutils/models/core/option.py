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

"""Configuration options for Slurm data models."""

__all__ = [
    "AcctGatherConfigOptionSet",
    "CgroupConfigOptionSet",
    "GRESConfigOptionSet",
    "GRESNameOptionSet",
    "GRESNodeOptionSet",
    "SlurmdbdConfigOptionSet",
    "SlurmConfigOptionSet",
    "NodeOptionSet",
    "DownNodeOptionSet",
    "FrontendNodeOptionSet",
    "NodeSetOptionSet",
    "PartitionOptionSet",
]

from collections.abc import Iterable
from dataclasses import dataclass, fields
from typing import Annotated

from slurmutils.models.core.callback import (
    Callback,
    ColonSeparatorCallback,
    CommaSeparatorCallback,
    EnergyIPMIPowerSensorsCallback,
    QuoteCallback,
    SlurmDictCallback,
)


@dataclass(frozen=True)
class _OptionSet:
    """Base for configuration option dataclasses."""

    @classmethod
    def keys(cls) -> Iterable[str]:
        """Yield iterable list of configuration option names."""
        for field in fields(cls):
            yield field.name


@dataclass(frozen=True)
class AcctGatherConfigOptionSet(_OptionSet):
    """`acct_gather.conf` configuration options."""

    EnergyIPMIFrequency: Callback = Callback()
    EnergyIPMICalcAdjustment: Callback = Callback()
    EnergyIPMIPowerSensors: Callback = EnergyIPMIPowerSensorsCallback
    EnergyIPMIUsername: Callback = Callback()
    EnergyIPMIPassword: Callback = Callback()
    EnergyIPMIFrequency: Callback = Callback()
    EnergyIPMITimeout: Callback = Callback()
    ProfileHDF5Dir: Callback = Callback()
    ProfileHDF5Default: Callback = CommaSeparatorCallback
    ProfileInfluxDBDatabase: Callback = Callback()
    ProfileInfluxDBDefault: Callback = CommaSeparatorCallback
    ProfileInfluxDBHost: Callback = Callback()
    ProfileInfluxDBPass: Callback = Callback()
    ProfileInfluxDBRTPolicy: Callback = Callback()
    ProfileInfluxDBUser: Callback = Callback()
    ProfileInfluxDBTimeout: Callback = Callback()
    InfinibandOFEDPort: Callback = Callback()
    SysfsInterfaces: Callback = CommaSeparatorCallback


@dataclass(frozen=True)
class CgroupConfigOptionSet(_OptionSet):
    """`cgroup.conf` configuration options."""

    CgroupMountpoint: Callback = Callback()
    CgroupPlugin: Callback = Callback()
    SystemdTimeout: Callback = Callback()
    IgnoreSystemd: Callback = Callback()
    IgnoreSystemdOnFailure: Callback = Callback()
    EnableControllers: Callback = Callback()
    AllowedRAMSpace: Callback = Callback()
    AllowedSwapSpace: Callback = Callback()
    ConstrainCores: Callback = Callback()
    ConstrainDevices: Callback = Callback()
    ConstrainRAMSpace: Callback = Callback()
    ConstrainSwapSpace: Callback = Callback()
    MaxRAMPercent: Callback = Callback()
    MaxSwapPercent: Callback = Callback()
    MemorySwappiness: Callback = Callback()
    MinRAMSpace: Callback = Callback()
    SignalChildrenProcesses: Callback = Callback()


@dataclass(frozen=True)
class GRESConfigOptionSet(_OptionSet):
    """`gres.conf` configuration options."""

    AutoDetect: Callback = Callback()


@dataclass(frozen=True)
class GRESNameOptionSet(GRESConfigOptionSet):
    """`gres.conf` generic configuration options."""

    Count: Callback = Callback()
    Cores: Callback = CommaSeparatorCallback
    File: Callback = Callback()
    Flags: Callback = CommaSeparatorCallback
    Links: Callback = CommaSeparatorCallback
    MultipleFiles: Callback = Callback()
    Name: Callback = Callback()
    Type: Callback = Callback()


@dataclass(frozen=True)
class GRESNodeOptionSet(GRESNameOptionSet):
    """`gres.conf` node configuration options."""

    NodeName: Callback = Callback()


@dataclass(frozen=True)
class SlurmdbdConfigOptionSet(_OptionSet):
    """`slurmdbd.conf` configuration options."""

    AllowNoDefAcct: Callback = Callback()
    AllResourcesAbsolute: Callback = Callback()
    ArchiveDir: Callback = Callback()
    ArchiveEvents: Callback = Callback()
    ArchiveJobs: Callback = Callback()
    ArchiveResvs: Callback = Callback()
    ArchiveScript: Callback = Callback()
    ArchiveSteps: Callback = Callback()
    ArchiveSuspend: Callback = Callback()
    ArchiveTXN: Callback = Callback()
    ArchiveUsage: Callback = Callback()
    AuthAltTypes: Callback = CommaSeparatorCallback
    AuthAltParameters: Callback = SlurmDictCallback
    AuthInfo: Callback = SlurmDictCallback
    AuthType: Callback = Callback()
    CommitDelay: Callback = Callback()
    CommunicationParameters: Callback = SlurmDictCallback
    DbdAddr: Callback = Callback()
    DbdBackupHost: Callback = Callback()
    DbdHost: Callback = Callback()
    DbdPort: Callback = Callback()
    DebugFlags: Callback = CommaSeparatorCallback
    DebugLevel: Callback = Callback()
    DebugLevelSyslog: Callback = Callback()
    DefaultQOS: Callback = Callback()
    LogFile: Callback = Callback()
    LogTimeFormat: Callback = Callback()
    MaxQueryTimeRange: Callback = Callback()
    MessageTimeout: Callback = Callback()
    Parameters: Callback = CommaSeparatorCallback
    PidFile: Callback = Callback()
    PluginDir: Callback = ColonSeparatorCallback
    PrivateData: Callback = CommaSeparatorCallback
    PurgeEventAfter: Callback = Callback()
    PurgeJobAfter: Callback = Callback()
    PurgeResvAfter: Callback = Callback()
    PurgeStepAfter: Callback = Callback()
    PurgeSuspendAfter: Callback = Callback()
    PurgeTXNAfter: Callback = Callback()
    PurgeUsageAfter: Callback = Callback()
    SlurmUser: Callback = Callback()
    StorageBackupHost: Callback = Callback()
    StorageHost: Callback = Callback()
    StorageLoc: Callback = Callback()
    StorageParameters: Callback = SlurmDictCallback
    StoragePass: Callback = Callback()
    StoragePort: Callback = Callback()
    StorageType: Callback = Callback()
    StorageUser: Callback = Callback()
    TCPTimeout: Callback = Callback()
    TrackSlurmctldDown: Callback = Callback()
    TrackWCKey: Callback = Callback()


@dataclass(frozen=True)
class SlurmConfigOptionSet(_OptionSet):
    """`slurm.conf` configuration options."""

    AccountingStorageBackupHost: Callback = CommaSeparatorCallback
    AccountingStorageEnforce: Callback = Callback()
    AccountingStorageExternalHost: Callback = Callback()
    AccountingStorageHost: Callback = Callback()
    AccountingStorageParameters: Callback = SlurmDictCallback
    AccountingStoragePass: Callback = Callback()
    AccountingStoragePort: Callback = Callback()
    AccountingStorageTRES: Callback = CommaSeparatorCallback
    AccountingStorageType: Callback = Callback()
    AccountingStorageUser: Callback = Callback()
    AccountingStoreFlags: Callback = CommaSeparatorCallback
    AcctGatherNodeFreq: Callback = Callback()
    AcctGatherEnergyType: Callback = Callback()
    AcctGatherInterconnectType: Callback = Callback()
    AcctGatherFilesystemType: Callback = Callback()
    AcctGatherProfileType: Callback = Callback()
    AllowSpecResourcesUsage: Callback = Callback()
    AuthAltTypes: Callback = CommaSeparatorCallback
    AuthAltParameters: Callback = SlurmDictCallback
    AuthInfo: Callback = SlurmDictCallback
    AuthType: Callback = Callback()
    BatchStartTimeout: Callback = Callback()
    BcastExclude: Callback = CommaSeparatorCallback
    BcastParameters: Callback = SlurmDictCallback
    BurstBufferType: Callback = Callback()
    CliFilterPlugins: Callback = CommaSeparatorCallback
    ClusterName: Callback = Callback()
    CommunicationParameters: Callback = SlurmDictCallback
    CheckGhalQuiesce: Callback = Callback()
    DisableIPv4: Callback = Callback()
    EnableIPv6: Callback = Callback()
    NoCtldInAddrAny: Callback = Callback()
    NoInAddrAny: Callback = Callback()
    CompleteWait: Callback = Callback()
    CoreSpecPlugin: Callback = Callback()
    CpuFreqDef: Callback = CommaSeparatorCallback
    CpuFreqGovernors: Callback = CommaSeparatorCallback
    CredType: Callback = Callback()
    DebugFlags: Callback = CommaSeparatorCallback
    BurstBuffer: Callback = Callback()
    DefCpuPerGPU: Callback = Callback()
    DefMemPerCPU: Callback = Callback()
    DefMemPerGPU: Callback = Callback()
    DefMemPerNode: Callback = Callback()
    DependencyParameters: Callback = SlurmDictCallback
    DisableRootJobs: Callback = Callback()
    EioTimeout: Callback = Callback()
    EnforcePartLimits: Callback = Callback()
    Epilog: Callback = Callback()
    EpilogMsgTime: Callback = Callback()
    EpilogSlurmctld: Callback = Callback()
    FairShareDampeningFactor: Callback = Callback()
    FederationParameters: Callback = CommaSeparatorCallback
    FirstJobId: Callback = Callback()
    GetEnvTimeout: Callback = Callback()
    GresTypes: Callback = Callback()
    GroupUpdateForce: Callback = Callback()
    GroupUpdateTime: Callback = Callback()
    GpuFreqDef: Callback = Callback()
    HealthCheckInterval: Callback = Callback()
    HealthCheckNodeState: Callback = CommaSeparatorCallback
    HealthCheckProgram: Callback = Callback()
    InactiveLimit: Callback = Callback()
    InteractiveStepOptions: Callback = Callback()
    JobAcctGatherType: Callback = Callback()
    JobAcctGatherFrequency: Callback = SlurmDictCallback
    JobAcctGatherParams: Callback = Callback()
    NoShared: Callback = Callback()
    UsePss: Callback = Callback()
    OverMemoryKill: Callback = Callback()
    DisableGPUAcct: Callback = Callback()
    JobCompHost: Callback = Callback()
    JobCompLoc: Callback = Callback()
    JobCompParams: Callback = SlurmDictCallback
    JobCompPass: Callback = Callback()
    JobCompPort: Callback = Callback()
    JobCompType: Callback = Callback()
    JobCompUser: Callback = Callback()
    JobContainerType: Callback = Callback()
    JobFileAppend: Callback = Callback()
    JobRequeue: Callback = Callback()
    JobSubmitPlugins: Callback = CommaSeparatorCallback
    KillOnBadExit: Callback = Callback()
    KillWait: Callback = Callback()
    MaxBatchRequeue: Callback = Callback()
    NodeFeaturesPlugins: Callback = Callback()
    LaunchParameters: Callback = SlurmDictCallback
    Licenses: Callback = CommaSeparatorCallback
    LogTimeFormat: Callback = Callback()
    MailDomain: Callback = Callback()
    MailProg: Callback = Callback()
    MaxArraySize: Callback = Callback()
    MaxDBDMsgs: Callback = Callback()
    MaxJobCount: Callback = Callback()
    MaxJobId: Callback = Callback()
    MaxMemPerCPU: Callback = Callback()
    MaxMemPerNode: Callback = Callback()
    MaxNodeCount: Callback = Callback()
    MaxStepCount: Callback = Callback()
    MaxTasksPerNode: Callback = Callback()
    MCSParameters: Callback = Callback()
    MCSPlugin: Callback = Callback()
    MessageTimeout: Callback = Callback()
    MinJobAge: Callback = Callback()
    MpiDefault: Callback = Callback()
    MpiParams: Callback = Callback()
    OverTimeLimit: Callback = Callback()
    PluginDir: Callback = ColonSeparatorCallback
    PlugStackConfig: Callback = Callback()
    PowerParameters: Callback = SlurmDictCallback
    PowerPlugin: Callback = Callback()
    PreemptMode: Callback = CommaSeparatorCallback
    PreemptParameters: Callback = SlurmDictCallback
    PreemptType: Callback = Callback()
    PreemptExemptTime: Callback = Callback()
    PrEpParameters: Callback = Callback()
    PrEpPlugins: Callback = CommaSeparatorCallback
    PriorityCalcPeriod: Callback = Callback()
    PriorityDecayHalfLife: Callback = Callback()
    PriorityFavorSmall: Callback = Callback()
    PriorityFlags: Callback = Callback()
    PriorityMaxAge: Callback = Callback()
    PriorityParameters: Callback = Callback()
    PrioritySiteFactorParameters: Callback = Callback()
    PrioritySiteFactorPlugin: Callback = Callback()
    PriorityType: Callback = Callback()
    PriorityUsageResetPeriod: Callback = Callback()
    PriorityWeightAge: Callback = Callback()
    PriorityWeightAssoc: Callback = Callback()
    PriorityWeightFairshare: Callback = Callback()
    PriorityWeightJobSize: Callback = Callback()
    PriorityWeightPartition: Callback = Callback()
    PriorityWeightQOS: Callback = Callback()
    PriorityWeightTRES: Callback = SlurmDictCallback
    PrivateData: Callback = CommaSeparatorCallback
    ProctrackType: Callback = Callback()
    Prolog: Callback = Callback()
    PrologEpilogTimeout: Callback = Callback()
    PrologFlags: Callback = CommaSeparatorCallback
    PrologSlurmctld: Callback = Callback()
    PropagatePrioProcess: Callback = Callback()
    PropagateResourceLimits: Callback = CommaSeparatorCallback
    PropagateResourceLimitsExcept: Callback = CommaSeparatorCallback
    RebootProgram: Callback = QuoteCallback
    ReconfigFlags: Callback = Callback()
    KeepPartInfo: Callback = Callback()
    KeepPartState: Callback = Callback()
    KeepPowerSaveSettings: Callback = Callback()
    RequeueExit: Callback = Callback()
    RequeueExitHold: Callback = Callback()
    ResumeFailProgram: Callback = Callback()
    ResumeProgram: Callback = Callback()
    ResumeRate: Callback = Callback()
    ResumeTimeout: Callback = Callback()
    ResvEpilog: Callback = Callback()
    ResvOverRun: Callback = Callback()
    ResvProlog: Callback = Callback()
    ReturnToService: Callback = Callback()
    SchedulerParameters: Callback = SlurmDictCallback
    SchedulerTimeSlice: Callback = Callback()
    SchedulerType: Callback = Callback()
    ScronParameters: Callback = CommaSeparatorCallback
    SelectType: Callback = Callback()
    SelectTypeParameters: Callback = Callback()
    SlurmctldAddr: Callback = Callback()
    SlurmctldDebug: Callback = Callback()
    SlurmctldHost: Callback = Callback()
    SlurmctldLogFile: Callback = Callback()
    SlurmctldParameters: Callback = SlurmDictCallback
    SlurmctldPidFile: Callback = Callback()
    SlurmctldPort: Callback = Callback()
    SlurmctldPrimaryOffProg: Callback = Callback()
    SlurmctldPrimaryOnProg: Callback = Callback()
    SlurmctldSyslogDebug: Callback = Callback()
    SlurmctldTimeout: Callback = Callback()
    SlurmdDebug: Callback = Callback()
    SlurmdLogFile: Callback = Callback()
    SlurmdParameters: Callback = CommaSeparatorCallback
    SlurmdPidFile: Callback = Callback()
    SlurmdPort: Callback = Callback()
    SlurmdSpoolDir: Callback = Callback()
    SlurmdSyslogDebug: Callback = Callback()
    SlurmdTimeout: Callback = Callback()
    SlurmdUser: Callback = Callback()
    SlurmSchedLogFile: Callback = Callback()
    SlurmSchedLogLevel: Callback = Callback()
    SlurmUser: Callback = Callback()
    SrunEpilog: Callback = Callback()
    SrunPortRange: Callback = Callback()
    SrunProlog: Callback = Callback()
    StateSaveLocation: Callback = Callback()
    SuspendExcNodes: Callback = Callback()
    SuspendExcParts: Callback = Callback()
    SuspendExcStates: Callback = Callback()
    SuspendProgram: Callback = Callback()
    SuspendRate: Callback = Callback()
    SuspendTime: Callback = Callback()
    SuspendTimeout: Callback = Callback()
    SwitchParameters: Callback = SlurmDictCallback
    SwitchType: Callback = Callback()
    TaskEpilog: Callback = Callback()
    TaskPlugin: Callback = CommaSeparatorCallback
    TaskPluginParam: Callback = SlurmDictCallback
    Cores: Callback = Callback()
    Sockets: Callback = Callback()
    Threads: Callback = Callback()
    SlurmdOffSpec: Callback = Callback()
    Verbose: Callback = Callback()
    Autobind: Callback = Callback()
    TaskProlog: Callback = Callback()
    TCPTimeout: Callback = Callback()
    TmpFS: Callback = Callback()
    TopologyParam: Callback = CommaSeparatorCallback
    Dragonfly: Callback = Callback()
    RoutePart: Callback = Callback()
    SwitchAsNodeRank: Callback = Callback()
    RouteTree: Callback = Callback()
    TopoOptional: Callback = Callback()
    TopologyPlugin: Callback = Callback()
    TrackWCKey: Callback = Callback()
    TreeWidth: Callback = Callback()
    UnkillableStepProgram: Callback = Callback()
    UnkillableStepTimeout: Callback = Callback()
    UsePAM: Callback = Callback()
    VSizeFactor: Callback = Callback()
    WaitTime: Callback = Callback()
    X11Parameters: Callback = Callback()


@dataclass(frozen=True)
class NodeOptionSet(_OptionSet):
    """`slurm.conf` node configuration options."""

    NodeName: Annotated[Callback, "primary"] = Callback()
    NodeHostname: Callback = Callback()
    NodeAddr: Callback = Callback()
    BcastAddr: Callback = Callback()
    Boards: Callback = Callback()
    CoreSpecCount: Callback = Callback()
    CoresPerSocket: Callback = Callback()
    CpuBind: Callback = Callback()
    CPUs: Callback = Callback()
    CpuSpecList: Callback = CommaSeparatorCallback
    Features: Callback = CommaSeparatorCallback
    Gres: Callback = CommaSeparatorCallback
    MemSpecLimit: Callback = Callback()
    Port: Callback = Callback()
    Procs: Callback = Callback()
    RealMemory: Callback = Callback()
    Reason: Callback = QuoteCallback
    Sockets: Callback = Callback()
    SocketsPerBoard: Callback = Callback()
    State: Callback = Callback()
    ThreadsPerCore: Callback = Callback()
    TmpDisk: Callback = Callback()
    Weight: Callback = Callback()


@dataclass(frozen=True)
class DownNodeOptionSet(_OptionSet):
    """`slurm.conf` down node configuration options."""

    DownNodes: Callback = CommaSeparatorCallback
    Reason: Callback = QuoteCallback
    State: Callback = Callback()


@dataclass(frozen=True)
class FrontendNodeOptionSet(_OptionSet):
    """`slurm.conf` frontend node configuration options."""

    FrontendName: Annotated[Callback, "primary"] = Callback()
    FrontendAddr: Callback = Callback()
    AllowGroups: Callback = CommaSeparatorCallback
    AllowUsers: Callback = CommaSeparatorCallback
    DenyGroups: Callback = CommaSeparatorCallback
    DenyUsers: Callback = CommaSeparatorCallback
    Port: Callback = Callback()
    Reason: Callback = QuoteCallback
    State: Callback = Callback()


@dataclass(frozen=True)
class NodeSetOptionSet(_OptionSet):
    """`slurm.conf` node set configuration options."""

    NodeSet: Annotated[Callback, "primary"] = Callback()
    Feature: Callback = Callback()
    Nodes: Callback = CommaSeparatorCallback


@dataclass(frozen=True)
class PartitionOptionSet(_OptionSet):
    """`slurm.conf` partition configuration options."""

    PartitionName: Annotated[Callback, "primary"] = Callback()
    AllocNodes: Callback = CommaSeparatorCallback
    AllowAccounts: Callback = CommaSeparatorCallback
    AllowGroups: Callback = CommaSeparatorCallback
    AllowQos: Callback = CommaSeparatorCallback
    Alternate: Callback = Callback()
    CpuBind: Callback = Callback()
    Default: Callback = Callback()
    DefaultTime: Callback = Callback()
    DefCpuPerGPU: Callback = Callback()
    DefMemPerCPU: Callback = Callback()
    DefMemPerGPU: Callback = Callback()
    DefMemPerNode: Callback = Callback()
    DenyAccounts: Callback = CommaSeparatorCallback
    DenyQos: Callback = CommaSeparatorCallback
    DisableRootJobs: Callback = Callback()
    ExclusiveUser: Callback = Callback()
    GraceTime: Callback = Callback()
    Hidden: Callback = Callback()
    LLN: Callback = Callback()
    MaxCPUsPerNode: Callback = Callback()
    MaxCPUsPerSocket: Callback = Callback()
    MaxMemPerCPU: Callback = Callback()
    MaxMemPerNode: Callback = Callback()
    MaxNodes: Callback = Callback()
    MaxTime: Callback = Callback()
    MinNodes: Callback = Callback()
    Nodes: Callback = CommaSeparatorCallback
    OverSubscribe: Callback = Callback()
    OverTimeLimit: Callback = Callback()
    PowerDownOnIdle: Callback = Callback()
    PreemptMode: Callback = Callback()
    PriorityJobFactor: Callback = Callback()
    PriorityTier: Callback = Callback()
    QOS: Callback = Callback()
    ReqResv: Callback = Callback()
    ResumeTimeout: Callback = Callback()
    RootOnly: Callback = Callback()
    SelectTypeParameters: Callback = Callback()
    State: Callback = Callback()
    SuspendTime: Callback = Callback()
    SuspendTimeout: Callback = Callback()
    TRESBillingWeights: Callback = SlurmDictCallback
