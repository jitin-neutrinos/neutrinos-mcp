# Perform the following steps:

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/log-page-flow>

You will be designing this flow in the log page to define variables that have to be initialized when the page is triggered.

![](/resources/Storage/psd-tutorial-publication/2021-08-26_20h47_45.png)

#### Perform the following steps:

1. Open the flow designer of the **log **page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. In the **On Init** node, add the following Page Input Variable.
    **Property**
    **Value**
    **Action**
    logArray
    []
    Click the + icon to add the page input variable.
    ![](/resources/Storage/psd-tutorial-publication/image-2021-08-26.png)
3. In the **Page Variable** node, set the following properties:
  1. **Operation Type** - Set page variables
  2. **Variables List** - Add a page variable called showLog, To set the default value, select **as is** and enter True
      .
      ![](/resources/Storage/psd-tutorial-publication/image-2021-08-26-1.png)
