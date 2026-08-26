# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/date-format>

The **Format** node is used to output the date and time in different formats.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Input Reference: **The date and time on which the action is to be performed. Choose number from the drop-down list and enter the date/time or map date/time to the bh. bh.input or bh.local property, and enter the variable name.
- **Action:** The action to be performed on the parameters. See [Format Actions](/articles/server-side-service-designer-publication/date-format/a/h3_941599958) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns the output based on the action you choose. Map the result to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Format Actions

**Format:** Converts date and time mentioned in **Input Reference** to the format that is mentioned in **Date Format**. This action returns a string.

- **Unit Format: **The format in which you want to display the date.

**Examples:**

- If the format is **dddd, MMMM Do YYYY, h:mm:ss** then the output is **Sunday, February 14th 2010, 3:25:50 pm**.
- If the format is **MMMM Qo DD YYYY**, then the output is **February 1st 14 2010**.

See the [Display documentation](https://momentjs.com/docs/#/displaying/format/) to learn about the combination of date formats that you can provide in this field.

---

**Time from now: **Returns the time elapsed since the given date and time in **Input Reference**. Example - If the Input Reference is **2018, 0, 1**, then the output is **3 years ago**.

---

**Time to now:** Returns the time to be elapsed before reaching the date and time in** Input Reference**. Example - If the date/time is **2024, 0, 1**, then the output is **in****3 years**.

---

**Time from x:** Returns the time elapsed between the start and end dates as a string.

- **Start Date: **The start date or time.
- **End Date:** The end date or time.

**Example: **If the Start Date is **2007, 0, 28 **and the End Date is **2007, 0, 29**, then the output is **a day ago**.

---

**Time to x:** Returns the time to be elapsed for the start date to be the end date.

- **Start Date:** The start date or time.
- **End Date:** The end date or time.

**Example: **If the Start Date is **2007, 0, 28 **and the End Date is **2007, 0, 29**, then the output is **in a day**.

---

**Difference:** Returns the duration between 2 dates.

- **Unit:** The unit on which the action is to be performed.
- **Start Date: **The start date and time. You can enter a string, moment object, date, number, or array.
- **End Date:** The end date and time. You can enter a string, moment object, date, number, or array.

**Example: **

- If the unit is** years**, the Start Date is **2008, 9** and the End Date is **2009, 2**, then the output is **1**.
- If the unit is** years**, the Start Date is **2009, 9** and the End Date is **2008, 2**, then the output is **-****1**.

---

**Unix Timestamp (milliseconds):** Takes **Input Reference** and calculates the number of milliseconds since the Unix epoch, that is, the number of milliseconds that has elapsed since the midnight of January 1, 1970. This action returns a Unix timestamp in milliseconds.

**Example:** If the Input Reference is 01/03/2021, then the output is 1614595698901.

---

**Unix Timestamp (seconds):** Takes **Input Reference** and calculates the number of seconds since the Unix epoch, that is, the number of seconds that has elapsed since the midnight of January 1, 1970. This action returns a Unix timestamp in seconds.

**Example: **If the Input Reference is 01/03/2021, then the output is 1614595698.

---

**As JavaScript Date:** Converts **Input Reference** to a native JavaScript date object.

---

**As Array:** Converts **Input Reference** to an array where the values in it will be the same as the date object.

---

**As JSON:** Converts **Input Reference** to a JSON object where the values in it will be the same as the date object.

---

**As Object:** Converts **Input Reference** to an object where the values in it will be the same as the date object.

---

**As String:** Converts **Input Reference** to a date string.
