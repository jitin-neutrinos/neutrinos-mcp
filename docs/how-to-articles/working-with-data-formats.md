# Reading a File in YML Format

<https://documentation.neutrinos.com/articles/#!how-to-articles/working-with-data-formats>

The [Server-side services Designer](/smart/project-concepts/server-services-designer) (SSD) provides parsers to convert data from one format to another while creating server-side service flows for your application.

In this example, you will learn how to convert data from YML to a JSON String format. To do that, you will be performing the following sub-steps:

1. Read a file in YML format by using the **FileIn** node
2. Convert the YML data to JSON object by using the **YML** parser node
3. Convert the JSON object to JSON string by using the** JSON** parser node
4. Write the converted data to a new file by using the **FileOut** node.

### Reading a File in YML Format

1. Open the **Server Services** editor from the Studio Application page.
2. Open an existing service or click the** Add a Server Service** button to add a new service.
3. From the Nodes Palette, drag and drop a **HTTP In** node to the workspace. The **HTTP In **node provides an HTTP end-point for creating web services.
4. Double-click the node to open its **Properties** window. Select the HTTP method and enter the URI path on which you want to perform HTTP operations.
    ![](/resources/Storage/how-to-articles/http_in_ex.png)
5. Drag and drop a **File In** node next to the **HTTP IN** node and create a flow. Double-click the node and provide the path of your YML file in the **File Path** field. Map the file data to an input or local parameter of your choice.
    ![](/resources/Storage/how-to-articles/file_in_ex.png)
6. The** ymlsrc.yml **file contains the following data: Copy CodeYAMLswagger: "2.0"
   info:
    description: "This is a sample server Petstore server. You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/). For this sample, you can use the api key `special-key` to test the authorization filters."
    version: "1.0.0"
    title: "Swagger Petstore"
    termsOfService: "http://swagger.io/terms/"
    contact:
    email: "apiteam@swagger.io"
    license:
    name: "Apache 2.0"
    url: "http://www.apache.org/licenses/LICENSE-2.0.html"
   host: "petstore.swagger.io"
   basePath: "/v2"

### Converting YML Data to JSON object

### 

To convert the YML data that we read from the location provided in the **File In **node, and to convert it to JSON Object, perform the following steps:

1. Drag and drop the **YML** parser node to the flow and connect it to the **File In** node.
2. Double-click the node to open its properties window.
3. Enter the Input or Local parameter which contains the YML data.
4. Enter the Input or local parameter to which you want to map the converted JSON object data. Or, toggle the **Switch** to replace the data stored in the source parameter with the result.

### Converting JSON Object to JSON String

JSON values can only be one of the six data types (strings, numbers, objects, arrays, Boolean, null). JavaScript values, on the other hand, can be any valid JavaScript Structure. Unlike JavaScript Object, a JSON Object has to be fed into a variable as a String and then parsed into JavaScript if its value has to be stored in a file.

Therefore, to store the JSON object data into a file, you should convert it to a JSON string. Perform the following steps: ![the JSON node](/resources/Storage/how-to-articles/json_ex.png)

1. Drag and drop a** J****SON **node to the flow and connect it to the** YML** node.
2. Double-click the node to add the properties.
3. Enter the source parameter which contains the JSON object to be parsed.
4. Enter the Input or local parameter to which you want to map the converted JSON string data. Or, toggle the **Switch** to replace the data in the source parameter with the result.

### Saving the Converted Data to a New File

After converting the data to JSON String, perform the following steps to save the converted data to a file:

1. Drag and drop a **File Out** node and connect it to the **JSON** node.
2. Double click the node. Enter the file path to which you want the data to be saved. The server-side service designer will create the file along with the path if the file does not exist.
3. In the **File Data Mapping** field, enter the source parameter which holds the data to be written to the file.
4. Choose between the options to create a directory, overwrite, or append at the end of the file.
5. Choose the type of encoding to be applied to the file that is to be created.
    ![](/resources/Storage/how-to-articles/file_out_ex.png)
6. Drag and drop the **HTTP Out **node to send responses back to requests received from an **HTTP In** node. Connect the node to the end of the flow.
7. Double-click the node. Select the** Response Type** as **Plain text** and enter the required values.
    ![](/resources/Storage/how-to-articles/http_out_ex.png)

The flow after completing all the sub-tasks:

![The example flow](/resources/Storage/how-to-articles/yml_parser_flow.png)

After deploying the flow, the **ymltojson.json **file will be created in the location that you provided in the **File Out** node. The JSON file content will look as follows:

```json
{  "swagger": "2.0",  "info": {    "description": "This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.",    "version": "1.0.0",    "title": "Swagger Petstore",    "termsOfService": "http://swagger.io/terms/",    "contact": {      "email": "apiteam@swagger.io"    },    "license": {      "name": "Apache 2.0",      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"    }  },  "host": "petstore.swagger.io",  "basePath": "/v2"}
```
