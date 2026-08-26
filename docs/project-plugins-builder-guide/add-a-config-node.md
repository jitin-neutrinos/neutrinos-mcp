# Add a Config node

<https://documentation.neutrinos.com/articles/#!project-plugins-builder-guide/add-a-config-node>

A [Config node](/articles/concepts-publication/node/a/h4_794977392) is always associated with a server node that requires configuration to a server.

To add a Config node, you enter the node details and the node attributes using the respective editors. You do not make any changes in the Node Dependencies and Code generation editors. All the dependencies and code will be written in the server node that the config node is associated with.

To add a Config node:

1. Expand **Nodes** and click the **plus** icon next to the **server** option.
2. Enter the name of the node that you want to create and press the **Enter** button. Append the word '**config**' in the node name. This is required as the config node is accessible within the server node. For example, for an AMQP configuration node, you can enter the node name as **AMQPConfig**. This helps distinguish the **AMQP** node from the **AMQP Config **node. The node gets added under the **server **section. Expand the node to view the editors that you can use to customize the node.
3. Enter node details. See [Node Details](/articles/project-plugins-builder-guide/node-details). Make sure you check the **Config Node** checkbox when you enter the details.
4. Enter node attributes. See [Node Attributes](/articles/project-plugins-builder-guide/node-attributes) to learn how to enter the node details. Do not select **Config** in the **Select Attribute Type** field.
