# Create Attributes

<https://documentation.neutrinos.com/articles/#!alpha-platform/model>

In Neutrinos Alpha Workflow Studio, a Model defines the information architecture encompassing all necessary attributes required to successfully execute the entire business process, including human tasks. It serves as a reference for structurally encapsulating search fields and data points, which can be accessed by various integrating services and user interfaces.

The Model editor allows data modeling in Workflow Studio. Data Modeling is the process of defining the structure of data elements and their relationships. A model acts as a container to hold various data types such as strings, booleans, and integers, represented as key-value pairs. Additionally, it supports complex data types, allowing connections to be nested structures, such as arrays and objects.

From a Case Instance perspective, a model represents Case Data. In terms of relationships between objects, Case Data serves as the top-level object. A 1-to-1 relationship is established by adding a single object, whereas a 1-to-many relationship is maintained by adding an array of objects. Users can input any type of string data, including URLs or reference IDs, which may facilitate linking between Case Instances when necessary. The image below illustrates relationship between objects, array of objects, and model in Workflow Studio.

![modelSample.jpg](/resources/Storage/alpha-platform/images/modelSample.jpg)

## Create Attributes

The attributes for a model can be added in the Visual Editor in the Workflow Studio. To add or create new attributes for a model, follow the steps below:

1. Navigate to **Model** editor in the Workflow Studio > In the Visual editor section, click the plus icon as shown in the image below:
    ![workflow-studio-create-attributes](/resources/Storage/alpha-platform/images/workflow-studio-create-attributes.png)
2. In the pop-up window, set the data type, enter the name of the attribute to be created > Click **Create** button.
    The image below shows the pop-up window to add Attribute in Visual Editor:
    ![](/resources/Storage/alpha-platform/images/workflow-studio-create-attribute-pop-up-screen.png)

The GIF below illustrates adding attributes to a sample project in Workflow Studio.

![workflow-studio-add-attribute-gif](/resources/Storage/alpha-platform/images/workflow-studio-add-attribute-gif.gif)

Observe, any Attribute, Object, or an Array added in the **Visual Editor** section, is converted into **JSON Schema** and is visible in the **Code Editor** section of the Model editor. The image below illustrates a sample JSON schema for the list of Objects and Attributes that are added in the Visual Editor:

![](/resources/Storage/alpha-platform/images/workflow-studio-visual-and-code-editor.png)

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | You can create or add individual attributes multiple times, or alternatively, add a complete JSON schema at once. Both panels update automatically to reflect changes made in either one. |
| --- | --- |

The GIF below illustrates how Visual Editor reflects changes when a complete JSON scheme is added.

![workflow-studio-add-complete-json-schema-gif](/resources/Storage/alpha-platform/images/workflow-studio-code-editor-json-complete-gif.gif)

## Add Object

An object is a logical entity that acts as a fundamental unit for storing and managing data within an application. Adding attributes without a defined structure can lead to ambiguity. By using objects, attributes in a model can be organized according to the specific requirements of the business process.

To add an Object in the Workflow Studio, select **Object** as the data type when creating or adding attributes. The GIF below demonstrates how to create an object in the studio to add sample list of attributes such as **name** and **dob** for a **Person** object:

![workflow-studio-create-object-gif](/resources/Storage/alpha-platform/images/workflow-studio-create-object-gif.gif)

Additionally, you can create an Array of objects by choosing the data type as **Array**. The table below summarizes the data types supported in Workflow Studio.

| **Data Type** | **Description** |
| --- | --- |
| True or False | Accepts boolean values that can contain either a True or a False value. |
| Text | Accepts string values that include Alphanumerical values. For example: policy ID and policy type. |
| Number | Accepts only numeric values. For example: premium amount. |
| Date | Accepts date-related values. For example: start date and end date. |
| Array | Accepts a list of items. For example: writers - an array of objects representing policy writers. |

| ![Note](/resources/Storage/alpha-platform/note.png) | Click the '**Plus**' button from the top-right corner on the Visual Editor screen to add individual objects. The '**Plus**' sign next to an object creates a child to that specific object. |
| --- | --- |

## Initialize

Initializing a project in the Workflow Studio is essential to ensure the Model and the JSON Schema are updated. This enables you to access these attributes or objects from or in the other components in the project.

| ![Warning](/resources/Storage/alpha-platform/warning.png) | Project initialization is mandatory for Enquiry and Filters to function for Workbench users. |
| --- | --- |

To initialize the project, click **Initialize Project** button on the top-right corner in the **Models** page. The image below shows the Initialize button in the Models page:

![workflow-studio-initialize-project-image](/resources/Storage/alpha-platform/images/workflow-studio-initialize-project.png)

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | The **Initialize Project** button re-appears every time the **JSON schema** or **Visual Editor** reflects a change. |
| --- | --- |
