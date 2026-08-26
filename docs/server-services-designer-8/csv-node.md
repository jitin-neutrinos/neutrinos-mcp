# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/csv-node>

The **CSV node** is used to convert between a **CSV formatted string** and **Javascript object** representation, or in either way. CSV string can be parsed to a javascript object or CSV parser can be built using Javascript object.

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- In the Nodes Palette, drag and drop the **CSV** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

- **Name**: The name for the node. This name will be displayed on the canvas when the node is saved.![CSV properties1](/resources/Storage/server-services-designer-8/csv_node.png)
- **Operation type**: The type of operation that the node should perform. It is either a **P****arse **or a** Builder.**
- **CSV source**: The source of the **CSV string** or **JavaScript object**. Select either:
  - **bh.input:** To specify the input parameter that holds the source. For example, if you specify bh.input.inputsource in this field, the server-side service fetches the input source that is saved.
  - **bh.local: **To specify the local parameter that holds the source. For example, if you specify bh.local.localsource in this field, the server-side service fetches the local source that is saved. To learn more about input and local parameters, see [properties](/articles/server-side-service-designer-publication/properties-in-server-services) to know more.
- **Switch**: Toggle the switch to replace the source property with the result. Else you can use the **Parsed CSV** field to save the result to a local or input property.
- **Parsed CSV**: Saves the retrieved data to a bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.input.result in this field, then that input property will hold the content of the file in the selected output format.
- If you chose **CSV parser** as the **Operation Type**, then you should configure these fields:

- **Key**: Generates records in the form of object literals. The key should start with an alphabet, and can contain alphabets, numbers, and underscore. You can enter the keys directly or click the **Map** icon to select the** Parse Columns** option.
  - For manual input, enter the key and click the **P****lus **icon to add the key. The key is required if you do not have column headers defined in your excel sheet. For example, if the data stored in ythe excel sheet is:![CSV file](/resources/Storage/server-services-designer-8/csv_key.png)and the keys defined are:![CSV keys](/resources/Storage/server-services-designer-8/csv_key2.png)Then the converted javascript object will look like: Copy CodeJavaScript[{"Email":"laura@example.com","number":"2070","First Name":"Laura"}]
  - To Parse columns, click the** Map** icon and toggle the **Parse Columns **button. The first row in the CSV data is treated as column headers for the data. Therefore, you need not specify keys manually. For example, If the data stored in your excel sheet is:![CSV file](/resources/Storage/server-services-designer-8/csv_header1.png)and **Parse Columns** option is selected ![](/resources/Storage/server-services-designer-8/parse_cols.png)then the converted will look like: Copy CodeJavaScript[{"email":"laura@example.com","number":"2070","firstname":"Laura"}]
- **Delimiter: **Set a field delimiter to separate the values. By default, a comma is selected as the delimiter. The delimiters that you can select are Comma, Tab, Space, Colon, Hashtag, Other (Specify the delimiter of your own choice).
- **Max record size**: The maximum number of characters and line buffers that the field can contain before an exception is raised. This field accepts only an integer value.
- **Relax column size**: Discards the count of inconsistent columns. By default, it is set to** false**.
- **Skip lines with errors**: Skips a line that has error and directly processes the next line.
- **Byte order mark**: A **byte order mark** (**BOM**) is a sequence of **bytes** used to indicate Unicode encoding of a text file. If true, it detects and excludes the BOM from the CSV input if any.

If you choose **CSV builder** as your **Operation Type**, you should configure these fields:

- **Header: **Toggle the header to show and configure the header field.
- ** Key**: The key values must be configured to be included as headers. For example, enter the keys that are specified in the key field during the parse operation.
- **Headers**: The header name for the key. For example, Header for **K****ey A** be "**Firstkey**" and Header for **Key B** be "**Secondkey**".
- **Delimiter**: Set a field delimiter to separate the values. By default, a **comma** is selected as the delimiter. The delimiters that you can select are **Comma**,** Tab**, **Space**, **Colon**,** Hashtag**, **Other **(Specify the delimiter of your own choice).

### Example

See [Working with Parsers](/articles/how-to-articles/working-with-data-formats) to view a similar example of working with a YML node. You can replace the** YML** node with a **CSV** node and create a similar flow to convert data from CSV to JSON String format.
