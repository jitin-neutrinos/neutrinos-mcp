# HTML 5

<https://documentation.neutrinos.com/articles/#!components-guide-7/html>

## HTML 5

### Overview

The **HTML 5 **component is used to design components to be displayed in web format. When you drag and drop an HTML 5 component, the page container by default displays an HTML editor inside the HTML 5 component. This editor can be used to compose web content.

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

- **Element type**: A drop-down list of the HTML5 element types. See the [Element types](/articles/components-guide-7/html/a/h3__1172380815) section to learn how to configure them.

---

### Element Types

The HTML element types include:

#### Div

Used to add a division or a section.

---

#### Span

Used to group inline elements.

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

Used to put a display text on the component describing what purpose it has for the user.

---

#### Caption

Used to add a caption.

---

#### Fieldset

Used to group related elements in a form. This tag draws a box around the related elements.

---

#### iFrame

Used to embed another document within the current HTML document. Configure the following properties:

- **name**: Specify the name of the iframe attribute which is used to refer to the element in the javascript.
- **Sandbox**: Used to enable the extra set of restrictions for the content.
- **Src**: The source or address of the document.
- **Scrdoc:** Used to specify the HTML content of the page to display in the icon.
- **Width**: Specify the width of the iFrame.

**Example:**

- **srcdoc**=<p>Hello world!</p>
- **name**=iframe-name-list
- **src**=https://platform.twitter.com/widgets/tweet_button.html
- **sandbox**=allow-scripts allow-popups

When the app is deployed, click on the mentioned URL to see the pop-up window.

---

#### Audio

Used to specify a standard way to embed an audio file. Configure the following properties:

- **Autoplay**: If set to true, the Audio will play automatically.
- **Loop**: If set to true, it will play the audio on loop.
- **Add source**: Add multiple addresses of the Audio files along with its type.
- **AudioDatasource:** Provide the array which is used to handle the dynamic addresses of audio content where the user has initialized/specified the audio source.
- **Audio src**: Provide the audio embedded source. In the background, an object reference called audio is created. This can be used to refer to the audio source address as audio.src.
- **Audio type**: Provide the type of audio. This is used to refer to the type of audio as audio type.
- **(audioplay):** Event emitted when audio is played.
- **(audiopause)**: Event emitted when audio is paused.
- **(audioended)**: Event emitted when audio is ended.

**Example:**

Enter the following code in the TS editor

```javascript
play(){    console.log('play audio?')}pause(){    console.log('audio paused')}end(){    console.log('audio ended')}Audio=[{       url:"http://oliverspost.com/Non%20Stop%20Party%20Song.mp3",type:"mp3"   } ]
```

Enter the following properties in the attribute window

- Add source= source url=http://oliverspost.com/Non%20Stop%20Party%20Song.mp3
- (audioplay)=play()
- (audiopause)=pause()
- (audioended)=end()
- audioDatasource=Audio
- audioSrc=audio.url
- audioType=audio.type

When you deploy the app, the mentioned audio will render and the play, pause, and end events are emitted based on the actions done to the audio.

---

#### Video

Used to specify a standard way to embed an audio file. Configure the following properties:

- **Autoplay(True/False)**: If set to true, the video will play automatically.
- **Loop(True/False)**: If set to true, it will play the video on loop.
- **Add Source:** Adding multiple addresses of the Video files along with their type.
- **VideoDatasource**: Provide the array which is used to handle the dynamic addresses of the Video content where the user has initialized the video source.
- **Video src**: To provide the video source, in the background, an object reference called video is created. This can be used to refer to the video source address as video.src
- **Video type**: To provide the type of the video. This is used to refer to the type of the video as video. type.
- **(videoplay):** Event emitted when the video is played.
- **(videopause)**: Event emitted when the video is paused.
- **(videoended)**: Event emitted when the video is ended.

**Example**:

Add the following code in the TS editor

```javascript
Video=[{       url:"https://interactive-examples.mdn.mozilla.net/media/examples/flower.webm"   } ]      play(){    console.log('play video?')}pause(){    console.log('video paused')}end(){    console.log('video ended')}
```

Enter the following properties in the attribute window

- Add Source- source url=https://interactive-examples.mdn.mozilla.net/media/examples/flower.webm
- videoDatasource=Video
- videoSrc=video.url
- videoType=video.type
- (videoplay)=play()
- (videopause)=pause()
- (videoended)=end()

When you deploy the app, the video is rendered and the play, pause, and end events are emitted based on the action done on the video.

---

#### Plugin

Used to add a plugin. Configure the following property:

- **data**: Used to embed custom plugin data on the HTML element such as Flashplayer, PDF readers, Java applets.

**Example**:

- Element type=Plugin
- data=/assets/Web/Icons/favicon.png

When you deploy the app the image will be rendered.

---

#### Youtube

Used to display Youtube videos. Configure the following properties:

- **n****ame**: Name of the youtube video tag used to refer to the element in the javascript.
- **sandbox**: Used to enable the extra set of restrictions for the content.
- **src**: The embedded source or address of the video.
- **srcdoc:** Used to specify the HTML content of the page to display in the video.
- **width**: Specify the width of the youtube video player.

**Example: **

- name=youtube-video-list
- src=https://platform.twitter.com/widgets/tweet_button.html
- sandbox=allow-scripts allow-popups
- srcdoc= <p>Hello world!</p>

When you deploy the app, the YouTube video that is mentioned in the URL is rendered and a popup appears when the video is clicked.
