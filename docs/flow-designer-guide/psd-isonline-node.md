# IsOnline node

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-isonline-node>

This is the default topic template.

The **isOnline **node returns a boolean value indicating the status of the network. True indicates that the network is available and False indicates that the network is unavailable.

![Information](/resources/Storage/flow-designer-guide/info.png)
 This event shouldn't be used to determine the availability of a particular website. Network problems or firewalls might still prevent the website from being reached.

Node Properties**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Result Mapping: **The result of the event. Enter the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) in which you want to save the result. Example:![Result emitted by the IsOnline node](/resources/Storage/flow-designer-guide/online%20%281%29.png)
