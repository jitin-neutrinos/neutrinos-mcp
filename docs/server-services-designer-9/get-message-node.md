# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/get-message-node>

The AWS SNS **Get Message** node is used to extract messages from the endpoint's body for the topics you have subscribed to. To consume the message, drag and drop an HTTP In Node, and connect it with the get message node. This flow when executed will extract the message from the body.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
