# Cardstack

<https://documentation.neutrinos.com/articles/#!components-guide-8/cardstack>

Cardstack**Cards** form the building blocks that allow for bringing in data from disparate sources, beautiful UI animations, encapsulated and flexible data schemas, and a quick ramp-up experience. The Cardstacks provide a full-stack development environment, meaning that it spans everything from the front-end browser experience to API layers, to the database and caching. OverviewThis is a swipe-able cards interface that allows a user to swipe a stack of cards up, down, left or right. The cards for this example contains static images. When a card is dragged past a point it gets destroyed. This template is responsive across all devices and screen sizes.UsageIt can be used in any application that provides functionality on the swipe of cards. It can also be seen in other applications. For example, a shopping cart, where swiping right on a product, adds it to the cart and swiping left, removes the item from the user's suggestions list.How to UseDownload the **cardstack** template from Neutrinos Store.Install the template in Neutrinos Studio.When creating a new app select the **cardstack** template from the **ENTER APP DETAILS** menu, and click the **CREATE** button.Create a component where you would like to display the cards.For example: The cardstack componentImport **angular2-swing** into your component.In appmodule.ts,import the Swing module.Copy CodeJavaScriptimport {SwingModule} from â€˜angular2-swingâ€™;

@Ngmodule({

 imports:[SwingModule]

 })
Define the configurations in your **component** class and give the allowed directions.Copy CodeJavaScript stackConfig:StackConfig = {

 allowedDirections: [Directions.LEFT,

 Directions.RIGHT,

 Directions.UP,

 Directions.DOWN]

 }
If the user swipes a card in a direction that is not specified in the **allowedDirections** array, the card returns back to its original position once the swipe action is complete.If the user swipes a card in a direction that is specified in the **allowedDirections** array, the card gets popped out and when it is past a certain threshold it gets destroyed.The **allowedDirections** array is user Configurable.Import the **stackservice **into your component.Copy CodeJavaScript`import {stackserviceService}

from../services/stackservice/stackservice.Service`
Inject the **stackservice** service the constructor.Copy CodeJavaScriptconstructor(public stackservice:stackserviceService)
When a card is swiped and popped, a snack bar appears showing a message containing the direction in which the card was swiped. Depending on the direction in which the card was swiped, the user can perform functions based on the user's requirement.When a card is popped out the number of cards remaining in the array is shown on the User Interface.A total number of cards remaining in the stack is shown by using a fab in the User Interface and this number can be used to perform functionalities according to the user requirements. Create a new component, drag and drop the custom Html to invoke the cardstack component- <bh-cardstack></bh-cardstack>.
