# Rich Text Editor

<https://documentation.neutrinos.com/articles/#!components-guide-8/rich-text-editor>

## Rich Text Editor

### Overview

A text editor is used to edit plain text. A Rich text editor provides advanced functionalities where you can not only edit text, but also style, format, and link it. You can also add videos and images to the editor. To do that, the Rich Text Editor component shows a boxed editing area with a toolbar, placed on the top of it.

This component is built using the primary open-source project named [CKEditor](https://ckeditor.com/docs/ckeditor5/latest/index.html).

| ![Information](/resources/Storage/components-guide-8/info.png) | Make sure you have Neutrinos Studio version 7.2.2 and above to use this component |
| --- | --- |

### Usage

The rich text editor provides a number of options for you to style your text. The options include:

You can manually configure the visibility of these options through the attributes window.

### How to use

1. In your application, click Plugins and click Manage Plugins.
2. The Plugins Manager opens up. navigate to the App Plugins tab. Click Go to Store and download Rich Text Editor from Neutrinos Store.
3. Once installed, the component should show up in the palette list. Drag and drop a component from the palette list to the page.
4. Open the Default Terminal on Studio and run the following commands:

```markdown
// Install the ckeditor package$ npm install --save @ckeditor/ckeditor5-build-classic
```

1. Navigate to the Page Flow Designer, drag and drop a Use Dependency node to the On Init flow and import the **Rich Text Editor** component library. ![](/resources/Storage/components-guide-8/title-2021-10-19-1.png)

1. Save the page and run your application.

### Associated Attributes

- **Style**: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (Example- background:orange;height: 200px;).

- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {border-radius:10px;flex-basis:10%;height:100px;}.class2 {border-radius:10px;flex-basis:10%;height:100px;}
```

- **[editor]**: provides the static create() method to create an instance of the editor.
- **placeholder**: The display name of the component. For example, The three greatest things you learn from traveling.
- **[data]:** The initial data of the editor. For example, adding **'<p>Hello World!</p>'** will display Hello World when the editor is loaded on run-time.
- **Disabled**: Disables the edit operation on the editor. This is used to control the editor’s read-only state.
- **(ready)**: Fired when the editor is ready. It corresponds with the editor #ready event. It is fired with the editor instance. For example, you can set the value of this attribute to **onReady()** and define the** onReady()** function in the Script node of the page flow designer.

```javascript
onReady() {  alert("Ready!");}"
```

- **(change):** Fired when the content of the editor has changed. It corresponds with the editor.model.document#change:data event. For example, you can set the value of this attribute to onChange() and it in the Script node of the page flow designer.

```javascript
onChange() {  alert("Changed!");}"
```

- **(focus):** Fired when the editing view of the editor is focused. It corresponds with the editor.editing.view.document#focus event. For example, you can set the value of this attribute to onFocus() and define it the Script node of the page flow designer.

```javascript
onFocus() {  alert("Focused!");}"
```

- **(blur)**: Fired when the editing view of the editor is blurred. It corresponds with the editor.editing.view.document#blur event. For example, you can set the value of this attribute to onBlur() and define it in the Script node of the page flow designer.

```javascript
onBlur() {  alert("Blurred!");}"
```

- **Manual Configuration**: If set to TRUE, the attributes window allows you to manually configure the options to be displayed on top of the editor. The options that you can show/hide include: ![](/resources/Storage/components-guide-8/components-guide-7/1-1-7-1-rich-text-editor-img0001.png)
  - **Show Heading**: Set to TRUE to show the Heading drop-down option on the top of the editor.
  - **Show Bold**: Set to TRUE to show the Bold option on the top of the editor.
  - **Show Italic**: Set to TRUE to show the Italic option on the top of the editor.
  - **Show Undo**: Set to TRUE to show the Undo option on the top of the editor.
  - **Show Redo**: Set to TRUE to show the Redo option on the top of the editor.
  - **Show Bullet List:** Set to TRUE to show the Bullet List option on the top of the editor.
  - **Show Number List:** Set to TRUE to show the Number List option on the top of the editor.
  - **Show Block Quote**: Set to TRUE to show the Block Quote option on the top of the editor.
  - **Show Link**: Set to TRUE to show the Link option on the top of the editor.
  - **Show Uploading Image**: Set to TRUE to show the Uploading Image icon on the top of the editor.
  - **Show Insert Table:** Set to TRUE to show the Insert Table icon on the top of the editor.

### Example

1. In the **Page Flow Designer **of the page, add a page variable in the Page Variable node of the **On Init** flow.
2. Double click the Page Variable node and enter the following properties:
  1. Operation Type: Set Page Variables
  2. Variables List: **Variable name**
     **Default value**
     Editor
     Select **as is** and enter **ClassicEditor**
  3. ![](/resources/Storage/components-guide-8/rich-text-editor-2021-10-19.png)
3. Navigate to the UI editor of the page, drag and drop the **Rich Text Editor** component to a page.
4. Double click the Rich Text Editor component and set the following properties:
  1. **[editor]**: page.Editor
  2. **[data]**: '<p>Hello World!</p>'
5. Save and run the page.

Once the page is loaded, you can use the rich text editor in runtime and edit the view of the webpage.
