# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/date-duration>

The **Duration** node is used to calculate the duration of date and time.

Duration is defined as a length of time. It is contextless and does not have a defined beginning and end date. Therefore, we recommend not to use the **Duration** node to convert between units that depend on a context.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Action:** The action to be performed on the parameters. See [Duration Actions](/articles/server-services-designer-8/date-duration/a/h3_825119271) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns the output based on the action you choose. Map the result to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Duration Actions

**As Unit of Time: **Gives the date and time as is.

- **Unit: **The unit on which the action is to be performed.
- **Unit Value: **The value to be expressed in the unit of time.

**Example:** if the unit is **year** and value is **20/03/****2021**, then the result will be** 2021**.

---

**Get Unit of Time:** Gets the number of units in a duration.

- **Unit: **The unit on which the action is to be performed.
- **Unit Value: **The value in the unit of time.

**Example: **If the unit is **month** and the value is **100**, then the calculation will be 100 divided by 12 and the remainder **4** is returned as the result.

---

**Create Duration:** Creates a Duration object.

If you want to create a duration object for one unit value, enter:

- **Unit:** The unit on which the action is to be performed.
- **Unit Value:** The date and time.

If you want to create duration objects of multiple unit values, enter:

- **Object literal: **The object literal with the values.

---

**Clone:** Creates a clone of the duration object.

- **Unit: **The unit on which the action is to be performed.
- **Unit Value: **The value which is to be cloned.
