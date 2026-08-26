# Assets API

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/assets-api>

To integrate Assets APIs, follow the steps below:

- **Fetch All**: This API retrieves all assets available in a specified folder on the platform. The following JSON example illustrates a sample request for this API:
    Copy CodeJSON{
    "folderName": "TestFolder2",
    "version": "1.0.0",
    "pageNumber": 1,
    "pageSize": 10,
    "searchKey": "reels-media-collection-file-upload-metadata"
   }
    Upon successful execution of the request, the response returns a list of all assets available in the specified folder. If a searchKey is provided, the response is filtered to return assets that match the specified value. The searchKey parameter is optional. If the folderName or version parameter is not supplied, the API returns an error indicating that both fields are mandatory. Without these required parameters, assets in the folder cannot be retrieved. The following JSON example shows a sample successful response.
    **Note**: The searchKey parameter filters assets by matching a specified metadata field value provided during asset creation.
    Copy CodeJSON{
    "success": true,
    "data": [
    {
    "id": "9696ccff-ab9d-4c47-b7a5-564a5f6b0e2b",
    "fileId": "d7b90c81-bdde-4a4a-9d82-6c4ab5847264",
    "disabled": false,
    "fileName": "reels-media-collection-file-upload-metadata.png",
    "fileSize": 105935,
    "metaData": {
    "fileName": "reels-media-collection-file-upload-metadata",
    "fileType": "png"
    },
    "createdAt": "2026-01-12T07:56:11.897Z",
    "updatedAt": "2026-01-12T07:56:11.897Z",
    "fileExtension": "png",
    "thumbnailBase64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABqElEQVR4nO3cy03DUBBG4em/BqAUJGBFDRTADsgDO487MwiyQK7gnsX5pF9iGenIduxYRAslZn8AbRkExiAwBoGJkdWuMIuqbteYecqCMQjM3ylLHB4hMPH+dfvDI4UhHp4vvzn6sFYvZ7dMXtw//QbJ/jxm7xe3n7x4eLkF2S3Zx5M7Tl7cPZ67a/THYfTu2+0mL17fTn8Xk8u1egw3Ji+qqtM1ZfEFOEzd+D9lHdZsl5gZZGUtZn/vdrm9Dzlfq11hFlndrjGL66h2hZmP32EMAuMpa7AWmdWuMPO9rGTN97KKtfg+ZbvEzEcnC2s+XFxZM8jKWsz+Ud/l9iWH2Xem2vJOfbDmfUix5ikLxiAwcRnVrjDzGlKs+bQ3WfMaAmMQGIPAGATGIDAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWAMAmMQGIPAGATGIDAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWAMAuP/7R2seYTAGATGIDAGgTEIjEGa5Qf7FxOKAKCH6wAAAABJRU5ErkJggg=="
    }
    ],
    "meta": {
    "totalCount": 1,
    "pageNumber": 1,
    "pageSize": 10,
    "totalPages": 1
    },
    "timestamp": "2026-01-12T10:15:02.190Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **folderName**: Specifies the name of the folder from which the assets are retrieved.
  - **version**: Specifies the folder version from which the assets are to be retrieved.
  - **pageNumber**: Specifies the page number from which the available assets are to be retrieved.
  - **pageSize**: Specifies the number of assets to be displayed on a single page.
  - **searchKey**: Specifies the search key used to filter and retrieve assets based on the metadata provided when the asset was added. This field is optional.
- **Add New Asset**: Adding a new asset is the process of uploading a media file to a media collection folder on the platform for discovery, management, and downstream use. The following image illustrates a sample request for this API:
    ![reels-media-collection-asset-add-integration-api](/resources/Storage/neutrinos-reels-publication/images/reels-media-collection-asset-add-integration-api.png)
    Upon successful execution of the request, the response returns a success message indicating that the file was successfully uploaded to the media collection folder. The following JSON example shows a sample successful response:
    Copy CodeJSON{
    "success": true,
    "data": {
    "fileName": "reels-dashboard-image.png",
    "fileExtension": "png",
    "fileId": "6d15888e-767d-4aa2-93bc-d3dfd8542e97",
    "fileSize": 179003,
    "createdAt": "2026-01-12T09:18:44.466Z"
    },
    "timestamp": "2026-01-12T09:18:44.472Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **folederName**: Specifies the name of the folder to which the assets are added.
  - **version**: Specifies the folder version to which the assets are added.
  - **metaData**: Specifies asset metadata for the media collection folder. This field is required if metadata fields were defined during folder creation; otherwise, it is optional. When required, metadata details must be supplied in JSON format. If this field is mandatory and no value is provided, the API returns an error indicating that required metadata values are missing.
  - **file**: Specifies the file that is being uploaded to the folder.
- **Update Asset**: Updating an asset refers to the process of modifying an existing media asset that is already stored within a media collection folder or adding a new asset to the folder. This operation allows updates to the asset’s content and/or its associated metadata while preserving the asset’s identity and its association with the media collection folder.
    To perform an update operation, the assetId must be provided. If metadata fields were defined during the creation of the media collection folder, then supplying values for those metadata fields as a JSON payload is mandatory as part of the update request. If the required metadata values are not provided, the system returns an error response and the update operation fails.
    For example, the following image illustrates a sample request for updating an asset schema.
    ![reels-media-collection-asset-update-integration-api](/resources/Storage/neutrinos-reels-publication/images/reels-media-collection-asset-update-integration-api.png)
    After the successful execution of the above request, a success message is displayed, and the updated details for the asset are returned as the output.
    Copy CodeJSON{
    "success": true,
    "data": {
    "fileId": "6835da8c-b1b6-4481-b905-8465dca29b0e",
    "fileName": "",
    "fileExtension": "",
    "author": "",
    "fileSize": 0,
    "createdAt": "2026-01-12T12:40:41.674Z"
    },
    "timestamp": "2026-01-12T12:40:41.674Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **folderName**: Specifies the name of the folder to which the assets are added.
  - **version**: Specifies the folder version to which the assets are added.
  - **id**: Specifies the asset ID associated with the target asset in the media collection folder. This ID uniquely identifies the asset and can be retrieved from the platform UI.
  - **metaData**: Specifies asset metadata for the media collection folder. This field is required if metadata fields were defined during folder creation; otherwise, it is optional. When required, metadata details must be supplied in JSON format. If this field is mandatory and no value is provided, the API returns an error indicating that required metadata values are missing.
  - **file**: Specifies the media file to be uploaded or updated in the media collection folder. This field is optional if the update is performed on an existing asset without modifying the file content.
      **Note**: When a new file is supplied as part of the Update Asset API request, the platform adds the new file to the media collection folder while preserving the previously existing file.
- **Remove Asset**: Removing an asset deletes an existing media asset from the platform. The following JSON example shows a sample removal request.
    Copy CodeJSON{
    "folderName": "TestFolder2",
    "version": "1.0.0",
    "id": "eea080d9-8789-4a22-a0bb-9eb90f2f027f"
   }
    Upon successful execution of the request, a success message is returned, along with the details of the removed asset in the response. The following JSON example shows a sample successful response:
    Copy CodeJSON{
    "success": true,
    "message": "File removed successfully"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **folderName**: Specifies the name of the folder to which the assets are added.
  - **version**: Specifies the folder version to which the assets are added.
  - **id**: Specifies the asset ID associated with the target asset in the media collection folder. This ID uniquely identifies the asset and is used to remove the asset from the platform.
- **Filter Assets**: Asset filtering refer to the subset of media assets retrieved from platform based on one or more specified filter criteria. Filtering enables users to narrow down asset results to only those that match defined criteria. The following JSON example shows a sample filter asset request:
    Copy CodeJSON{
    "folderName": "TestFolder2",
    "version": "1.0.0",
    "filters": {
    "fileType": "png"
    }
   }
    Upon successful execution of the request, a success message is returned, along with the asset(s) that matched the filter criteria. The following JSON example shows a sample successful response:
    Copy CodeJSON{
    "success": true,
    "data": [
    {
    "id": "eea080d9-8789-4a22-a0bb-9eb90f2f027f",
    "fileId": "6835da8c-b1b6-4481-b905-8465dca29b0e",
    "disabled": true,
    "fileName": "IMG_20251115_135616.jpg",
    "fileSize": 3056165,
    "metaData": {
    "fileName": "bca",
    "fileType": "png"
    },
    "createdAt": "2026-01-12T10:57:43.834Z",
    "createdBy": "muhammed.fawaz@neutrinos.co",
    "updatedAt": "2026-01-12T12:40:41.669Z",
    "fileExtension": "jpg"
    },
    {
    "id": "1ccd47d0-40e6-482e-bd03-8286799dd387",
    "fileId": "6d15888e-767d-4aa2-93bc-d3dfd8542e97",
    "disabled": false,
    "fileName": "reels-dashboard-image.png",
    "fileSize": 179003,
    "metaData": {
    "fileName": "abc",
    "fileType": "png"
    },
    "createdAt": "2026-01-12T09:18:44.466Z",
    "updatedAt": "2026-01-12T09:18:44.466Z",
    "fileExtension": "png"
    },
    {
    "id": "9696ccff-ab9d-4c47-b7a5-564a5f6b0e2b",
    "fileId": "d7b90c81-bdde-4a4a-9d82-6c4ab5847264",
    "disabled": false,
    "fileName": "reels-media-collection-file-upload-metadata.png",
    "fileSize": 105935,
    "metaData": {
    "fileName": "reels-media-collection-file-upload-metadata",
    "fileType": "png"
    },
    "createdAt": "2026-01-12T07:56:11.897Z",
    "updatedAt": "2026-01-12T07:56:11.897Z",
    "fileExtension": "png"
    }
    ],
    "timestamp": "2026-01-13T05:48:23.966Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **folderName**: Specifies the name of the folder to which the assets are added.
  - **version**: Specifies the folder version to which the assets are added.
  - **filters**: Specifies the criteria for filtering assets based on the selected requirements.
- **Get Asset File**: The Get Asset File API retrieves a specific file from the platform using the file ID provided as a request parameter. The file ID corresponds to the identifier returned by the Add Asset API during asset creation. The image below illustrates a sample Get Asset File request:
    ![reels-media-collection-asset-get-asset-file-integration-api-request](/resources/Storage/neutrinos-reels-publication/reels-media-collection-asset-get-asset-file-integration-api-request.png)
    Upon successful execution of the request, the file matching the file id passed in the request is returned. The image below illustrates a sample response:
    ![reels-media-collection-asset-get-asset-file-integration-api-response](/resources/Storage/neutrinos-reels-publication/reels-media-collection-asset-get-asset-file-integration-api-response.png)
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **Path Variable**: Specifies the file ID of the file to be retrieved from the media collection folder on the platform.
