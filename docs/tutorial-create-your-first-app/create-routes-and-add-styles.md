# Routes for the weather app

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/create-routes-and-add-styles>

| ![Information](/resources/Storage/tutorial-create-your-first-app/tutorial-create-a-leave-management-system/info.png) | Note that you need to create pages before you start configuring routes. |
| --- | --- |

**Creating and configuring Routes**

To create and configure [routes](/smart/project-concepts/routes), click the **Route** icon.

![Add routes](/resources/Storage/tutorial-create-your-first-app/tutorial-create-a-leave-management-system/routes.png)

When you create a route, you need to define a Path and select a [Page](/smart/project-concepts/page). To create a child route to the **home** route, click the arrow icon next to the home router.

### Routes for the weather app

### Add Application Styles

To add styling, click on the **Styles** icon on the left menu bar of the app editor.

#### Styling the weather app

Replace the styles editor with the code below

```css
/*Importing default angular material css theme. */@import "~@angular/material/prebuilt-themes/deeppurple-amber.css";@import "nDefaults.scss";body {    padding: 5px;}* {    box-sizing: border-box;    font-family: Roboto,"Helvetica Neue",sans-serif;}mat-grid-tile {  background: #b9c6d8;  border-radius: 4px;}.weathers {    padding: 0 5px;}.weather-card {    border: 2px solid rgba(0, 0, 0, 0.12);    border-radius: 15px;    width: 500px;}mat-card-title {    font-weight: bold;}.get-weather-button {    color: white !important;    background: #343438 !important;}
```
