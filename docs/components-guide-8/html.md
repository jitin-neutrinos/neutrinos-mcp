# HTML 5

<https://documentation.neutrinos.com/articles/#!components-guide-8/html>

## HTML 5

### Overview

The **HTML 5 **component is used to design components to be displayed in web format. When you drag and drop an HTML 5 component, the page container, by default, displays an HTML editor inside the HTML 5 component. This editor can be used to compose web content.

### How to use

1. Drag and drop an **HTML5 **component to the page container. An HTML Editor is already added to the component by default.
2. In the **Element Type** field, select the type of element to display on the application page. For example, **Header 1**.
3. On the HTML Editor, compose the web content. For example, if your **Element Type** is **Header 1**, then you can enter the header in the HTML Editor. For example - **This is a Level 1Header**.
4. Save and run the page.

### Associated Attributes

- **style**: Accepts a string value and affects different properties such as height, width, and color of the component based on the values provided. Example: background:orange;height:200px;.
- **class**: Used to point to a class in a style sheet. A class contains one or more style statements. Classes are created in the Styles editor by clicking Styles in the editor menu. The class attribute accepts space-separated class names. They are defined in the Style tab as shown below.

```css
class1 {border-radius:10px;flex-basis:10%;height:100px;}.class2 {border-radius:10px;flex-basis:10%;height:100px;}
```

- **Element type**: A drop-down list of the HTML5 element types. See the [Element types](/articles/components-guide-8/html/a/h3__1172380815) section to learn how to configure them.

---

### Element Types

The HTML element types include:

#### Div

Used to add a division or a section on the page. You can add any HTML element inside this element type.

---

#### Span

Used to group inline elements. It is used to mark up a part of a text, or a part of a document.

This element type is much like the **Div **element type, but** Div** is a block-level element and **Span** is an inline element.

To learn the difference between block-level and inline elements, see the [HTML documentation](https://www.w3schools.com/html/html_blocks.asp).

---

#### Paragraph

Used to insert a paragraph.

---

#### Header 1

Used to insert an H1 header tag.

---

#### Header 2

Used to insert an H2 header tag.

---

#### Header 3

Used to insert an H3 header tag.

---

#### Header 4

Used to insert an H4 header tag.

---

#### Header 5

Used to insert an H5 header tag.

---

#### Header 6

Used to insert an H1 header tag.

---

#### Label

Used to put a display text on the component, describing its purpose. The label acts as a caption for a specified element.

If you use the **Label **element type for form components, it increases the clickable area of the component, as clicking the label activates the form component as well.

---

#### Caption

Used to add a caption.

---

#### Fieldset

Used to group related elements in a form. This tag draws a box around the related elements.

---

#### iFrame

Used to embed another document within the current HTML document. Configure the following properties:

- **name**: Specify the name of the **iframe** attribute which is used to refer to the element in JavaScript.
- **Sandbox**: Enables an extra set of restrictions for the content in the iFrame.
- **Src**: The address of the document to embed in the iFrame.
- **Scrdoc:** Specify the HTML content to show in the iFrame.
- **Width**: Specify the width of the iFrame.

**Example:**

- **srcdoc**=<p>Hello world!</p>
- **name**=iframe-name-list
- **src**=https://platform.twitter.com/widgets/tweet_button.html
- **sandbox**=allow-scripts allow-popups
- **width** = 100%

When the app is deployed, click the URL to see the pop-up window.

---

#### Audio

Used to specify a standard way to embed an audio file. Configure the following properties:

- **Autoplay**: If set to true, the Audio will start playing automatically as soon as it loads.
- **Loop**: If set to true, the audio will be played on loop.
- **Add source**: Add one or more URLs of the Audio files along with their type.
- **AudioDatasource:** Provide the array which is used to handle the dynamic addresses of audio content where the user has initialized/specified the audio source.
- **Audio src**: Provide the audio embedded source.
- **Audio type**: Provide the type of audio. For example, Mp3, Ogg, etc.
- **(audioplay):** The event to be emitted when the audio plays. Enter the event name directly, or click ![the flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map a page/client flow to this field. See [Binding Page Flows](/smart/project-sample-how-to-guide/bind-page-flows-to-components) and [Binding Client Service Flows](/smart/project-sample-how-to-guide/import-client-services-to-the-page-ui) to learn more.
- **(audiopause)**: The event to be emitted when the audio is paused. Enter the event name directly, or map a page/client flow to this field.
- **(audioended)**: The event to be emitted when the audio ends. Enter the event name directly, or map a page/client flow to this field.

**Example:**

Enter the following properties in the attribute window:

- Select the Element type as **Audio**.
- Click the **Add Source** button and add the following details in the Add Source editor:
  - Source url = https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3
  - type = mp3
  - Click the** Add button **to add the URL to the list. Then, click **Save**.

When you deploy the app, the mentioned audio will render on the application page.

---

#### Video

Used to specify a standard way to embed an audio file. Configure the following properties:

- **Autoplay(True/False)**: If set to true, the video will play automatically as soon as it loads.
- **Loop(True/False)**: If set to true, the video will play on loop.
- **Add Source:** Add one or more URLS of the Video files along with their type.
- **VideoDatasource**: Provide the array which is used to handle the dynamic addresses of the Video content where the user has initialized the video source.
- **Video src**: The video source URL.
- **Video type**: The type of video. For example, Mp4, mkv, etc.
- **(videoplay):** The event to be emitted when the video plays. Enter the event name directly, or click ![the flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map a page/client flow to this field. See [Binding Page Flows](/smart/project-sample-how-to-guide/bind-page-flows-to-components) and [Binding Client Service Flows](/smart/project-sample-how-to-guide/import-client-services-to-the-page-ui) to learn more.
- **(videopause)**: The event to be emitted when the video is paused. Enter the event name directly, or map a page/client flow to this field.
- **(videoended)**: The event to be emitted when the video ends. Enter the event name directly, or map a page/client flow to this field.

**Example**:

Enter the following properties in the attribute window:

- Select the Element type as **Video**.
- Click the **Add Source** button and add the following details in the Add Source editor:
  - Source url = http://techslides.com/demos/sample-videos/small.mp4
  - type = mp4
  - Click the** Add button **to add the URL to the list. Then, click **Save**.

When you deploy the app, the video will render on the application page.

---

#### Plugin

Used to add plugins such as Java applets, PDF readers, and Flash Players to the application page. Configure the following property:

- **data**: Used to embed custom plugin data on the HTML element such as Flashplayer, PDF readers, Java applets.

**Example**:

- Element type = Plugin
- data = /assets/Web/Icons/favicon.png

When you deploy the app the image will be rendered.

---

#### Youtube

Used to display Youtube videos on the application page. Configure the following properties:

- **n****ame**: Name of the youtube video tag used to refer to the element in the javascript.
- **sandbox**: Extra set of restrictions that you want to apply for the content. For example, allow-same-origin.
- **src**: The source URL of the Youtube video. On Youtube, right-click the video and copy the embed code. The embed code will contain the URL of the video.
- **srcdoc:** The HTML content of the page to display in the video.
- **width**: The width of the youtube video player.

**Example: **

- name= Neutrinos Overview Video
- src = https://www.youtube.com/embed/llo1XzpJInM
- sandbox=allow-scripts allow-popups allow-same-origin
- Width= 80%

When you deploy the app, the YouTube video is rendered on the application page.
