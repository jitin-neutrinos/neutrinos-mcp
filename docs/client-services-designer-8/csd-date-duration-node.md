# Node Properties

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/csd-date-duration-node>

The **Duration **node is used to calculate the duration of the date and time.

Duration is defined as a length of time. It is contextless and does not have a defined beginning and end date. Therefore, we recommend not to use this node to convert between units that depend on a context.

### Node Properties

- **Name:** A unique name for the node.
- **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.
- **Input Reference**: The date and time on which the action is to be performed.
- **Action: **The action to be performed on the parameters. See [Duration Actions](/articles/client-services-designer-8/csd-date-duration-node/a/h3_825119271) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns the output based on the action you choose. Enter the [flow variable](/articles/client-services-designer-8/service-designer-variables) to which you want to map the result.

### Duration Actions

**As Unit of Time**: Gives the date and time as is.

- **Unit**: The unit on which the action is to be performed.
- **Unit Value**: The value to be expressed in the unit of time.

Example: if the unit is year and value is **20/03/2021**, then the result will be **2021**.

**Get Unit of Time**: Gets the number of units in a duration.

- **Unit**: The unit on which the action is to be performed.
- **Unit Value**: The value in the unit of time.

Example: If the unit is **month** and the value is **100**, then the calculation will be 100 divided by 12, and the remainder **4** is returned as the result.

**Create Duration**: Creates a Duration object.

If you want to create a duration object for one unit value, enter:

- **Unit**: The unit on which the action is to be performed.
- **Unit Value**: The date and time.

If you want to create duration objects of multiple unit values, enter:

- **Object literal**: The object literal with the values.

---

**Clone**: Creates a clone of the duration object.

- **Unit**: The unit on which the action is to be performed.
- **Unit Value**: The value which is to be cloned.
