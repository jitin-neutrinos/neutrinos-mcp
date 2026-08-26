# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/date-operations>

The **Date Operation** node provides various actions to manipulate the date and time on a moment object.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Input Reference: **The date and time on which the action is to be performed.
- **Action:** The action to be performed on the parameters. See [Date Actions](/articles/server-side-service-designer-publication/date-operations/a/h3__1710887367) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns a moment object. Map the result to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Date Actions

**Add:** Adds date and time to **Input Reference**.

**Note:**

- If you are adding time that crosses over daylight saving time, the original hour will always match the added hour.
- Adding a month will add the specified number of months to the date.
- If you are adding hours, minutes, seconds, or milliseconds, the assumption is that you want precision to the hour, and will result in a different hour.
- when decimal values are passed for days and months, they are rounded to the nearest integer. Weeks, quarters, and years are converted to days or months and then rounded to the nearest integer.

If you want to add one unit at a time, enter:

- **Unit:** The unit to be added.
- **Unit Value:** The value to be added.

**Example: **If the **U****nit** is **year **and the **Unit Value** is **5**, then 1st March 2021 will be converted to 1st March 2026.

If you want to add multiple units at a time (for example, year and month), enter:

- **Object literal: **Enter an object literal or a duration object with the values. Example:
  - Object literal: **({years:5, months:1})**
  - Duration object: **moment.duration({'years': 5}{‘days’ : 1})**

**Example: **If the **Input reference **is** ({years:5, months:1})**, then 1st March 2021 will be converted to 1st April 2026.

---

**Subtract:** Subtracts date and time from **Input Reference**.

**Note:**

- If you are subtracting time that crosses over daylight saving time, the original hour will always match the subtracted hour.
- Subtracting a month will subtract the specified number of months to the date. For example, subtracting a month from February 28th will give you the result to January 28th.
- If you are subtracting hours, minutes, seconds, or milliseconds, the assumption is that you want precision to the hour, and will result in a different hour.
- when decimal values are passed for days and months, they are rounded to the nearest integer. Weeks, quarters, and years are converted to days or months and then rounded to the nearest integer.

If you want to subtract one unit at a time, enter:

- **Unit:** The unit to be subtracted.
- **Unit Value:** The value to be subtracted.

Example:

If the

Unit

is

year

and the

Unit Value

is

5

, then 1st March 2021 will be converted to 1st March 2016.

If you want to subtract multiple units at a time(for example, year and month), enter:

- **Input Reference: **Enter an object literal or a duration object with values. Example:
  - Object literal: **({days:7, months:1})**
  - Duration object: **moment.duration({‘days’ : 1})**

**Example: **If the **Input reference **is** ({years:5, months:1})**, then 1st March 2021 will be converted to 1st February 2016.

---

**Start of Time:** Mutates the ****Input Reference** ** by setting it to the start of a unit of time.

- **Unit: **The unit which is to be set as the start of time.

- If the unit selected is **year**, then the moment will be set to January 1st, 12:00 am of this year.
- If the unit selected is **quarter**, then the moment will be set to the beginning of the current quarter, 1st day of months, 12:00 am.
- If the unit selected is **hours**, then the moment will be set to now, but with 0 minutes, 0 seconds, and 0 milliseconds.

---

**End of Time:** Mutates the ****Input Reference** ** by setting it to the end of a unit of time.

- **Unit: **The unit which is to be set as the end of time. If the unit selected is **year**, then the moment will be set to 12-31 23:59:59.999 this year.

---

**Local: **Shows the local time instead of the original date and time in **Input Reference.**

---

Input Reference:

you can pass an object

literal like ({days:7, months:1}) or you can

pass a duration object like moment.duration({‘days’ : 1}).

Input Reference:

you can pass an object

literal like ({days:7, months:1}) or you can

eew pass a durat.duration({‘days’ : 1}).

**UTC:** Shows the Coordinated Universal Time (UTC) instead of the original date and time in **Input Reference**.
