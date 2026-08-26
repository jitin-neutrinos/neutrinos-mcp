# File Upload

<https://documentation.neutrinos.com/articles/#!components-guide/file-upload5>

## File Upload

OverviewFile Upload is a button by clicking which the selected files can be uploaded.**Usage**When the user is needed to upload certain files (such as scanned images, log files, etc.), this component is used to provide that interface.How to useDrag and drop the “File Upload” component from the “Advanced” Category where it is needed on that page.Double click on the component and give values to the attributes.Save the changes.ExampleCreate a page called **page**.Drag and drop the **File Upload** component.Double click on that component.In **Ts** file, create a property called **uploadOptions** and set its value as below.uploadOptions = {"entityName":"users", "metadata":{"key":"abcj@gmail.com"} }Set the value of [uploadOptions] to **uploadOptions**.Write a function in Ts file as below: onSuccess(){ console.log("Succesfully uploaded!") }Save the changes.Open the address where the app is running.A button with **choose file** as its value should appear.Click the button, select the file to upload.Click on the button again to upload.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**[uploadOptions]:** Takes the name of the object that is defined in the Ts file. The object is of type: {"entityName": "user", "metadata":{"key": "aUniqueKey"}}Where ,“entityName” is the name under which the files with same “entityName” are grouped.“key” is used to uniquely identify the uploaded file. eg.uploadOptions = {"entityName":"users","metadata":{"key":"sankarshanaj@gmail.com"}}**(onSuccess):** Takes function (that is defined in Ts file) name as argument which will be called when the upload is successful. eg. `onSuccess()`**(indexChange):** Takes function (that is defined in Ts file) name as argument which will be called when an error occurs. eg. `onError()`**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
