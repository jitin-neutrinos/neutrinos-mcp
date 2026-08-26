# Add assets and style

<https://documentation.neutrinos.com/articles/#!create-a-widget-on-studio-8/add-styles-and-assets>

You have already created the studio package and component(s) by following the steps mentioned in the below topics:

- [Create a Studio Package](/articles/create-a-widget-on-studio-8/create-a-studio-package)
- [Create a Component](/articles/create-a-widget-on-studio-8/create-component-file) or [Create an Advanced Component](/articles/create-a-widget-on-studio-8/create-advanced-component-file)

### Add assets and style

| ![Information](/resources/Storage/create-a-widget-on-studio-8/info.png) | Make sure you reread the steps multiple times and verify the contents of the studio package before you test it on Neutrinos Studio. |
| --- | --- |

1. [Add assets](/articles/create-a-widget-on-studio-8/add-styles-and-assets/a/addassets)
2. [Add styles](/articles/create-a-widget-on-studio-8/add-styles-and-assets/a/addstyles)

**Step 1: Add Assets**

In your studio package, create an **assets** folder. Within the **assets** folder, create an** icons** folder and upload your component's icons. Icons are used to display the component in the palette list. Such as:

Within the **assets** folder, create an **images** folder and add the component's image. The component's image is used to display a preview of the component when dragged and dropped to a page container. Such as:

**Step 2: Add Styles**

If you want to style your component, inside your component's package, create a** styles** folder. Within the **styles** folder, create an **index.css** file and write your CSS script in it. If you are using classes in your CSS script, you should prefix the class names with your package name so that the package's CSS doesn't conflict with the studio CSS.

Example:

```css
.drop-view{background: #d9e8ff!important; }.drop-container {border: 1pxsolid#ccc!important;border-radius: 5px;background: white!important;display: table;min-width: calc(100%-50px);height: 100%;margin: 0px!important;outline: none!important;}
```
