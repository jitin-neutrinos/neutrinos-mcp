# Product Constant Usages

<https://documentation.neutrinos.com/articles/#!reels-publication/procons>

A product constant is a predefined value that takes the place of a number or string that does not change. They play a crucial role in defining the logic and behavior of the rules.

![](/resources/Storage/reels-publication/procons/procons1.png)

**Product Constant (With Runtime)**

The Runtime option is a component within the product constant, that facilitates the user to select an existing input or an output field as a value and use constant as a global variable. This feature can be activated by selecting the checkbox corresponding to runtime within the product constant screen.

![](/resources/Storage/reels-publication/procons/procons2.png)

### Product Constant Usages

Here's how product constants are used in a reels engine:

1. **Product Parameters**: Constants can represent product-specific parameters, such as price limits, quantity thresholds, or discount rates. For example, you might define a constant like MAX_PRICE to represent the maximum price allowed for a product.

2. **Eligibility Rules**: Constants can be used to define eligibility rules for products. These rules can determine whether a product qualifies for specific offers, discounts, or promotions. For instance, you might use a constant like ELIGIBILITY_AGE to specify the minimum age required to purchase a product.

3. **Discount Codes**: Constants can represent discount codes or promotional offers associated with products. You might define constants like DISCOUNT_CODE_PRODUCT_A or DISCOUNT_CODE_PRODUCT_B to apply discounts when certain products are in the shopping cart.

4. **Pricing Tiers**: Constants can define different pricing tiers for products. For instance, you might have PRICE_TIER_STANDARD and PRICE_TIER_PREMIUM to set different prices for the same product based on customer preferences.

**Use Case**

Let us consider an example where Customers whose policy duration is more than or equal 3 years get 5% discount on base premium. We will use the product constant feature for both scenarios (without applying runtime and after applying runtime).

#### Adding Product Constants without runtime

Follow the steps given below to add a product constant (without using runtime)

1. Create a Product.
2. Within the product constants tab, click on the ![](/resources/Storage/reels-publication/procons/addicon.png) icon.
3. The product constant window is displayed.
   ![](/resources/Storage/reels-publication/procons/Prodcons.png)
4. Enter the Constant name and value as 5.
   ![](/resources/Storage/reels-publication/procons/prodcons3.png)
5. Navigate to Rules Flow tab > click on Rule's Data button of the Decision rule node.
   The decision table config window is displayed. Enter the a product constant name in curly braces ( this is the constant name that we have already provided).
   ![](/resources/Storage/reels-publication/procons/procons4.png)
6. Click save.
7. Navigate to Data Mapping > select the source as Input and click save.
   ![](/resources/Storage/reels-publication/procons/IDM.png)
8. Go to Product Info > Enable Deploy toggle button > Click on Sandbox and execute the rule.

**View and Download this example**

To view this example, download the [Product Constant (without runtime)](https://drive.google.com/file/d/1eQHV1PnU0EKed4Ca1AgK7GGpHWVqPuPV/view?usp=sharing) sample and import it within the Reels platform. For more information about importing, refer to the [Import](/articles/reels-publication/importing-a-product) feature.

**Adding Product Constants with runtime**

Follow the steps given below to add a product constant (using runtime)

1. Create a Product.
2. Within the product constants tab, click on the ![](/resources/Storage/reels-publication/procons/addicon.png) icon.
3. The product constant window is displayed.
   ![](/resources/Storage/reels-publication/procons/Prodcons.png)
4. Select the checkbox corresponding to runtime > select the value from the source drop-down list.
   ![](/resources/Storage/reels-publication/procons/procons5.png)
   In this example, we will select the source for constant as user input at runtime and enter the constant name.
5. Click done and Navigate to Rules Flow > Data Mapping of the node.The Input Data Mapper window is displayed.
6. Select the Source as Policyyear ( this will be our product constant and will act as a global variable).
7. Click Save.
8. Navigate to Product Info > Enable Deploy toggle button > Click on Sandbox.
9. Enter a value for the Policyyear.
   ![](/resources/Storage/reels-publication/procons/polyear.png)
10. Click Submit and execute the rule.

**View and Download this example**

To view this example, download the [Product Constant (with runtime)](https://drive.google.com/file/d/14zAb5sYOe-mO5u8Nl3CstqNtRDw0Lxpn/view?usp=sharing) sample and import it within the Reels platform. For more information about importing, refer to the [Import](/articles/reels-publication/importing-a-product) feature.
