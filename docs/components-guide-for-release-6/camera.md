# Camera

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/camera>

## Camera

### Overview

The **camera** is a custom directive based on Cordova to take pictures using the camera and upload the file. It can be used only on mobiles. If you want to use this add an n-camera custom directive to any component.

### Usage

This directive can be added to any component. Once this directive is added to any component click event is triggered the following functions:

- The camera on the mobile device will open.
- The user is provided the option to take a picture.
- Once a picture is taken it is saved to the local device and uploaded.

### How to use

1. Drag and drop any component and then add the following key-value pairs using the New property: Attribute section of the HTML page.

**Note:** If the value field is missing then leave it empty. If an input needs to be added to the value field, click the **Key&Value** tab and edit the value.

2. Add the directive as an attribute.

- **key:** (n-camera)
- Leave the value field empty.
- Click the **ADD** button.

3. Provide the options that the directive will use.

- **key**: (cameraOptions)
- **value **: {entityName: 'profile', metadata: {key: 'example@neutrinos.co'}}
- Click the **ADD** button.

4. Input the action that occurs if the directive successfully completed its functionality.

- **key** : (onsuccess)
- **value** : success($event)
- Click the **ADD** button.
- Then in the TS editor add the following function success($event){console.log($event)}

5. Input the action that occurs if the directive failed to complete its functionality.

- **key** : (onerror)
- **value** : error($event)
- Click the **ADD** button.
- Then in the TS editor add the following function error($event){console.log($event)}

The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per the developer's requirement.

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
