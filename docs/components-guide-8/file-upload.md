# File Upload

<https://documentation.neutrinos.com/articles/#!components-guide-8/file-upload>

## File Upload

| ![Warning](/resources/Storage/components-guide-8/warning.png) | This component is not supported from Neutrinos Studio version 7.2.1. |
| --- | --- |

### Overview

File Upload is a button by clicking which the selected files can be uploaded.

### Usage

When the user is needed to upload certain files (such as scanned images, log files, etc.), this component is used to provide that interface.

### How to use

1. Drag and drop the **File Upload** component from the **Advanced** Category where it is needed on that page.
2. Double click on the component and give values to the attributes.
3. Save the changes.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the** Style** tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[uploadOptions]**: Takes the name of the object that is defined in the Ts file. The object is of type: {"entityName": "user", "metadata":{"key": "aUniqueKey"}}.Where ,

- “**entityName**” is the name under which the files with same “**entityName**” are grouped.
- “**key**” is used to uniquely identify the uploaded file.

For example: **uploadOptions**= "entityName":"users","metadata":"key":"abc@gmail.com"}}

- **(onSuccess):** Takes function (that is defined in Ts file) name as argument which will be called when the upload is successful. Example: onSuccess()
- **( exchangeindexChange)**: Takes function (that is defined in Ts file) name as argument which will be called when an error occurs. Example: onError()
- **(onerror)**: Event emitted when an error is found or detected.
- **disabled**: Disables the File upload property.

### Example

1. Create a page called page.
2. Drag and drop the File Upload component.
3. Double click on that component.
4. In Ts file, create a property called **uploadOptions** and set its value as below.

```javascript
uploadOptions = {"entityName":"users", "metadata":{"key":"abcj@gmail.com"} }
```

1. Set the value of [uploadOptions] to **uploadOptions**.
2. Write a function in Ts file as below:

```javascript
 onSuccess(){ console.log("Succesfully uploaded!") }
```

1. Save the changes.
2. Open the address where the app is running.
3. A button with choose file as its value should appear.
4. Click the button, select the file to upload.
5. Click on the button again to upload.
