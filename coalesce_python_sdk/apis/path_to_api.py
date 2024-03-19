import typing_extensions

from coalesce_python_sdk.paths import PathValues
from coalesce_python_sdk.apis.paths.scheduler_start_run import SchedulerStartRun
from coalesce_python_sdk.apis.paths.scheduler_run_status import SchedulerRunStatus
from coalesce_python_sdk.apis.paths.scheduler_rerun import SchedulerRerun
from coalesce_python_sdk.apis.paths.scheduler_cancel_run import SchedulerCancelRun
from coalesce_python_sdk.apis.paths.api_v1_environments import ApiV1Environments
from coalesce_python_sdk.apis.paths.api_v1_environments_environment_id import ApiV1EnvironmentsEnvironmentID
from coalesce_python_sdk.apis.paths.api_v1_environments_environment_id_nodes import ApiV1EnvironmentsEnvironmentIDNodes
from coalesce_python_sdk.apis.paths.api_v1_environments_environment_id_nodes_node_id import ApiV1EnvironmentsEnvironmentIDNodesNodeID
from coalesce_python_sdk.apis.paths.api_v1_runs import ApiV1Runs
from coalesce_python_sdk.apis.paths.api_v1_runs_run_id import ApiV1RunsRunID
from coalesce_python_sdk.apis.paths.api_v1_runs_run_id_results import ApiV1RunsRunIDResults

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SCHEDULER_START_RUN: SchedulerStartRun,
        PathValues.SCHEDULER_RUN_STATUS: SchedulerRunStatus,
        PathValues.SCHEDULER_RERUN: SchedulerRerun,
        PathValues.SCHEDULER_CANCEL_RUN: SchedulerCancelRun,
        PathValues.API_V1_ENVIRONMENTS: ApiV1Environments,
        PathValues.API_V1_ENVIRONMENTS_ENVIRONMENT_ID: ApiV1EnvironmentsEnvironmentID,
        PathValues.API_V1_ENVIRONMENTS_ENVIRONMENT_ID_NODES: ApiV1EnvironmentsEnvironmentIDNodes,
        PathValues.API_V1_ENVIRONMENTS_ENVIRONMENT_ID_NODES_NODE_ID: ApiV1EnvironmentsEnvironmentIDNodesNodeID,
        PathValues.API_V1_RUNS: ApiV1Runs,
        PathValues.API_V1_RUNS_RUN_ID: ApiV1RunsRunID,
        PathValues.API_V1_RUNS_RUN_ID_RESULTS: ApiV1RunsRunIDResults,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SCHEDULER_START_RUN: SchedulerStartRun,
        PathValues.SCHEDULER_RUN_STATUS: SchedulerRunStatus,
        PathValues.SCHEDULER_RERUN: SchedulerRerun,
        PathValues.SCHEDULER_CANCEL_RUN: SchedulerCancelRun,
        PathValues.API_V1_ENVIRONMENTS: ApiV1Environments,
        PathValues.API_V1_ENVIRONMENTS_ENVIRONMENT_ID: ApiV1EnvironmentsEnvironmentID,
        PathValues.API_V1_ENVIRONMENTS_ENVIRONMENT_ID_NODES: ApiV1EnvironmentsEnvironmentIDNodes,
        PathValues.API_V1_ENVIRONMENTS_ENVIRONMENT_ID_NODES_NODE_ID: ApiV1EnvironmentsEnvironmentIDNodesNodeID,
        PathValues.API_V1_RUNS: ApiV1Runs,
        PathValues.API_V1_RUNS_RUN_ID: ApiV1RunsRunID,
        PathValues.API_V1_RUNS_RUN_ID_RESULTS: ApiV1RunsRunIDResults,
    }
)
