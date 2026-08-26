# Properties

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/log-page-ui>

On the [Page explorer](/smart/project-sample-how-to-guide/page-explorer), open the UI designer of the **Log** page. Drag and drop various components to the [canvas](/smart/project-concepts/canvas) and create the following layout.

### Properties

To configure the properties of a component, double-click the component. Its attributes window is displayed to the right.

Configure the properties of the components highlighted in this layout:

**Row 1**

**Basic properties**

- **Style: **padding:10px;
- **Layout Direction: **space-between
- **Perpendicular direction:** center

**Html5 1**

**Basic properties**

- **Style:** font-size:1em;font-weight:bold;
- **Element Type**: Div

Double click the **HTML editor** inside HTML5 and enter l**og**.

**Slide Toggle-1**

**Basic properties**

- **Slide toggle label: **toggle log visibility
- **text: **Toggle log visibility
- **Label Position: **before
- **(change): **page.showLog=$event.checked
- **checked:** true
- **Disabled: **False
- **Disable Ripple:** False
- **Disable Toggle Value:** False

Configure the next set of components highlighted below:

![log 2 of the layout](/resources/Storage/psd-tutorial-publication/log2.png)

**Column-2**

**Basic properties**

- **Style: **width:500px;
- **fxLayoutGap: **5px
- **Perpendicular Direction: **Start

**Custom properties**

In the **custom properties **section, select the **Key&Value** button and enter the values from the table respectively and click the **Add **button.

- ***ngIf:** page.showLog

**Html5- 2**

**Basic properties**

- **Style: **font-size:0.8em; margin-top:10px

**Custom Properties**

In the **custom properties** section, select the Key&Value button and enter the values from the table respectively.

- ***ngFor:** let logObj of logArray; let i = index
- **[ngStyle]:** {'color': logObj.type === 'error' ? 'red' : 'green'}

Double click the HTML editor inside HTML5 and enter  {{'- ' + logObj.message}}.

Save the changes.
