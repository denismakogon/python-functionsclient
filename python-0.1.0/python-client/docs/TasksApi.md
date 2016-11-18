# swagger_client.TasksApi

All URIs are relative to *https://127.0.0.1:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_get**](TasksApi.md#tasks_get) | **GET** /tasks | Get next task.


# **tasks_get**
> TaskWrapper tasks_get(n=n)

Get next task.

Gets the next task in the queue, ready for processing. Titan may return <=n tasks. Consumers should start processing tasks in order. Each returned task is set to `status` \"running\" and `started_at` is set to the current time. No other consumer can retrieve this task.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TasksApi()
n = 1 # int | Number of tasks to return. (optional) (default to 1)

try: 
    # Get next task.
    api_response = api_instance.tasks_get(n=n)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| Number of tasks to return. | [optional] [default to 1]

### Return type

[**TaskWrapper**](TaskWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

