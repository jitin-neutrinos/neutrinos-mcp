# Filter Records

<https://documentation.neutrinos.com/articles/#!pulse-publication/integrate-master-data>

To integrate a Master Data, follow the steps below:

1. In the sub-module navigation bar, click **Master Data**, then choose a specific master data to open its details page. On the details page, navigate to the **Details **section and click **Download Swagger**.
    ![master-data-download-swagger](/resources/Storage/pulse-publication/images/master-data-download-swagger.png)
2. Open the Swagger documentation (import) downloaded from the Reels platform.
    ![swagger-import-master-data](/resources/Storage/pulse-publication/images/swagger-import-master-data1.gif)
    The Swagger for any workflow contains the following API endpoints:
    ![swagger-master-data-endpoints](/resources/Storage/pulse-publication/images/swagger-master-data-endpoints1.png)
  1. **Filter**: Retrieves a list of records that match the specified filter criteria. You can define these criteria in the filter section of the JSON request. Additionally, you can specify the columns to be included in the results using the select section. Use the appropriate column selection settings to retrieve distinct values and eliminate redundancy.
  2. **Update**: Retrieves records that match the specified criteria and updates the data in a specific column as defined in the API.
  3. **Delete**: Deletes the records that match the specified criteria.
  4. **Add**: Adds a new record to the Master Data using the details specified in the API call. Ensure that all column values in the Master Data are provided when the API is called, or an error will be returned.

## Filter Records

After importing the Master Data JSON into Swagger, follow these steps to execute the Filter API endpoint:

1. Click the **Authorize** button in Swagger. Provide the bearer token obtained from IDS by entering "Bearer " followed by a space and then pasting the token. Alternatively, you can use a token generated from the Reels platform for authorization.
2. Navigate to the Filter endpoint. Expand its section, click the **Try it out** button to enable editing:
  1. **datasetID**: Specifies the datasetID of the master data. This field is pre-filled and does not require editing.
  2. **entityID**: Specifies the entityID of the master data. This field is pre-filled and does not require editing.
  3. **mdmID**: Specifies the mdmID of the master data. This field is pre-filled and does not require editing.
3. In the Request Body section, specify the details required by the parameters to fetch the information from the master data.
  1. pageNumber: 0 indicates that the search starts from the first page while applying the specified filter criteria.
  2. pageSize: Limits the results to the number of pages, with records per page as specified.
  3. multiplicity: Specifies whether a single record or multiple records are retrieved.
  4. filter: Accepts filtering criteria to retrieve information from the master data. Only records meeting this condition will be included in the results.
  5. select: Specifies the columns to be included in the response.
  6. distinct: Ensures that unique values of the specified column appear in the result set. Even if multiple records have the same column, only one unique entry per column will be returned.
4. Click the **Execute** button to run the API. The result will be returned and can be viewed by scrolling down the page. Note that a 200 status code indicates a successful execution. If an error occurs during execution, a specific error code will be returned.

The GIF below demonstrates how to use the Filter API in Swagger to filter records from the master data.




 ![swagger-execute-master-data](/resources/Storage/pulse-publication/images/swagger-execute-master-data.gif)

## Update Record

After importing the Master Data JSON into Swagger, follow these steps to execute the Update API endpoint:

1. Click the **Authorize** button in Swagger. Provide the bearer token obtained from IDS by entering "Bearer " followed by a space and then pasting the token. Alternatively, you can use a token generated from the Reels platform for authorization.
2. Navigate to the Update endpoint. Expand its section, click the Try it out button to enable editing:
  1. **datasetID**: Specifies the datasetID of the master data. This field is pre-filled and does not require editing.
  2. **entityID**: Specifies the entityID of the master data. This field is pre-filled and does not require editing.
  3. **mdmID**: Specifies the mdmID of the master data. This field is pre-filled and does not require editing.
3. In the Request Body section, specify the required parameter details to retrieve information from the master data and update it. The update endpoint consists of two parts: a filter section and an update section. The API first retrieves the records that match the filter criteria, then updates the specified column values with those provided in the update section.
4. The sample schema includes predefined filter criteria that can be customized based on the column names in the master data. After configuring the filter criteria to retrieve a specific record, enter the column names and their corresponding values in the update section to apply the updates. The image below illustrates the sample schema:
    ![swagger-master-data-update-endpoint](/resources/Storage/pulse-publication/images/swagger-master-data-update-endpoint.png)
