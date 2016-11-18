# Route

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | App this route belongs to. | [optional] 
**path** | **str** | URL path that will be matched to this route | [optional] 
**image** | **str** | Name of Docker image to use in this route. You should include the image tag, which should be a version number, to be more accurate. Can be overridden on a per route basis with route.image. | [optional] 
**headers** | **str** | Map of http headers that will be sent with the response | [optional] 
**memory** | **int** | Max usable memory for this route (MiB). | [optional] 
**type** | **str** | Route type | [optional] 
**config** | **dict(str, str)** | Route configuration - overrides application configuration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


