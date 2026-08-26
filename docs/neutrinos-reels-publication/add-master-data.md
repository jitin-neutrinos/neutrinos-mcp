# Add Master Data through Excel

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/add-master-data>

Following the steps below to add Master Data:

1. Click the **Master Data** button in the left-side navigation bar to open the Master Data page. This page displays a list of Master Data files created in the Reels platform in a tabular format, including details such as Master Data Name, ID, Version, Type, Author, Last Updated Date, and Date of Creation.
    ![master-data-details](/resources/Storage/neutrinos-reels-publication/images/master-data-details.png)
  1. **Search Bar**: Search the Master Data by name.
  2. **Name**: This column displays the name of the Master Data.
  3. **ID**: This column displays the ID of the Master Data
  4. **Version**: This column displays the latest version of the Master Data. The most recent version is marked with a 'Latest' tag next to the Master Data name.
  5. **Type**: This column displays the method used to create the Master Data file—either API or Excel.
  6. **Author**: This column displays the User ID of the author who created the Master Data
  7. **Last Updated and Time**: This column displays the date and time of the latest update to the Master Data.
  8. **Available From**: This column displays the creation date of the Master Data.
  9. **Actions**: This column provides options to update to a new version, download the Excel file, delete the Master Data, or export it as a JSON file.
2. Click the **Add** button on the top right of the Master Data page > Click **New** from the dropdown options. Alternatively, you can import an existing Master Data file by uploading a JSON file containing the required Master Data.
3. After clicking the **New** option from the dropdown, a pop-up window appears, allowing you to select a method for creating a Master Data file. You can either create Master Data from an Excel sheet or create it via an API.
    ![master-data-create-page](/resources/Storage/neutrinos-reels-publication/images/master-data-create-page.png)

### Add Master Data through Excel

1. After clicking the **New** option from the pop-up window, select '**Excel**' to create Master Data using Excel, and click '**Next**'.
    ![master-data-create-excel-option](/resources/Storage/neutrinos-reels-publication/images/master-data-create-excel-option.png)
2. Upload the file by either dragging and dropping it or browsing to select and upload it. To set a name for the Master Data file, click the edit option in the top-right corner of the window. By default, the file name is 'My File Name.' You can also add a description for the Master Data being created.
    ![master-data-excel-upload](/resources/Storage/neutrinos-reels-publication/images/master-data-excel-upload.png)
    ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
    The maximum size of the file that can be uploaded is 15 MB
3. After selecting the Excel sheet that contains the information for creating Master Data, click 'Next'.
    ![master-data-excel-next](/resources/Storage/neutrinos-reels-publication/images/master-data-excel-next.png)
4. The headers of each column in the Excel sheet are extracted, and data types are automatically assigned based on the column data. If the data types are correct, verify them and click 'Next'. If needed, modify the data types before proceeding.
    ![master-data-excel-review-mapping](/resources/Storage/neutrinos-reels-publication/images/master-data-excel-review-mapping.png)

The GIF below illustrates how to create Master Data using Excel, including fields such as ID, Name, Age, Email, City, and Country.




 ![master-data-create-excel](/resources/Storage/neutrinos-reels-publication/images/master-data-create-excel.gif)

### Add Master Data through API

1. After clicking the **New** option from the pop-up window, select '**API**' to create Master Data using API, and click '**Next**'.
2. The window now prompts you to add a URL, including headers, query parameters, payload, authorization settings, and output mapping.
    ![master-data-create-api](/resources/Storage/neutrinos-reels-publication/images/master-data-create-api.png)
  1. **Method**: Specifies the HTTP method for the API call, which can be either POST or GET.
  2. **Type**: This can be either an API object or a string.
  3. **Value**: Specifies the value used to call the API, such as the base URL.
  4. **Path**: The actual path of the API.
  5. **API Authorization**: Defines the authorization method used by the API. Options include:
    - None: No authorization required
    - Client: Requires Client ID and Client Secret
    - Bearer Token: commonly used for OAuth 2.0
    - Basic: requires Username and Password
  6. **Output Mapping**: Specifies how to extract relevant data from the API response. This is useful when the response is nested or only a specific part of it is needed.
  7. **After Response**: This editor is used to define actions or modifications that occur after the API request is made and the response is received.
3. Click '**Next**' to retrieve the column headers for the Master Data created through the API.
4. Verify the columns and their data types, then click '**Next**' to create the Master Data file.

The GIF below illustrates how to create a Master Data file using an API. This example demonstrates retrieving a list of all products using a dummy API.

![master-data-create-api-example](/resources/Storage/neutrinos-reels-publication/images/master-data-create-api-example.gif)

### Update Master Data

The data in the Master Data file can be updated at regular intervals. This process can be automated using a cron. To set up a cron, follow the steps below:

1. While configuring Master Data in the **Add URL** section, enable the Cron toggle to automate updates.
    ![master-data-add-cron](/resources/Storage/neutrinos-reels-publication/images/master-data-add-cron.png)
2. After enabling the toggle, select the update frequency from the Unit dropdown and enter a value. For example, to update Master Data daily, select 'Day' from the Unit dropdown and enter 1 in the input field.
    ![master-data-cron-example](/resources/Storage/neutrinos-reels-publication/images/master-data-add-cron-day-example1.png)

### Retieve selected fields

When creating Master Data using an API, you can specify the required fields and filter out unnecessary details. This can be done by writing custom code in the After Response section when generating the file. The steps below demonstrate retrieving only the necessary fields from the DummyJSON API while excluding arrays or objects from the response.

1. Enter the necessary inputs for base URL, actual API path, and authentication.
2. Add the below custom code in the **After Respose** section to remove the arrays and objects from the fields that are populated into the Master Data.
    Copy CodeJavaScriptconst response = apiObj.get('response'); // Assuming 'response' is the key for the API response object
   response.products = response.products.map(simplifyProduct);
   function simplifyProduct(product) {
    let simplifiedProduct = {};
    for (let key in product) {
    if (Object.prototype.hasOwnProperty.call(product, key)) {
    if (Array.isArray(product[key]) || typeof product[key] === 'object') {
    continue; // Skip nested arrays and objects
    }
    simplifiedProduct[key] = product[key];
    }
    }
    return simplifiedProduct;
   }
   apiObj.update('response',response);
    **Working of the Code:**
    The code retrieves an API response and stores it in apiObj under the key 'response'. It then updates the response.products array by mapping each product object through the simplifyProduct function.
    For each product, the function iterates over its keys while ensuring they belong directly to the object. If a key's value is an object or an array, it is skipped. Otherwise, the key-value pair is added to simplifiedProduct, resulting in a flattened product object that contains only primitive values (strings, numbers, booleans).
    Finally, the modified response is stored back into apiObj under the key 'response'.

[Next Topic](/articles/neutrinos-reels-publication/manage-data)

[Previous Topic](/articles/neutrinos-reels-publication/master-data-management)
