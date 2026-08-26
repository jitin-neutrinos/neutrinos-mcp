# Create your First Flow

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/create-your-first-flow>

## Create your First Flow

Start modeling your application services. Perform these steps to create your first flow:

### Add an Inject Node

The** Inject **node allows you to inject messages into a flow, either by clicking the button on the node or setting a time interval between injects.

Drag one onto the workspace from the palette. The node gets renamed to** Timestamp** as the payload type is Timestamp by default. Open the sidebar (Ctrl-Space, or via the dropdown menu) and select the **Info** tab.

Select the node to see information about its properties and a description of what it does.

![Create a flow 1](/resources/Storage/neutrinos-modelr-guide/inject.png)

### Add a Debug node

The **Debug** node causes any message to be displayed in the Debug sidebar. By default, it just displays the payload of the message, but it is possible to display the entire message object.

![Create a flow - Add a Debug node](/resources/Storage/neutrinos-modelr-guide/debug_node.png)

### Wire the two together

Connect the **Inject** and **Debug** nodes together by dragging between the output port of one to the input port of the other.

### Deploy

At this point, the nodes only exist in the editor and must be deployed to the server. Click the **Deploy** button. With the Debug sidebar tab selected, click the Inject button. You should see numbers appear in the sidebar. By default, the Inject node uses the number of milliseconds as its payload.

### 

### Add a Function node

The **Function** node allows you to pass each message through a JavaScript function.

Wire the Function node in between the Inject and Debug nodes. You may need to delete the existing wire (select it and hit delete on the keyboard).

Double-click on the Function node to bring up the edit dialog. Copy the following code into the function field:

```javascript
// Create a Date object from the payloadvar date = new Date(msg.payload);// Change the payload to be a formatted Date stringmsg.payload = date.toString();// Return the message so it can be sent onreturn msg;
```

Click **Ok** to close the edit dialog and then click the **Deploy** button.

![Create a flow - add a Function node](/resources/Storage/neutrinos-modelr-guide/function.png)

Now when you click the Inject button, the messages in the sidebar will be more readable timestamps.

### Source

The flow created in this example is represented by the following JSON. It can be imported straight into the editor by pasting the JSON into the Import dialog (Ctrl-I or via the dropdown menu).

```json
[  {"id":"58ffae9d.a7005",   "type":"debug",   "name":"",   "active":true,   "complete":false,   "x":640,   "y":200,   "wires": [   ]  },  {    "id":"17626462.e89d9c",    "type":"inject",    "name":"",    "topic":"",    "payload":"",    "repeat":"",    "once":false,    "x":240,    "y":200,    "wires": [      ["2921667d.d6de9a"      ]    ]  },  {    "id":"2921667d.d6de9a",    "type":"function",    "name":"Format timestamp",    "func":"// Create a Date object from the payload\nvar date = new Date(msg.payload);\n// Change the payload to be a formatted Date string\nmsg.payload = date.toString();\n// Return the message so it can be sent on\nreturn msg;",    "outputs":1,    "x":440,    "y":200,    "wires": [      ["58ffae9d.a7005"      ]    ]  }]
```
