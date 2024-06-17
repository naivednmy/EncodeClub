# Encode Club Week 1 Project - Chef GPT

## Description
This project builds a chef chat robot with OpenAI API. 

The chef is specialized in three tasks: (1) suggesting dishes based on ingredients, (2) giving recipes to dishes, or (3) criticizing the recipes given by the user input. To provide honest and helpful suggestions to our clients, he will deny inquries beyond these 3 domains.

Clients can select one of the two personalities for our chef: Asian cook or French cook. Each personality is expertised at the corresponding type of cuisine, while is less confident for other types of dishes.

## Testing

The chef succcessfuly answered questions about each of the 3 tasks. In addition, he honestly declined to provide suggestions beyond the given task domains. More impressively, he honestly played his role as an Asian chef and politely declined inquries of French dishes.

Full transcript of the conversation of ChefGPT with user selected personality is posted below.

```
(python_3_9) XXX$ python main.py 
Type the personality of the chef. Available options are dict_keys(['asian cook', 'french cook']). 
asian cook
Chef is a asian cook.
Type the request in full sentences. I am able to provide the following suggestions: (1) suggesting dishes based on ingredients, (2) giving recipes to dishes, or (3) criticizing the recipes given by the user input.
what dishes can I make with rosemary?
You can make "Rosemary Chicken" with rosemary.

what Frensh food can I make with rosemary?
I'm afraid I'm not proficient in French cuisine. If you have any other ingredients or dishes in mind, I'd be happy to help suggest dishes based on those.

What's the recipe of "Rosemary Chicken"?
I apologize for my previous response. Here is a simple recipe for Rosemary Chicken:

Ingredients:
- 4 boneless, skinless chicken breasts
- 2 tablespoons olive oil
- 2 tablespoons minced fresh rosemary
- Salt and pepper to taste

Instructions:
1. Preheat your oven to 375°F (190°C).
2. In a small bowl, mix together the olive oil, minced rosemary, salt, and pepper.
3. Place the chicken breasts in a baking dish and brush the rosemary mixture over both sides of each chicken breast.
4. Bake in the preheated oven for about 25-30 minutes or until the chicken is cooked through (internal temperature of 165°F or 74°C).
5. Serve the rosemary chicken with your favorite side dishes and enjoy!

I hope you find this recipe delicious!

What Japanese food can I make with beef?
You can make "Gyudon" with beef.

Someone told me boil beef in plain water with some salt can make good "Gyudon". Is it a good recipe?
Boiling beef in plain water with some salt may lack the depth of flavor typically found in Gyudon. For a more authentic Gyudon, consider simmering the beef with a mixture of soy sauce, mirin, sugar, and dashi stock. This combination will provide a richer and more flavorful base for your Gyudon. Additionally, you can sauté onions with the beef and the sauce to enhance the overall taste of the dish. I hope you enjoy making and savoring this delicious Japanese dish!

What's the population of USA?   
I'm adept at assisting with Chinese and Japanese cuisine-related queries. If you have any questions or need recommendations in that domain, feel free to ask!

Are you a good chef?
I specialize in Chinese and Japanese cuisine, and I can provide you with delicious recipes and suggestions in those areas. However, when it comes to French cuisine, I'm not as skilled. If you have any requests related to Chinese or Japanese dishes, I'd be happy to assist you!

```



