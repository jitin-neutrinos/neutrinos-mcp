# Text To Speech

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/text-to-speech>

## Text To Speech

### Overview

Text to Speech (tts) is a custom directive based on Cordova to speak out the text input into the directive. It can be used only on mobiles. If you want to use this add an **n-tts** custom directive to any component.

### Usage

This directive can be added to any component. Once this directive is added to a component, the click() event is triggered with the following functions:

- The text is converted into speech.
- Then it is spoken out using the device's speaker.

### How to use

1. Drag and drop any component to the page container. Add the following **key-value** pairs using the **New property** Attribute section of the HTML page. If the value field is missing then leave it empty. If an input needs to be added to the value field, click the **Key&Value** tab and the value field becomes editable.
  1. Add the directive as an attribute.
    - **key**: (n-tts)
    - Leave the value field empty
    - Click the **ADD** button
  2. Provide the options that the directive will use.
    - **key** : (ttsOptions)
    - **value** : {text: 'Enter your text', locale: 'en-GB', rate: 1}
    - Click the **ADD** button
  3. Input the action that occurs if the directive successfully completed its functionality.
    - **key** : (onsuccess)
    - **value** : success($event)
    - Click the **ADD** button
    - Then is TS editor add the following function success($event){console.log($event)}
  4. Input the action that occurs if the directive failed to complete its functionality.
    - **key **: (onerror)
    - **value** : error($event)
    - Click the **ADD** button
    - Then is TS editor add the following function error($event){console.log($event)}
2. The console.log($event) line inside the values of the (onsuccess) and (onerror) keys can be changed as per your requirement.

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Console.log($event) displays the output (which is $event) of the directive for both success and error on a console which can be accessed by google chrome or safari. |
| --- | --- |
