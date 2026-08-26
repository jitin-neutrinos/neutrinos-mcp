# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/date-get-set>

The **Get Set** node is used to get and set time.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Input Reference: **The date and time as a moment object or string. If you give a string, this function converts the string to a moment object and then performs the action on it.
- **Action:** The action to be performed on the parameters. See [Get Set Actions](/articles/server-services-designer-8/date-get-set/a/h3__1710304451) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns a moment object. Map the result to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Get Set Actions

**Get:** Gets date and time. If you are in UTC mode, then the result will be UTC equivalent.

- **Unit:** The unit of date and time to get.

**Example:** If the **Input Reference** is **03/09/2021** and if the Unit is **month**, then **09** is returned.

---

**Set:** Sets date and time. If you are in UTC mode, then the result will be UTC equivalent.

- **Unit:** The unit of date and time to set.
- **Unit Value:** The value to set in the moment object in the** Input Reference** field.

Or,

- **Object: **The date and time that is to be set in the moment object given in the **Input Reference** field. Example of an object - **{hour:10, minute:25, second:50}**.

---

**Maximum:** Returns the maximum (most distant future) of the given input references.

- **Input Reference 1: **The date and time to be compared against Input Reference 2.
- **Input Reference 2:** The date and time to be compared against Input Reference 1.

---

**Minimum:** Returns the minimum (most distant past) of the given input references.

- **Input Reference 1:** The date and time to be compared against Input Reference 2.
- **Input Reference 2:** The date and time to be compared against Input Reference 1.
