# Define Node Attributes

<https://documentation.neutrinos.com/articles/#!project-plugins-builder-guide/node-attributes>

Each node has a set of attributes or properties associated with it. These attributes are used to define the functionality of the node.

For example, these are the attributes of a **Log** node:

---

### Define Node Attributes

Use this editor to define attributes for the node.

To add attributes to the node, open the **Node Attributes** editor. Click the **Add New + **button and enter the following fields:

1. **Attribute ****Label**: The label of the attribute.
2. **Attribute ****Name**: The name for the attribute is auto-generated based on the **Attribute Label** you provide.
3. **Attribute ****ID**: The Attribute ID is auto-generated based on the **Attribute Label **you provide.
4. **Select ****Attribute ****Type**: Define the type of the attribute. See [Types of Node Attributes](/articles/project-plugins-builder-guide/node-attributes/a/h3__668741143) to learn more.
5. **Required:** Select **Required **if a particular attribute is mandatory.

After entering the details of the attributes, click the **tick** icon and the attributes get added.

---

### Add the Node Label

Every node has a default **Name** attribute associated with it. This is an optional attribute and can be left empty. The name you enter in the node will be its display label on the Server Services editor.

![node name](/resources/Storage/project-plugins-builder-guide/node_name.png)

What if the** Name** attribute is not entered for a node? What will be the label of the node then?

While building the node on Plugins builder, you can handle situations where if the **Name** attribute is not entered, it can dynamically pick the label of the node by using the value you define for another node attribute. Click the **Edit Label** button and define the node attribute value that should be alternatively displayed if the node name is not entered.

For example, consider creating a node named **Server node 1**. Add an attribute of the node, say **schedule**. In the **Edit Label **editor of this node, enter the following code:

```javascript
function editlabel(SD) {    let label = 'Server Node Config'    if (this.name) {        label = this.name    }  else label = this.schedule   //Takes the value of the schedule attribute as the node label.    return label;}
```

If the name of this node is entered, then the name is displayed as the node label.

![](/resources/Storage/project-plugins-builder-guide/server%20node%20test2.png)

![Dummy server node](/resources/Storage/project-plugins-builder-guide/server%20node%20test.png)

If the name of the node is not entered and the value for the **schedule** attribute is entered, then that value is displayed as the node label.

![value of another node attribute](/resources/Storage/project-plugins-builder-guide/schedule_value.png)

![node label](/resources/Storage/project-plugins-builder-guide/schedult_node_label.png)

---

### Types of Node Attributes

Node attributes can be of many types. In Neutrinos Studio, you can create an attribute for a node with the following types:

- Input
- Typed Input
- Select
- Toggle
- File Upload
- Config

---

#### Input

A field to enter values.

- **Regex: **Define the pattern of the input.
- **Error Message: **An error message to display if the pattern is mismatched.

**Example:**

---

#### Typed Input

A replacement for a regular Input attribute that allows the type of the value to be chosen, including options for string, number, and boolean types.

**Select Types: **Select the types for the typed input. The types can be:

- "**bh" Types - **bh is the flow object. See [Properties in Server Services](/smart/project-server-side-service-designer/properties-in-server-services) to learn more. A user can choose to map any key of the bh object. Keys include:
  - **bh.** - The value sent to {Node}.js for code generation will be bh.{User input value}.
  - **bh.input** - The value sent to {Node}.js for code generation will be bh.input.{User input value}.
  - **bh.local** - The value sent to {Node}.js for code generation will be bh.local.{User input value}.
- **String - The user** input will be stringified. The value sent for the {Node}.js will be equivalent to JSON.stringify({User Input Value}).
- **Number - **The user input will be parsed to a number. The number entered will be validated when this type is selected.
- **As is - **The user input is considered as is.
- **Boolean - **The value field will have a dropdown to select true or false.
- **Page Variable** - This field is visible only when you are creating a **page** node. See [Properties in Page Designer](/smart/project-page-services-designer-guide/properties-page-designer) to learn about the page variable and what it includes.
- **Client Env - **This field is visible only when you are creating a **page** node or a **client **node. You use this field to access the** client** environment properties that you have defined in the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor. These properties are internally stored in bh.system.environment.properties.<property_name> property.
- **Server Env** - This field is visible only when you are creating a **server** node. You use this field to access the** server** environment properties that you have defined in the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor. These properties are internally stored in process.env.<property_name> property.

**Example:**

---

#### Select

A drop-down list with options.

- **Option: **Define the option of the drop-down list to select from.
  - **Value:** The value for the option.
  - **Display Value:** The value of the option in the drop-down list.
  - **Make Default:** Check to make this option default.
- **Field dependency**
  - **Dependent: **Fields to which actions are to be applied based on the value of the controlling field.
  - **Value: **The value of the controlling field.
  - **Condition: **The condition to which the action should take place.
  - **Action: **Action that is to be applied to the dependent field when the defined condition is met.

**Example: **

![](/resources/Storage/project-plugins-builder-guide/select%20type1.png)

**Toggle Button**


 A button to switch between two states.

- **State**: The state of the toggle button. By default, it is **ON**.
- **Field dependency**
  - **Dependent: **Fields to which actions are applied based on the value of the controlling field.
  - **Value: **The value of the controlling field.
  - **Condition:** The condition to which the action should take place.
  - **Action: **Action that is to be applied to the dependent field when the defined condition is met.

**Example:**

![](/resources/Storage/project-plugins-builder-guide/toggle%20type.png)

---

#### File Upload

A button to upload files.

- **Upload Multiple Files:** A checkbox, when enabled, allows the user to upload multiple files.

---

#### Config

This attribute is visible when you are defining node attributes for a server node. Use this field to associate a [Config](/smart/project-concepts/node/a/h5_795116784) node with the server node.

- **Select the Config Node: **Select the configuration node to be associated with the server node that you are creating.

**Example: **The AMQP config node that is part of the **AMQP producer **node.

![](/resources/Storage/project-plugins-builder-guide/amqp%20config.png)