5. Click the **Execute** button to run the API. The result will be returned and viewed by scrolling down the page. Note that a 200 status code indicates a successful execution. If an error occurs during execution, a specific error code will be returned.

The GIF below demonstrates how to execute the Update API endpoint in Swagger to modify a record in the master data. In this example, the age value is updated from 30 to 45 by applying a filter to identify the specific record:




 ![swagger-master-data-update-api-complete](/resources/Storage/pulse-publication/images/swagger-master-data-update-api-complete.gif)

## Delete Record

After importing the Master Data JSON into Swagger, follow these steps to execute the Delete API endpoint:

1. Click the **Authorize** button in Swagger. Provide the bearer token obtained from IDS by entering "Bearer " followed by a space and then pasting the token. Alternatively, you can use a token generated from the Reels platform for authorization.
2. Navigate to the Delete endpoint. Expand its section, click the Try it out button to enable editing:
  1. **datasetID**: Specifies the datasetID of the master data. This field is pre-filled and does not require editing.
  2. **entityID**: Specifies the entityID of the master data. This field is pre-filled and does not require editing.
  3. **mdmID**: Specifies the mdmID of the master data. This field is pre-filled and does not require editing.
3. In the Request Body section, specify the required parameter details to delete information from the master data. The deleteArray section accepts all the column values to match the record in the master data and deletes the matching record.
4. The sample schema includes a predefined deleteArray section that can be customized based on the column names in the master data. Enter the relevant column names and their corresponding values in the deleteArray section to specify the record to be deleted. The image below illustrates the sample schema:
    ![swagger-master-data-delete-endpoint](/resources/Storage/pulse-publication/images/swagger-master-data-delete-endpoint.png)
5. Click the **Execute** button to run the API. The result will be returned and viewed by scrolling down the page. Note that a 200 status code indicates a successful execution. If an error occurs during execution, a specific error code will be returned.

The GIF below demonstrates how to execute the Delete API endpoint in Swagger to remove a record from the master data. In this example, the record with the following details is deleted:

- ID: IND1
- Name: QWE
- Age: 30
- Email: abc@hotmail.com
- City: Tokyo
- Country: UK

![swagger-master-data-delete-endpoint-execution](/resources/Storage/pulse-publication/images/swagger-master-data-delete-endpoint-execution.gif)

## Add Record

After importing the Master Data JSON into Swagger, follow these steps to execute the Add API endpoint:

1. Click the **Authorize** button in Swagger. Provide the bearer token obtained from IDS by entering "Bearer " followed by a space and then pasting the token. Alternatively, you can use a token generated from the Reels platform for authorization.
2. Navigate to the Update endpoint. Expand its section, click the Try it out button to enable editing:
  1. **datasetID**: Specifies the datasetID of the master data. This field is pre-filled and does not require editing.
  2. **entityID**: Specifies the entityID of the master data. This field is pre-filled and does not require editing.
  3. **mdmID**: Specifies the mdmID of the master data. This field is pre-filled and does not require editing.
3. In the Request Body section, specify the column names and their corresponding values for the record to be added to the master data.
4. The sample schema includes predefined columns that can be customized based on the column names in the master data. The image below illustrates the sample schema:
    ![swagger-master-data-add-endpoint](/resources/Storage/pulse-publication/images/swagger-master-data-add-endpoint.png)
5. Click the **Execute** button to run the API. The result will be returned and viewed by scrolling down the page. Note that a 200 status code indicates a successful execution. If an error occurs during execution, a specific error code will be returned.

The GIF below demonstrates how to execute the Add API endpoint in Swagger to add a record into the master data. In this example, a record with the following data is added:

- ID: IND1
- Name: QWE
- Age: 30
- Email: abc@hotmail.com
- City: Tokyo
- Country: Japan

![swagger-master-data-add-api-execution](/resources/Storage/pulse-publication/images/swagger-master-data-add-api-execution.gif)

[Next Topic](/articles/pulse-publication/integrate-content-repository)

[Previous Topic](/articles/pulse-publication/integrate-workflow)
