# HTML 5

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/html>

## HTML 5

### Overview

The HTML5 component is used to design components to be displayed in web format. When you drag and drop an HTML5 component, the page container by default displays an HTML editor inside the HTML 5 component. This editor can be used to compose web content.

### How to use

1. Drag and drop an **HTML5 **component to the page container. An HTML Editor is already added into the component by default.
2. Click the HTML Editor to open an editor on the page container. Design the HTML document according to your app requirement by adding tags. A few of the commonly used tags are described below:
  1. **Div**: Used to add a division or a section in an HTML document.
  2. **Span**: Used to group inline-elements in an HTML document.
  3. **Paragraph**: Used to insert a paragraph in an HTML document.
  4. **Header1 - 6**: Used to insert a header tag in an HTML document.
  5. **Label**: Used to put a display text on the component describing what purpose it has for the user.
  6. **Caption**: Used to add a caption to an HTML table.
  7. **Fieldset**: Used to group related elements in a form. This tag draws a box around the related elements.
  8. **iframe**: An inline frame is used to embed another document within the current HTML document.
  9. **Audio**: The audio tag used to embed audios of type MP3, Ogg, and WAV.
  10. **Video**: The video tag is used to embed videos of type MP4, WebM, and Ogg.
  11. **Plugins**: Used for extending the functionality of the web browser such as adding maps, PDf readers, Flash Players.
  12. **YouTube**: Used for embedding youtube videos.
3. Optionally add another HTML Editor if required.
4. Save and run the page.

### Associated Attributes

- **style**: Accepts a string value and affects different properties such as height, width, and color of the component based on the values provided. Example: background:orange;height:200px;.
- **class**: Used to point to a class in a style sheet. A class contains one or more style statements. Classes are created in the Styles editor by clicking Styles in the editor menu. The class attribute accepts space-separated class names. They are defined in the Style tab as shown below.

```css
class1 {border-radius:10px;flex-basis:10%;height:100px;}.class2 {border-radius:10px;flex-basis:10%;height:100px;}
```

- **Element type**: A drop-down list containing the following HTML5 elements:
- **Div:** Used to add a division or a section in an HTML document.
- **Span**: Used to group inline-elements in an HTML document.
- **Paragraph**: Used to insert a paragraph in an HTML document.
- **Header1 - 6**: Used to insert a header tag in an HTML document.
- **Label**: Used to put a display text on the component describing what purpose it has for the user.
- **Caption**: Used to add a caption to an HTML table.
- **Fieldset**: Used to group related elements in a form. This tag draws a box around the related elements.
- **iFrame**: An inline frame is used to embed another document within the current HTML document.
  - **name**: Specify the name of the iframe attribute which is used to refer the element in the javascript.
  - **Sandbox**: Used to enable the extra set of restrictions for the content.
  - **Src**: The source or addresses of the document.
  - **Scrdoc:** Used to specify the HTML content of the page to display in the icon.
  - **Width**: Specify the width of the iFrame.

**Example**:

- **srcdoc**=<p>Hello world!</p>
- ** name**=iframe-name-list
- **src**=https://platform.twitter.com/widgets/tweet_button.html
- **sandbox**=allow-scripts allow-popups

When the app is deployed, click on the mentioned URL to see the pop-up window.

- **Audio**: Specify a Standard way to embed an audio file on a webpage.
  - **Autoplay**: If set to true, the Audio will play automatically.
  - **Loop**: If set to true, it will play the audio on loop.
  - **Add source**: Add multiple addresses of the Audio files along with its type.
  - **AudioDatasource:** Provide the array which is used to handle the dynamic addresses of audio content where the user has initialized/specified the audio source.
  - **Audio src**: Provide the audio embedded source. In the background, an object reference called audio is created. This can be used to refer to the audio source address as audio.src.
  - **Audio type**: Provide the type of audio. This is used to refer to the type of audio as audio.type.
  - **(audioplay):** Event emitted when audio is played.
  - **(audiopause)**: Event emitted when audio is paused.
  - **(audioended)**: Event emitted when audio is ended.

**Example:** Enter the following code in the TS editor

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

When you deploy the app, the mentioned audio will render and the play,pause, and end events are emitted based on the actions done to the audio.

- **Video**:
  - **Autoplay(True/False)**: If set to true, the video will play automatically.
  - **Loop(True/False)**: If set to true, it will play the video on loop.
  - **Add Source:** Adding multiple addresses of the Video files along with its type.
  - **VideoDatasource**: Provide the array which is used to handle the dynamic addresses of the Video content where the user has initialized the video source.
  - **Video src**: To provide the video source, in the background, and object reference called video is created. This can be used to refer to the video source address as video.src
  - **Video type**: To provide the type of the video. This is used to refer to the type of the video as video.type.
  - **(videoplay):** Event emitted when the video is played.
  - **(videopause)**: Event emitted when the video is paused.
  - **(videoended)**: Event emitted when the video is ended.

**Example**: Add the following code in the TS editor

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

When you deploy the app, the video is rendered and the play,pause, and end events are emitted based on the action done on the video.

- **plugin:**
  - **data**: Used to embed custom plugin data on the HTML element such as Flashplayer, PDF readers, Java applets.

**Example**:

- Element type=Plugin
- data=/assets/Web/Icons/favicon.png

When you deploy the app the image will be rendered.

- **Youtube:**
  - **n****ame**: Name of the youtube video tag used to refer the element in the javascript.
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
