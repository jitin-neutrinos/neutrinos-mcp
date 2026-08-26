# Node Details

<https://documentation.neutrinos.com/articles/#!plugins-builder-guide-8/node-details>

Use this editor to enter node details such as:

- **Node Display Name: **The name of the node. This field is pre-filled. You can edit this field to rename the node.
- **Config Node:** This field is visible only when you are adding a **Server** node. Check this field if you are creating a [Config node](/smart/project-concepts/node/a/h5_795116784).
- **Generated Node Name**: The auto-generated name for the node.
- **Node Color Code: **The color code for the node. You can use the color palette to choose a color of your choice.
- **Documentation Link:** The link to the node documentation.
- **Category: **The category to which the node belongs. When a node registration happens with a service type, the node will appear in this category in the canvas's node palette. By default, the category of a node is **General**. For example, the category for the **Log** node was given as **General**. Therefore, the **Log** node appears under the **General** section in the nodes palette.
    ![server category](/resources/Storage/plugins-builder-guide-8/server%20category.png)
- **Node Flow Type: **Decides the flow of the node.
  - **Start:** Used to start a service flow. The node will have only the output port to connect to other nodes. For example, the **Start **node:
      ![](/resources/Storage/plugins-builder-guide-8/start%20node.png)
  - **Flow: ** Used anywhere in the service flow. The node will have both input and output ports to connect to other nodes. For example, the Call Service node:
      ![](/resources/Storage/plugins-builder-guide-8/call%20serv%20node.png)
  - **End:** Used to end the service flow. The node will have only the input port to connect to other nodes. For example, the** Log** node:
      ![](/resources/Storage/plugins-builder-guide-8/log%20node.png)
- **Package Store Icon**: The icon to be associates with the node. After uploading, the preview of the icon will be displayed to the right.
    ![Node details](/resources/Storage/plugins-builder-guide-8/Node_details.png)
