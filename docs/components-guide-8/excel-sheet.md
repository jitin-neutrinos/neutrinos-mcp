# Excel Sheet

<https://documentation.neutrinos.com/articles/#!components-guide-8/excel-sheet>

## Excel Sheet

### Overview

This is a custom directive to convert excel sheets into HTML. If you want to use this add the n-sheet custom directive to any component.

### Usage

This directive can be added to any component. Once added, the following functionality will be triggered once the component is loaded:

- The n-sheet directive calls the n-sheet service (which can be used separately as well).
- The inputs from the directive (if valid) will be used to convert the excel data which could either be an absolute file path or a file buffer into HTML. The HTML data can then be inserted directly into any component on a page.

### How to use

1. Download and install the **Excel Sheet **directive from Neutrinos Store.
2. Drag and drop any component and then add the following key-value pairs using the **Custom Properties** section of the component's attributes window. If the value field is missing, then leave it empty. If an input needs to be added to the value field, click the **Key&Value** tab and edit the value of the attribute.
  1. Next, add the directive as an attribute.
    - **key:** n-sheet
    - No value field
    - Click the **ADD** button
  2. Provide the inputs that the directive will use.
    - **key: **[htmlContent]
    - **value: **(Optional, used if sheet options not specified) any HTML that will be directly populated to the component.
    - Click the **ADD** button to add the attribute to the component.
    - **key: **[sheetOptions]
    - **value:** (Higher Preference input) a variable that takes the following object as input from within the TS file. Replace type with value (example- Boolean becomes true).
    - Click the **ADD** button to add the attribute to the component.
  3. Next, add the directive as an attribute.
    1. Enter key: n-sheet with no value.
    2. Click the **ADD** button to add the attribute to the component.
  4. Provide the inputs that the directive will use.
    1. **key:** [htmlContent]
    2. **value:** (Optional, used if sheet options not specified) any Html that will be directly populated to the component.
    3. Click the **ADD** button to add the attribute to the component.
    4. **key:** [sheetOptions]
    5. **value:** (Higher Preference input) a variable that takes the following object as input from within the TS file. Replace type with value (eg: boolean becomes true).
    6. Click the **ADD** button to add the attribute to the component. Copy CodeJavaScript{
        doAppend: boolean, // Optional | Default value : false | If set to true does not clear the innerHTML of the component that the directive is being used within.
        url: 'string', // Mandatory | No Default value | Required to call the HTTP request node that then calls the Excel to HTML parser node
        httpMethod: 'string', // Optional | Default value : post | If set to 'get' then the other sheetOptions can be provided within B modelr.
        preHttpRequestCallback: Promise/Boolean, // Optional | No Default value | A Promise or a function that returns a boolean which runs right before url is called using the httpMethod. Will wait for the promise to complete. Can be used to check connectivity etc.
        dataType: 'string', // Mandatory | No Default value | Can take values 'file' or 'buffer', based on which the input sheetData has to be specified. For 'file', sheetData will be absolute filepath of the file on the system where B modelr is running. For 'buffer', sheetData will be the file buffer of the file. This input need not be specified at the directive if it is specified in B modlr.
        sheetData: 'string', // Mandatory | No Default value | THe absolute filepath or the file buffer based on the input dataType. This input need not be specified at the directive if it is specified in B modlr.
        retPure: boolean, // Not Valid | Default value : false | This variable returns each sheet as HTML in an array but cannot be used via the service or the directive, only via the B modelr.
        sheetIndices: Number Array[], // Optional | Default value : All | A number array which is used to decide which sheets have to be rendered in the final output. Index of the sheets start from 0 till (total number of sheets - 1). If not specified all sheets will be returned.
        noParent: boolean // Optional | Default value : false | If set to true, can be set to be viewed in full page views. Normal behaviour takes the height and width of the parent element
       }

5. Input the action that occurs if the directive successfully completed its functionality.

1. **key:** (onsuccess)
2. **value:** success($event).
3. Click the **ADD** button.
4. In the TypeScript editor, add the following function: success($event){console.log($event)}
5. The object returned on success contains the following values:
  1. In case of an exception, an HTTP error object will be received.
  2. In case of success, the excel rendered as HTML will be returned as a string. An array containing all the **sheetnames** and one with specified **sheetnames** (if **sheetIndices** input was specified) may also be returned if correct **sheetOptions** input was provided to the directive.

6. Input the action that occurs if the directive failed to complete its functionality.

1. **key:** (onerror)
2. **value:** error($event). Click the **ADD **button.
3. Then is TS file add the following function: error($event){console.log($event)}
4. The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per your requirement.

| ![Information](/resources/Storage/components-guide-8/info.png) | **console.log($event)** displays the output (which is **$event**) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
