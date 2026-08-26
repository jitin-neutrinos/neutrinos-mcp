# Messages

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/messages>

## Messages

These recipes address problems specific to **messages** and shows by example how they can be solved using the capabilities of Modelr .

- [Set a message property to a fixed value](/articles/neutrinos-modelr-guide/messages/a/h3__1755792576)
- [Delete a message property](/articles/neutrinos-modelr-guide/messages/a/del_msg)
- [Move a message property](/articles/neutrinos-modelr-guide/messages/a/h3__2118639688)
- [Map a property between different numeric ranges](/articles/neutrinos-modelr-guide/messages/a/map_a_msg)

---

### Set a message property to a fixed value

#### Problem

You want to set a message property to a fixed value.

#### Solution

Use the Change node to set the property of the message.

#### Example

![](https://cookbook.nodered.org/images/basic/copy-message-property.png)

#### Discussion

The Changenode can be used to set properties of a message. The node supports setting various JavaScript types as well as some Modelr specific types.

- strings: `"hello world"`
- numbers: `42`
- boolean: `true/``false`
- timestamp: the current time, in milliseconds
- JSON: a JSON string that will be parsed to its Object representation
- Buffer: a Node.js Buffer object

It also supports setting a property to a value based on the value of context properties, other message properties or a JSONata expression.

---

### Delete a message property

#### Problem

You want to delete a message property.

#### Solution

Use the `Change` node to delete the property.

#### Example

![](https://cookbook.nodered.org/images/basic/delete-message-property.png)

#### Discussion

The Change node can be used to delete the properties of a message.

---

### Move a Message Property

#### Problem

You want to move a message property to a different property.

#### Solution

Use the **change** node to move a property.

#### Example

![](https://cookbook.nodered.org/images/basic/move-message-property.png)

#### Discussion

The `Change` node can be used to move a property of a message.

It can be done as two separate actions in the `**Change**` node; first using a Set action to copy the property to its new location and then a Delete action to remove the original.

Alternatively, the node supports a Move action that does it in one step.

---

### 

### Map a property between different numeric ranges

#### Problem

You want to scale a number from one numeric range to another. For example, a sensor reading in the range 0 - 1023 should be mapped to a voltage range of 0 - 5.

#### Solution

Use the `Range` node to map between the defined ranges.

### Example

![](https://cookbook.nodered.org/images/basic/map-between-different-number-ranges.png)

#### Discussion

The `Range` node can be used to linearly scale between two different numeric ranges.

By default, the result is not constrained to the range defined in the node. This means using the voltage example above, a value of 2046 would map to a result of 10.

The node can be configured to constrain the result to the target range or apply simple modulo arithmetic so the value wraps within the target range.
