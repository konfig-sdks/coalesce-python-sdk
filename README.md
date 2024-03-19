<div align="center">

[![Visit Coalesce](./header.png)](https://coalesce.io&#x2F;)

# Coalesce<a id="coalesce"></a>

REST API for performing operations with the Coalesce backend.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`coalesce.environments.get_information`](#coalesceenvironmentsget_information)
  * [`coalesce.environments.list_information`](#coalesceenvironmentslist_information)
  * [`coalesce.jobs.cancel_job_run`](#coalescejobscancel_job_run)
  * [`coalesce.jobs.get_status_updates`](#coalescejobsget_status_updates)
  * [`coalesce.jobs.initiate_run`](#coalescejobsinitiate_run)
  * [`coalesce.jobs.trigger_rerun`](#coalescejobstrigger_rerun)
  * [`coalesce.nodes.get_information`](#coalescenodesget_information)
  * [`coalesce.nodes.list`](#coalescenodeslist)
  * [`coalesce.runs.get_run_details`](#coalescerunsget_run_details)
  * [`coalesce.runs.list_information`](#coalescerunslist_information)
  * [`coalesce.runs.list_results`](#coalescerunslist_results)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Coalesce&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from coalesce_python_sdk import Coalesce, ApiException

coalesce = Coalesce(access_token="YOUR_BEARER_TOKEN")

try:
    # Get Environment
    get_information_response = coalesce.environments.get_information(
        environment_id="environmentID_example",
    )
    print(get_information_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi.get_information: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
    if e.status == 500:
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["error"])
    if e.status == 502:
        pprint(e.body["error"])
    if e.status == 404:
        pprint(e.body["error"])
    if e.status == 503:
        pprint(e.body["error"])
    if e.status == 504:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from coalesce_python_sdk import Coalesce, ApiException

coalesce = Coalesce(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Get Environment
        get_information_response = await coalesce.environments.aget_information(
            environment_id="environmentID_example",
        )
        print(get_information_response)
    except ApiException as e:
        print("Exception when calling EnvironmentsApi.get_information: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["error"])
        if e.status == 500:
            pprint(e.body["error"])
        if e.status == 403:
            pprint(e.body["error"])
        if e.status == 502:
            pprint(e.body["error"])
        if e.status == 404:
            pprint(e.body["error"])
        if e.status == 503:
            pprint(e.body["error"])
        if e.status == 504:
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from coalesce_python_sdk import Coalesce, ApiException

coalesce = Coalesce(access_token="YOUR_BEARER_TOKEN")

try:
    # Get Environment
    get_information_response = coalesce.environments.raw.get_information(
        environment_id="environmentID_example",
    )
    pprint(get_information_response.body)
    pprint(get_information_response.body["description"])
    pprint(get_information_response.body["connection_account"])
    pprint(get_information_response.body["default_storage_mapping"])
    pprint(get_information_response.body["name"])
    pprint(get_information_response.body["oauth_enabled"])
    pprint(get_information_response.body["run_time_parameters"])
    pprint(get_information_response.body["tag_colors"])
    pprint(get_information_response.body["project"])
    pprint(get_information_response.headers)
    pprint(get_information_response.status)
    pprint(get_information_response.round_trip_time)
except ApiException as e:
    print("Exception when calling EnvironmentsApi.get_information: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
    if e.status == 500:
        pprint(e.body["error"])
    if e.status == 403:
        pprint(e.body["error"])
    if e.status == 502:
        pprint(e.body["error"])
    if e.status == 404:
        pprint(e.body["error"])
    if e.status == 503:
        pprint(e.body["error"])
    if e.status == 504:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `coalesce.environments.get_information`<a id="coalesceenvironmentsget_information"></a>

Get information about an environment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = coalesce.environments.get_information(
    environment_id="environmentID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### environment_id: `str`<a id="environment_id-str"></a>

The environment ID.

#### 🔄 Return<a id="🔄-return"></a>

[`BaseEnvironment`](./coalesce_python_sdk/pydantic/base_environment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/environments/{environmentID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.environments.list_information`<a id="coalesceenvironmentslist_information"></a>

Get a collection of environment information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_information_response = coalesce.environments.list_information(
    detail=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### detail: `bool`<a id="detail-bool"></a>

Include the full detail of the environments.

#### 🔄 Return<a id="🔄-return"></a>

[`EnvironmentsResponse`](./coalesce_python_sdk/pydantic/environments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/environments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.jobs.cancel_job_run`<a id="coalescejobscancel_job_run"></a>

Querying this endpoint will cancel a currently running job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_job_run_response = coalesce.jobs.cancel_job_run(
    run_id=1,
    org_id="string_example",
    environment_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_id: `int`<a id="run_id-int"></a>

The ID of the run the user would like to cancel.

##### org_id: `str`<a id="org_id-str"></a>

The organization's ID of the run the user would like to cancel.

##### environment_id: `str`<a id="environment_id-str"></a>

The environment ID of the run the user would like to cancel.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsCancelJobRunRequest`](./coalesce_python_sdk/type/jobs_cancel_job_run_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/scheduler/cancelRun` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.jobs.get_status_updates`<a id="coalescejobsget_status_updates"></a>

Querying this endpoint will allow you to receive updates on the current status of a specific run.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_status_updates_response = coalesce.jobs.get_status_updates(
    run_counter=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_counter: `int`<a id="run_counter-int"></a>

ID of the run to query

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetStatusUpdatesResponse`](./coalesce_python_sdk/pydantic/jobs_get_status_updates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/scheduler/runStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.jobs.initiate_run`<a id="coalescejobsinitiate_run"></a>

Querying this endpoint will initiate a new run to refresh your data warehouse based on your specified details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_run_response = coalesce.jobs.initiate_run(
    run_details={
        "environment_id": "environment_id_example",
        "parallelism": 16,
    },
    parameters="string_example",
    user_credentials={
        "snowflake_auth_type": "Basic",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_details: [`JobsInitiateRunRequestRunDetails`](./coalesce_python_sdk/type/jobs_initiate_run_request_run_details.py)<a id="run_details-jobsinitiaterunrequestrundetailscoalesce_python_sdktypejobs_initiate_run_request_run_detailspy"></a>


##### parameters: `str`<a id="parameters-str"></a>

Contains parameters to be used in the Refresh

##### user_credentials: [`JobsInitiateRunRequestUserCredentials`](./coalesce_python_sdk/type/jobs_initiate_run_request_user_credentials.py)<a id="user_credentials-jobsinitiaterunrequestusercredentialscoalesce_python_sdktypejobs_initiate_run_request_user_credentialspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsInitiateRunRequest`](./coalesce_python_sdk/type/jobs_initiate_run_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsInitiateRunResponse`](./coalesce_python_sdk/pydantic/jobs_initiate_run_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/scheduler/startRun` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.jobs.trigger_rerun`<a id="coalescejobstrigger_rerun"></a>

Querying this endpoint will initiate a new run to refresh your data warehouse based on your specified details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_rerun_response = coalesce.jobs.trigger_rerun(
    run_details={
        "run_id": "run_id_example",
    },
    user_credentials={
        "snowflake_auth_type": "Basic",
    },
    parameters="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_details: [`JobsTriggerRerunRequestRunDetails`](./coalesce_python_sdk/type/jobs_trigger_rerun_request_run_details.py)<a id="run_details-jobstriggerrerunrequestrundetailscoalesce_python_sdktypejobs_trigger_rerun_request_run_detailspy"></a>


##### user_credentials: [`JobsTriggerRerunRequestUserCredentials`](./coalesce_python_sdk/type/jobs_trigger_rerun_request_user_credentials.py)<a id="user_credentials-jobstriggerrerunrequestusercredentialscoalesce_python_sdktypejobs_trigger_rerun_request_user_credentialspy"></a>


##### parameters: `str`<a id="parameters-str"></a>

Contains parameters to be used in the Refresh

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsTriggerRerunRequest`](./coalesce_python_sdk/type/jobs_trigger_rerun_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobsTriggerRerunResponse`](./coalesce_python_sdk/pydantic/jobs_trigger_rerun_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/scheduler/rerun` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.nodes.get_information`<a id="coalescenodesget_information"></a>

Get information about a node in an environment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_information_response = coalesce.nodes.get_information(
    environment_id="environmentID_example",
    node_id="nodeID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### environment_id: `str`<a id="environment_id-str"></a>

The environment ID.

##### node_id: `str`<a id="node_id-str"></a>

The node ID.

#### 🔄 Return<a id="🔄-return"></a>

[`Node`](./coalesce_python_sdk/pydantic/node.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/environments/{environmentID}/nodes/{nodeID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.nodes.list`<a id="coalescenodeslist"></a>

Get a collection of nodes for an environment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = coalesce.nodes.list(
    environment_id="environmentID_example",
    detail=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### environment_id: `str`<a id="environment_id-str"></a>

The environment ID.

##### detail: `bool`<a id="detail-bool"></a>

Include the full detail of the nodes.

#### 🔄 Return<a id="🔄-return"></a>

[`NodesResponse`](./coalesce_python_sdk/pydantic/nodes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/environments/{environmentID}/nodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.runs.get_run_details`<a id="coalescerunsget_run_details"></a>

Gets a single run.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_run_details_response = coalesce.runs.get_run_details(
    run_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_id: `int`<a id="run_id-int"></a>

The run ID.

#### 🔄 Return<a id="🔄-return"></a>

[`RunInfo`](./coalesce_python_sdk/pydantic/run_info.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/runs/{runID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.runs.list_information`<a id="coalescerunslist_information"></a>

Get a collection of information about runs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_information_response = coalesce.runs.list_information(
    limit=25,
    starting_from=None,
    order_by="id",
    order_by_direction="desc",
    run_type="deploy",
    run_status="canceled",
    environment_id="string_example",
    detail=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of runs to return.

##### starting_from: Union[`int`, `datetime`]<a id="starting_from-unionint-datetime"></a>


The starting run ID, runStartTime, or runEndTime (exclusive) for paging the query results.

##### order_by: [`RunsOrderBy`](./coalesce_python_sdk/type/.py)<a id="order_by-runsorderbycoalesce_python_sdktypepy"></a>

The field used to order results.

##### order_by_direction: `str`<a id="order_by_direction-str"></a>

The sort order for query results.

##### run_type: [`RunType`](./coalesce_python_sdk/type/.py)<a id="run_type-runtypecoalesce_python_sdktypepy"></a>

A run type to filter the query results.

##### run_status: [`RunStatus`](./coalesce_python_sdk/type/.py)<a id="run_status-runstatuscoalesce_python_sdktypepy"></a>

A status value to filter the query results.

##### environment_id: `str`<a id="environment_id-str"></a>

An environment ID to filter the query results.

##### detail: `bool`<a id="detail-bool"></a>

Include the full detail of the run.

#### 🔄 Return<a id="🔄-return"></a>

[`RunsResponse`](./coalesce_python_sdk/pydantic/runs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/runs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `coalesce.runs.list_results`<a id="coalescerunslist_results"></a>

Get a collection of the results of a deploy or refresh run

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_results_response = coalesce.runs.list_results(
    run_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_id: `int`<a id="run_id-int"></a>

The run ID.

#### 🔄 Return<a id="🔄-return"></a>

[`RunResultsResponse`](./coalesce_python_sdk/pydantic/run_results_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/runs/{runID}/results` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
