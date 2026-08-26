# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/date-validate-node>

This is the default topic template.

The **Validate** node is used to:

- Check for leap years
- Compare date and time
- Check if the date and time are valid

### Node Properties

- **Name:** A unique name for the node.
- **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.
- **Action**: The action to be performed on the parameters. See [Validate Actions](/articles/flow-designer-guide/date-validate-node/a/h3__1475266389) to learn about the actions that can be performed using this node.
- **Result Mapping**: Returns **True** or **False**. You can map the result to a [flow or page variable](/articles/flow-designer-guide/properties-page-designer).

---

### Validate Actions

**Is Before**: Returns True if the **Start Date** is before the **End Date**. Else, returns False.

- **Start Date**: The date/time to be checked.
- **End Date**: The date/time to be checked against.

**Is Same**: Returns True if the **Start Date** is the same as the **End Date**. Else, returns False.

- **Start Date**: The date/time to be checked.
- **End Date**: The date/time to be checked against.

**Is After**: Returns True if the **Start Date** is after the** End Date**. Else, returns False.

- **Start Date**: The date/time to be checked.
- **End Date**: The date/time to be checked against.

**Is Same or Before**: Returns True if the **Start Date** is the same or before the **End Date**. Else, returns False.

- **Start Date**: The date/time to be checked.
- **End Date**: The date/time to be checked against.

**Is Same or After**: Returns True if the **Start Date** is the same or after the **End Date**. Else, returns False.

**Start Date**: The date/time to be checked.**End Date**: The date/time to be checked against.**Is Between**: Returns True if a date or time is between the given dates. Else, returns False.**Start Date**: The starting date/time. **End Date**: The end date/time.**Is Between**: The date/time to be validated if it is between the start and end dates.

**Is a Moment**: Returns True the date/time in Input Reference is a moment object. Else, returns False.

- **Input Reference**: The date/time to be validated.

**Is a Date**: Returns True if the date/time in Input Reference is a native JavaScript date object. Else, returns False.

**Input Reference**: The date/time to be validated.

**Is Leap Year**: Returns True if the date/time in Input Reference is a leap year. Else, returns False.

- **Input Reference**: The date/time to be validated.

**Is Daylight Saving Time**: Returns True if the date/time in Input Reference is in daylight saving time. Else, returns False.

- **Input Reference**: The date/time to be validated.

**Is a Duration**: Returns True if the date/time in Input Reference is a duration object. Else, returns False.

- **Input Reference**: The date/time to be validated.
