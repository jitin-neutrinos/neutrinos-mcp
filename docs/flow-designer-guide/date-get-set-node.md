# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/date-get-set-node>

This is the default topic template.

The **G****et Set** node is used to get and set time.

### Node Properties

- **Name:** A unique name for the node.
- **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.
- **Input Reference**: The date and time as a moment object or string. If you give a string, this function converts the string to a moment object and then performs the action on it.
- **Action**: The action to be performed on the parameters. See [Get Set Actions](/articles/flow-designer-guide/date-get-set-node/a/h3__1710887367) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns a moment object. You can map the result to a[flow or page variable](/articles/flow-designer-guide/properties-page-designer).

### Get Set Actions

**Get**: Gets date and time. If you are in UTC mode, then the result will be UTC equivalent.

Unit: The unit of date and time to get.

Example: If the Input Reference is **03/09/2021 **and if the Unit is **month**, then** 09** is returned.

**Set**: Sets date and time. If you are in UTC mode, then the result will be UTC equivalent.

- **Unit**: The unit of date and time to set.
- **Unit Value**: The value to set in the moment object in the Input Reference field.

Or,

- **Object**: The date and time that is to be set in the moment object given in the **Input Reference** field. Example of an object - **{hour:10, minute:25, second:50}**.

---

**Maximum**: Returns the maximum (most distant future) of the given input references.

**Input Reference 1**: The date and time to be compared against** Input Reference 2**.**Input Reference 2**: The date and time to be compared against **Input Reference 1**.

**Minimum**: Returns the minimum (most distant past) of the given input references.

- **Input Reference 1**: The date and time to be compared against **Input Reference 2**.
- **Input Reference 2**: The date and time to be compared against** Input Reference 1**.
