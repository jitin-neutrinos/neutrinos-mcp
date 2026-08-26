# Card

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/card>

## Card

### Overview

The Card component is a content container for text, photos, and actions in the context of a single subject.

A card can contain many sub-components such as card title, card subtitle, card image, card action, card header, and card footer. These sub-components can be inserted within a card by clicking on the Add options provided at the bottom of the card. Further, each sub-components component can be sorted within a card according to your application requirements. Also, the properties of each sub-component can be configured by clicking on the component and updating its Attribute window. Therefore, you can call Card as an advanced component that groups all card sub-components together and displays it as a single block.

When you add a **Card **component to a page container, by default, sub-components such as the **card title, card subtitle, card image, card action, card header**, and** card footer** are already added within the** Card**. You can also add other palette components into a **Card**. For example, you can add a **Row** component to a card and configure its behavior.

### How to Use

- Drag and drop a **Card** component to a page container.
- (optional) Add sub-components such as **card title**, **card subtitle**,** card image**, **card action**, **card header**, and **card footer **to the **Card** by clicking respective options at the bottom of the card.
- Click the respective component and set its attributes/behavior using the Attributes window.

### Associated Attributes

**Basic Properties: **These properties remain the same for all **Card** components.

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

| Copy CodeCSS |
| --- |
| .class1 {  border-radius:10px;  flex-basis:10%;  height:100px; } .class2 {  border-radius:10px;  flex-basis:10%;  height:100px; } |

**Other Properties: **These properties are unique to each component:

#### Card: It is a content container for card sub-components.

- **card label:** The display name of the Card.
- **tabindex:** Specifies the index of the selected Card sub-component.

**Card Title:** A **Card Title** can be used to give a title to any block. It contains a text value.

- **Title:** Title of the Card. This field accepts string value and displays the inserted value as the card title, applying bold property.
- **Align:** Select an alignment from the drop-down list to align the **Card Title**.
  - **Right:** Aligns the card title to the right.
  - **Left:** Aligns the card title to left.
  - **Center: **Aligns the card title to the center of the Card.
- **Justify: **defines how the browser distributes space between and around content items along the main axis of a flex container, and the inline axis of a grid container.

**Card Sub-Title:** A **Card Sub-Title **can be used to give a subtitle to any block. It contains the text value. It is used below the title component.

- **Sub Title: **Sub-title of a card. This field accepts string value and displays it as the card sub-title on the page.
- **Align:** Select an alignment from the drop-down list to align the card title to the right, left, center, or justify.

**Card Image: **A card image component can be used to display an image inside the Card.

- **alt: **Alternate text for the image. This text will be displayed instead of the image when the image does not load. For example, alt text can be Image not available.
- **Assets src: **Stores the source path of the image. It displays the image if the image is present in the path that is specified. For example,** android\wallpaper.jpg** displays the image which is in .jpg format.
- **[src]: **The source location of the image
- **Secure URL:** The Secure URL of the image. If you do not use a secure URL, app users may get warnings that the app contains insecure data.
- **[collection name]:** Name of the collection
- **[image filter]:** Image filters (if any).

**Card Content:** A **Card Content** is a container in which you can insert a paragraph or text. It is basically intended to display a block of text. You can add other palette components into a card content.

- **Align:** Select an alignment from the drop-down list to align the card title to the right, left, center, or justify. Justify defines how the browser distributes space between and around content items along the main axis of a flex container, and the inline axis of a grid container.

**Card Action**: A **Card Action** can be used as a container of buttons, wherein clicking a button should perform some action.

- **Align:** Select an alignment from the drop-down list to align the card title to the right, left, center, or justify. Justify defines how the browser distributes space between and around content items along the main axis of a flex container, and the inline axis of a grid container.

**Card Header**: A **Card Header** contains the card title, card subtitle, and card image as attributes within it. It cannot contain any other component inside it. Multiple card headers can be inserted into a card.

- **title: **Accepts string value and the text will be displayed as the title of the card in the bold property.
- **subtitle: **Accepts string value and the text will be displayed below the title attribute in normal text.
- **Assets src: **This attribute stores the path of the image stored in the system and it displays the images based on the path (if present).
- [src]: The source location of the image.
- **alt: **Alternate text for the image. This text will be displayed instead of the image when the image does not load. For example, alt text can be Image not available.
- **[src]:** The source location of the image.
- **Secure URL: **The Secure URL of the image. If you do not use a secure URL, app users may get warnings that the app contains insecure data.
- **[collection name]:** Name of the collection
- **[image filter]:** Image filters (if any).

**Card Footer**: A card footer component can be used where the data should be displayed as footer, at the bottom of any container. It can contain data such as string value, logo or any content inside it.

- **card label:** Name of the card.
- **tabindex: **Specifies the index of the selected Footer component.

### Example

Display a Card with a title, image, and a paragraph

1. Drag and drop a **Card **component to the page container.
2. Select the **Card Title** component inside the card. In the card title Attributes window, set the card title as** Blog**.
3. Now, double click the **Card Image** component. In the Attributes window, enter assets location as \android\wallpaper.jpg in the Assets src field. This sets the path of the image to the image stored in the assets folder.
4. Save and run the page.

A Card component with the title as **Blog** and a wallpaper image will be displayed on the screen.
