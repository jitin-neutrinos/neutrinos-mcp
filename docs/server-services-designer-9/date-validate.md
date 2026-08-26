# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/date-validate>

The **Validate **node is used to:

- Check for leap years
- Compare date and time
- Check if the date and time are valid

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Action:** The action to be performed on the parameters. See [Validate Actions](/articles/server-services-designer-9/date-validate/a/h3__1475266389) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns True or False. Map the result to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Validate Actions

#### Is Before: Returns True if the Start Date is before the End Date. Else, returns False.

**Is Same:** Returns **True** if the Start Date is same as the End Date. Else, returns **False**.

**Is After:** Returns **True** if the Start Date is after the End Date. Else, returns **False**.

**Is Same or Before:** Returns **True **if the Start Date is the same or before the End Date. Else, returns** False**.

**Is Same or After:** Returns **True** if the Start Date is the same or after the End Date. Else, returns **False**.

**Parameters for above actions:**

- **Start Date: **The date/time to be checked.
- **End Date: **The date/time to be checked against.

---

**Is Between:** Returns **True** if a date or time is between the given dates. Else, returns **False**.

- **Start Date:** The starting date/time. Choose **string **from the drop-down list and enter the topic or map the topic to the bh. bh.input or bh.local property, and enter the variable name.
- **End Date**: The end date/time.
- **Is Between: **The date/time to be validated if it is between the start and end dates.

---

**Is a Moment:** Returns **True** the date/time in **Input Reference** is a moment object. Else, returns **False**.

**Is a Date: **Returns **True** if the date/time in **Input Reference** is a native JavaScript date object. Else, returns **False**.

**Is Leap Year:** Returns **True** if the date/time in **Input Reference** is a leap year. Else, returns** False**.

**Is Daylight Saving Time:** Returns **True** if the date/time in** Input Reference** is in daylight saving time. Else, returns** False**.

**Is a Duration:** Returns **True** if the date/time in **Input Reference** is a duration object. Else, returns** False**.

**Parameter for above actions:**

- **Input Reference: **The date/time to be validated.
