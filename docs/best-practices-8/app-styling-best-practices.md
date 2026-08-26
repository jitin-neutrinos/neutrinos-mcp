# Nesting the Selectors

<https://documentation.neutrinos.com/articles/#!best-practices-8/app-styling-best-practices>

# 

CSS is a must for giving your app a good look. But it lacks some modern features such as variables, reusable code, and nesting. That is where Sass (Syntactically Awesome StyleSheets) with Scss syntax comes to play.

That said, follow these best practices and conventions while styling your app:

### Nesting the Selectors

Selector nesting helps to structure your code using indentation. It denotes the relation between selectors or properties. That is, instead of being able to write nothing but CSS declarations in rulesets, it allows you to write inner rulesets that will then get compiled at root-level with the relevant selectors. For example, you can nest selectors to apply various styling to the footer container like this:

```html
<div class="footer-container">  <span class="terms"> Advise / arrange contract of insurance in respect of    Life Policies</span>  <div class="vertical-divider"> </div></div>
```

```css
.footer-container {  Background-color: green;   .terms {    font-size: 12px;    // You can also add pseudo selectors using this syntax    &:hover {       color: red;    }  }   .vertical-divider {    color: black;  }}
```

| ![Information](/resources/Storage/best-practices-8/info.png) | While using selector nesting, do not nest more than 3 to 4 levels. |
| --- | --- |

VariablesSCSS allows you to work with variables. These variables start with a dollar sign ($) and are different from CSS variables that start with a double dash. We recommend that you define the most common values using variables before starting any project in Neutrinos Studio. For example: ![Defining variables in the Styles editor](/resources/Storage/best-practices-8/styles_variables.png)CommentsAlways write section-wise comments. It helps you organize the styles in your stylesheet and quickly make changes as styles start getting bigger. For example:Copy CodeCSS/*START: Login Page */

 .input-error .mat-form-field {
 border: 1px solid $font_disabled_gray;
 }

 .login-button {
 background: $button-background;
 font-size: $large_font;
 }

/*END: Login page*/
MixinsA mixin allows you to package existing code into reusable chunks of CSS. This helps avoid rewriting the same piece of code every time you need it. Here is an example of a simple mixin that allows you to modify the button's properties. These properties once set can be reused across the project.Copy CodeCSS@mixin button-add($width, $height, $background, $color) {
 width: $width;
 height: $height;
 background-color: $background;
 color: $color;
 }
Once the mixin is defined, you can use them in your CSS like this:Copy CodeCSS.btn-add-client {
 @include button-add(150px, 75px, $background_primary, $font_secondary);
 // Add additional styles here
 }

.btn-continue {
 @include button-add(50px, 35px, $background_primary, $font_primary);
 // Add additional styles here
 }

Extend SelectorsSCSS allows you to extend selectors by copying and combining selectors in the CSS output. Interestingly, while the mechanism is very different, the semantics of @extend is quite analogous to traditional object-oriented programming languages (such as Java). That is, in the below example, .cat has all the properties of its parent class .animal, plus any specific ones it adds or overrides.
Copy CodeCSS.animal {
background: gray;
}

.cat {
@extend .animal
color: white;
}
Helper StylesWrite helper styles to avoid code redundancy. For example:Copy CodeCSS/*Helper styles*/

.center-element {
 display: flex;
 align-items: center;
 justify-content: center;
}

.p-0 {
 padding: 0px;
}

.p-3 {
 padding: 3px;
}

.ml-25 {
 margin-left: 25px;
}

.ml-30 {
 margin-left: 30px;
}
You can refer to more helper styles from here:[https://gist.github.com/jacurtis/30da4bf9a6c9b9b5cc0aebac512ca7c9](https://gist.github.com/jacurtis/30da4bf9a6c9b9b5cc0aebac512ca7c9)
[https://gist.github.com/prasofty/2b5f290e1d60f17b5acb](https://gist.github.com/prasofty/2b5f290e1d60f17b5acb)
Useful ResourcesApart from the best practices mentioned above, there are many websites that describe the best practices of using Sass. Here are a few for your reference:[http://sass-lang.com/](https://sass-lang.com/)
[http://www.sassmeister.com/](http://www.sassmeister.com/)
[https://github.com/NulledGravity/pib](https://github.com/NulledGravity/pib)
[https://github.com/engageinteractive/front-end-baseplate/blob/master/src/scss/utility/_mixins.scss](https://github.com/engageinteractive/front-end-baseplate/blob/master/src/scss/utility/_mixins.scss)
