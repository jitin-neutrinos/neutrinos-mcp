# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/date-parse>

The **Parse** node is used to parse date and time as a JavaScript object, string, array, and date object. The node will return the moment object as an output.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Action:** The action to be performed on the parameters. See [Parse actions](/articles/server-services-designer-8/date-parse/a/h3__929851382) to learn about the actions that can be performed using this node.
- **Result Mapping: **Returns a moment object or a UTC time moment object based on the **action** you choose. Map the result to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Parse Actions

#### Parse String: Parses a date in string type to a moment object.

- **Date:** The date as a string.
- **Date Format:** The format of the date. For example- **DD/MM/YYYY**. If you don’t know the exact format of the date string, you can use an array of date formats. For example - **[‘DD/MM/YYYY’, ‘MM/DD/YYYY’ ]**.
- **Locale:** The two-letter country code to identify a language. For example - **fr**, **en**.

---

#### Parse Object: Parses a date in object type to a moment object.

- **Object:** The object to be parsed. Example of an object - **{ year :2017, month :10, day :3, hour :15, minute :10, second :3, millisecond :123}**.

---

#### Parse Date: Parses a date object to a moment object.

- **Date Object: **The date object to be parsed. Example of a date object - **new Date(2021, 10, 11)**.

#### 

---

#### Parse Array: Parses a date array to a moment object.

- **Array: **The date array to be parsed. Example - **[2018, 10, 08, 10, 30, 40]**.

#### 

---

#### Unix Timestamp: Converts integer value in milliseconds and seconds to a moment object.

- **Timestamp: **The timestamp to convert.

---

#### UTC Parse String: Parses a string to a UTC time moment object.

- **Date:** The date (in string) to be parsed. Example - **21/02/2021**.

#### 

---

#### UTC Parse Date: Parses a date object to a UTC time moment object.

- **Date Object:** The date object to be parsed. Example - **date( 21/02/2021)**.
