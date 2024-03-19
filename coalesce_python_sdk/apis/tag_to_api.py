import typing_extensions

from coalesce_python_sdk.apis.tags import TagValues
from coalesce_python_sdk.apis.tags.jobs_api import JobsApi
from coalesce_python_sdk.apis.tags.runs_api import RunsApi
from coalesce_python_sdk.apis.tags.environments_api import EnvironmentsApi
from coalesce_python_sdk.apis.tags.nodes_api import NodesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.JOBS: JobsApi,
        TagValues.RUNS: RunsApi,
        TagValues.ENVIRONMENTS: EnvironmentsApi,
        TagValues.NODES: NodesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.JOBS: JobsApi,
        TagValues.RUNS: RunsApi,
        TagValues.ENVIRONMENTS: EnvironmentsApi,
        TagValues.NODES: NodesApi,
    }
)
