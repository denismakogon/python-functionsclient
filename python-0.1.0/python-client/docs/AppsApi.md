# swagger_client.AppsApi

All URIs are relative to *https://127.0.0.1:8080/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_app_get**](AppsApi.md#apps_app_get) | **GET** /apps/{app} | Get information for a app.
[**apps_app_put**](AppsApi.md#apps_app_put) | **PUT** /apps/{app} | Create/update a app.
[**apps_get**](AppsApi.md#apps_get) | **GET** /apps | Get all app names.
[**apps_post**](AppsApi.md#apps_post) | **POST** /apps | Post new app


# **apps_app_get**
> AppWrapper apps_app_get(app)

Get information for a app.

This gives more details about a app, such as statistics.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
app = 'app_example' # str | name of the app.

try: 
    # Get information for a app.
    api_response = api_instance.apps_app_get(app)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_app_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_app_put**
> AppWrapper apps_app_put(app, body)

Create/update a app.

You can set app level settings here. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
app = 'app_example' # str | name of the app.
body = swagger_client.AppWrapper() # AppWrapper | App to post.

try: 
    # Create/update a app.
    api_response = api_instance.apps_app_put(app, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_app_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | **str**| name of the app. | 
 **body** | [**AppWrapper**](AppWrapper.md)| App to post. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get**
> AppsWrapper apps_get()

Get all app names.

Get a list of all the apps in the system.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()

try: 
    # Get all app names.
    api_response = api_instance.apps_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppsWrapper**](AppsWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_post**
> AppWrapper apps_post(body)

Post new app

Insert a new app

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppsApi()
body = swagger_client.AppWrapper() # AppWrapper | App to post.

try: 
    # Post new app
    api_response = api_instance.apps_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->apps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppWrapper**](AppWrapper.md)| App to post. | 

### Return type

[**AppWrapper**](AppWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

