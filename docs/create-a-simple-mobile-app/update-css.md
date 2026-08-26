# Update CSS

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/update-css>

You add application specific styles in the [styles editor](/smart/project-sample-how-to-guide/apply-global-styling). All the styles added to the styles editor will be available throughout the application and can be applied to the page component's class property in the Attributes window.

** Style Editors**

To add styling, click on the **Styles** icon on the menu list of the app editor.

**Style for this app**

Add the following CSS style sheet in the editor. The CSS classes will then be called when configuring the component.

```css
/*Importing default angular material css theme. */// @import "~@angular/material/prebuilt-themes/deeppurple-amber.css";@import "~@angular/material/prebuilt-themes/indigo-pink.css";@import "nDefaults.scss";@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');*:not(mat-icon) {    font-family: 'Roboto' !important;}bh-home, bh-greetings, bh-userslist, bh-captureinfo {    height: 100%;}.layout-column {    height: calc(100% - 56px);}.sidenav-container {  position: absolute;  top: 0;  bottom: 0;  left: 0;  right: 0;}.hundred-height {    height: 100%;}.toolbar-background {    background: #ffffff;}.logo-size {    max-width: 50%;    max-height: 50%;}.listitem-padding {    padding: 1em 2em;}.center {  display: block;  margin-left: auto;  margin-right: auto;  max-width: 50%;}.mat-header-cell {padding: 0.5em!important;font-size: 0.75em;}.mat-cell {padding: 0.5em!important;font-size: 0.7em;}.red-background {    background: #f22129;}.card-font {    color:#ffffff;    font-size: 0.75em;}.mat-grid-tile .mat-figure {    justify-content: flex-start !important;}.rcorners1 {  border-radius: 20px;  background: #ffffff;//   width: 100%;//   height: 90%;}.sidenav-style {    border-top-right-radius: 20px;    border-bottom-right-radius: 20px;    width: 220px}.red-gradient {  background: linear-gradient(to bottom, #f22129 0%, #f22129 29%, #f22129 44%, #f22129 61%, white 49%);}.card-shadow {    box-shadow: 0 9px 38px 0 rgba(0, 0, 0, 0.16);}
```
