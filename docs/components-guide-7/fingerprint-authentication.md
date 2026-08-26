# Fingerprint Authentication

<https://documentation.neutrinos.com/articles/#!components-guide-7/fingerprint-authentication>

## Fingerprint Authentication

### Overview

This is a custom directive based on Cordova to authenticate users by using the fingerprint or face ID (iPhone X) saved on the device. It can be used only on mobile apps. To use this directive, add the n-fingerprint custom directive to a component.

| ![Information](/resources/Storage/components-guide-7/info.png) | Make sure the version 2.0.0 of the [cordova-plugin-fingerprint-aio](https://www.npmjs.com/package/cordova-plugin-fingerprint-aio) plugin is installed. |
| --- | --- |

### Usage

Once this directive is added to a component, the click() event is triggered on the component with the following functions:

- A message box asking the user to verify his/her identity using a fingerprint or face ID.
- Once the user verifies his/her identity using the fingerprint sensor on the mobile, a success string is returned.

### How to use

1. Drag and drop a component to the page container, and then add the following key-value pairs in the **Custom Properties **section of the component's attributes window. If the value field is missing, then leave it empty. If an input needs to be added to the value field, click the **Key&Value** tab and this makes the value field editable.
  1. Add the directive as an attribute.
    - **key**: (n-fingerprint)
    - Leave the value field empty
    - Click the **ADD** button
  2. Provide the options that the directive will use.
    - **key** : (fingerprint option)
    - **value** : {clientId: 'string', clientSecret: 'string'}
    - Click the **ADD** button
  3. Input the action that occurs if the directive successfully completed its functionality.
    - **key** : (onsuccess)
    - **value** : success($event)
    - Click the** ADD** button
    - Then is TS editor add the following function success($event){console.log($event)}
  4. Input the action that occurs if the directive failed to complete its functionality.
    - **key** : (onerror)
    - **value** : error($event)
    - Click the **ADD** button
    - Then is TS file add the following function error($event){console.log($event)}
2. The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per the developer's requirement.

| ![Information](/resources/Storage/components-guide-7/components-guide-for-release-6/info.png) | console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
