# Add a Config Node

<https://documentation.neutrinos.com/articles/#!plugins-builder-guide-8/add-a-server-node>

| ![Information](/resources/Storage/plugins-builder-guide-8/info.png) | Before you add a node, learn about the [types of nodes](/articles/concepts-publication/node/a/h3__1155479691) in Neutrinos Studio. |
| --- | --- |

If you are creating a server node that contains a config node, we recommend that you add the **Config** node in the **Server **section of [Plugins Builder](/smart/project-concepts/plugins-builder) before adding the **server** node.

### Add a Config Node

A [Config node](/articles/concepts-publication/node/a/h4_794977392) is always associated with a server node that requires configuration to a server.

To add a Config node, you enter the node details and the node attributes using the respective editors. You do not make any changes in the Node Dependencies and Code generation editors. All the dependencies and code will be written in the server node that the config node is associated with.

To add a Config node:

1. Expand **Nodes** and click the **plus** icon next to the **server** option.
2. Enter the name of the node that you want to create and press the **Enter** button. Append the word '**config**' in the node name. This is required as the config node is accessible within the server node. For example, for an AMQP configuration node, you can enter the node name as **AMQPConfig**. This helps distinguish the **AMQP** node from the **AMQP Config **node. The node gets added under the **server **section. Expand the node to view the editors that you can use to customize the node.
3. Enter node details. See [Node Details](/articles/plugins-builder-guide-8/node-details). Make sure you check the **Config Node** checkbox when you enter the details.
4. Enter node attributes. See [Node Attributes](/articles/plugins-builder-guide-8/node-attributes) to learn how to enter the node details. Do not select **Config** in the **Select Attribute Type** field.

### Add a Server Node

To add a server node:

1. Expand **Nodes** and click the plus icon next to the **server **option.
    ![Add a node](/resources/Storage/plugins-builder-guide-8/server.png)
2. Enter the name of the node that you want to create and press the **Enter **button. Make sure you name the node based on its functionality. The node gets added under the **server **section. Expand the node to view the editors that you can use to customize the node.
    ![Adding a node name](/resources/Storage/plugins-builder-guide-8/server%20node%201.png)
3. Enter the [node details](/articles/plugins-builder-guide-8/node-details).
4. Define the [node attributes](/articles/plugins-builder-guide-8/node-attributes). Define the config node (if any) to be associated with the server node.
5. Add the [node dependencies](/articles/plugins-builder-guide-8/node-dependencies).
6. Define the [code generation](/articles/plugins-builder-guide-8/code-generation) logic.
7. Add the [Startup script](/articles/plugins-builder-guide-8/startup-script) that is to be executed when the node is installed. This is an optional step.
8. Add the required [node utility](/articles/plugins-builder-guide-8/node-utils) files.
9. [Publish](/articles/plugins-builder-guide-8/publish-the-node-package) the node package to test the node in the respective designer.
10. [Export to Production Publish](/articles/plugins-builder-guide-8/export-for-production-publish) to send the node to Neutrinos.
