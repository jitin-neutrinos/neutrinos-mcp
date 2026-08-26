# Initialize input and local Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/properties-in-server-services>

When you drag and drop a node to the services editor, Neutrinos by default creates a flow level object named bh.. This object has the following properties, which we refer to as flow properties:Flow PropertiesThe bh.local contains variables that are private to the flow. They are not available outside the flow unless they are defined as Output variables using the [Start](/articles/server-side-service-designer-publication/start-node) node.
The bh.input properties are the input parameters passed to the function that is performed by the node. They are not available outside the flow unless they are defined as **Output **variables using the [Start](/articles/server-side-service-designer-publication/start-node) node.
By default, when a client request is sent to the server, the following parameters are mapped to the bh.input properties: Copy CodeMarkdown bh.input.params = web.req.params;
 bh.input.query = web.req.query;
 bh.input.body = web.req.body;
 bh.input.files = web.req.files;
 bh.input.cookies = web.req.cookies;
 bh.input.headers = web.req.headers;
 bh.input.hostname = web.req.hostname;
 bh.input.method = web.req.method;
 bh.input.path = web.req.path;
 bh.input.signedCookies = web.req.signedCookies;The bh.error property is created when an exception occurs. It stores the error object that is thrown when an exception occurs. These exceptions are caught by the [Catch](/articles/server-side-service-designer-publication/catch-node) node in the Server Services Designer. You can read the error objects and debug the flow to solve the error.

The process.env or the bh.system.environment property is used to access the server environment properties that are configured in the [Environments editor](/smart/project-sample-how-to-guide/what-is-an-environment). See [Define Environments](/smart/project-sample-how-to-guide/what-is-an-environment) to learn more.The bh.web property contains req, res, and next objects. See the [Express documentation](https://expressjs.com/en/4x/api.html#req) to learn more.



 ![Warning](/resources/Storage/server-services-designer-9/warning.png)

  You should not override the** bh **object. For example, you should not assign the following values to the** bh** object:bh = nullbh = undefinedbh = empty object

### Initialize input and local Properties

You can initialize bh.input and bh.local properties in the Start and Script nodes of a flow and assign them values.

#### Creating input or local Variables in the Start Node

To create **input** or **local** variables in the **Start **node, create a service or open an existing service, and perform the following steps:

1. Drag and drop a **Start** node.
2. To create an input variable, in the** Input Parameters** field specify the input parameters for the flow.
  - Enter an input key.
  - Enter a value to be associated with the key. The value can be of type JSON, String, and number.
  - If you want to access the input variable outside the flow, assign it to be an output variable by toggling output to True. ![](/resources/Storage/server-services-designer-9/output_var.png)
  - Click **+ icon **to add the variable to the list of input variables.
3. To create a local variable, in the **Local Variables** field:

![Information](/resources/Storage/server-services-designer-9/info.png) If you want to set an input or local property as an output variable so that the variable can be accessed outside the flow, then you have to create the property only in the** Start** node and toggle the **Output** to **True**.

#### Create input or local Variables in the Script node

To create or update the values of **input** or **local** variables in the **Script **node, perform the following steps:

1. Drag and drop a **Script** node to the service flow.
2. In the **Code Editor**, add the code similar to this example:

Copy CodeJavaScriptbh.input.modelrApiURL='http://localhost:24483/';
bh.local.city='Goa';

If the variable exists, its value will be updated. If the variable does not exist, it will be created.

| ![Information](/resources/Storage/server-services-designer-9/info.png) | You cannot set **local and input** variables as output variables from the Script node. You have to use the** Start** node to do this operation. |
| --- | --- |
