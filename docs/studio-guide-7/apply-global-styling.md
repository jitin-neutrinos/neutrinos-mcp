# Importing Styles

<https://documentation.neutrinos.com/articles/#!studio-guide-7/apply-global-styling>

Styles allow you to separate the details of your app design from the UI structure and behavior. This is similar to stylesheets in web design. It is a collection of attributes that specify the appearance of an app. It can specify attributes such as font color, font size, background color, and much more.

In Neutrinos Studio, there are two ways to add Global (Application wide styles) styles to an application. You can add styles directly, or import styles. To apply global styling to your app, navigate to your [Studio Application page](/articles/concepts-publication/studio-application-page), select **Styles** in the editor pane.

![Styles editor](/resources/Storage/studio-guide-7/style.png)

Using the Styles editor, you can update the Angular material theme or write custom CSS and SaSS code in this editor.

### Importing Styles

To import Angular styles in your application, click **Styles** in the Editor pane of the application page and import the style of your choice. For example:

```css
/*Importing default angular material css theme. */@import "~@angular/material/prebuilt-themes/deeppurple-amber.css";@import "nDefaults.css";
```

### Adding an external style sheet

To add external style sheets:

**Copy them locally**

For example to include bootstrap 4 you can copy the latest version from the link [https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css](https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css) and copy it in the Styles editor.

```css
/*Importing the Bootstrap theme. */@import "bootstrap.min.css";
```

**Installing the npm Package**

Install the npm package provided by the third-party libraries. The CSS files will be copied under the node_modules folder. Copy the file and add it to the styles editor. To learn how to add an npm dependency to your app, see [Add npm dependency](/articles/studio-guide-7/manage-app-dependencies).

### Adding Styles Directly

Edit the Styles sheet and add the CSS and SaSS styles manually.

| ![Information](/resources/Storage/studio-guide-7/info.png) | You can add the component-specific styles in individual components, which will override the global styles. |
| --- | --- |

---

| **Learn More:** |
| --- |
| [App Styling Best practices](/articles/best-practices/app-styling-best-practices) |
