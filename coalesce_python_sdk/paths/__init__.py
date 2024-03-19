# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from coalesce_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SCHEDULER_START_RUN = "/scheduler/startRun"
    SCHEDULER_RUN_STATUS = "/scheduler/runStatus"
    SCHEDULER_RERUN = "/scheduler/rerun"
    SCHEDULER_CANCEL_RUN = "/scheduler/cancelRun"
    API_V1_ENVIRONMENTS = "/api/v1/environments"
    API_V1_ENVIRONMENTS_ENVIRONMENT_ID = "/api/v1/environments/{environmentID}"
    API_V1_ENVIRONMENTS_ENVIRONMENT_ID_NODES = "/api/v1/environments/{environmentID}/nodes"
    API_V1_ENVIRONMENTS_ENVIRONMENT_ID_NODES_NODE_ID = "/api/v1/environments/{environmentID}/nodes/{nodeID}"
    API_V1_RUNS = "/api/v1/runs"
    API_V1_RUNS_RUN_ID = "/api/v1/runs/{runID}"
    API_V1_RUNS_RUN_ID_RESULTS = "/api/v1/runs/{runID}/results"
