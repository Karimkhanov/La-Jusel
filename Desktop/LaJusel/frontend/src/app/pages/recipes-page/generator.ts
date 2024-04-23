import { IRecipe } from "src/app/models/models";

const carbonaraSteps: string[] = ["Cook spaghetti in a pot of salted boiling water until al dente.",  "While the pasta cooks, fry chopped bacon in a pan until crispy.",  "Beat eggs, grated parmesan cheese, and black pepper together in a bowl.",  "When the pasta is cooked, reserve some of the pasta water and drain the rest.",  "Add the drained pasta to the pan with the bacon and toss to coat the pasta in the bacon fat.",  "Remove the pan from the heat and pour the egg mixture over the pasta, stirring quickly to combine and coat the pasta.",  "If the mixture is too thick, add a small amount of the reserved pasta water to thin it out.",  "Serve immediately, garnished with more grated parmesan cheese and black pepper."]
const margaritaSteps: string[] = ["Preheat your oven to the highest temperature it can go.",  "Roll out your pizza dough and place it on a baking sheet or pizza stone.",  "Spread a layer of tomato sauce on the dough.",  "Add slices of fresh mozzarella cheese on top of the sauce.",  "Drizzle with olive oil and sprinkle with salt and pepper.",  "Bake in the preheated oven for 10-12 minutes, until the crust is golden brown and the cheese is melted and bubbly.",  "Remove from the oven and let cool for a few minutes before slicing and serving."]
const caesarSteps: string[] = ["Wash and chop a head of romaine lettuce and place it in a large bowl.",  "Add croutons and grated parmesan cheese to the bowl.",  "In a small bowl, whisk together olive oil, lemon juice, minced garlic, Dijon mustard, and Worcestershire sauce to make the dressing.",  "Drizzle the dressing over the salad and toss to coat the lettuce and croutons.",  "Serve immediately, garnished with more parmesan cheese and black pepper."]
const hamburgerSteps: string[] = ["Preheat a grill or grill pan to medium-high heat.",  "Season ground beef with salt and pepper and form into patties.",  "Grill the burgers for 3-4 minutes on each side for medium-rare, or longer for well-done.",  "Top each burger with a slice of cheese and let it melt for a minute.",  "Toast hamburger buns on the grill for a minute.",  "Assemble the burgers with your desired toppings, such as lettuce, tomato, onion, pickles, ketchup, and mustard.",  "Serve hot and enjoy!"]
const chickenSoupSteps: string[] = ["Heat oil in a large pot over medium-high heat.",  "Add diced onion, carrots, and celery to the pot and cook until softened.",  "Add minced garlic and cook for 30 seconds until fragrant.",  "Add chicken broth, diced chicken, and herbs to the pot.",  "Bring to a boil, then reduce heat to low and let simmer for 30-40 minutes.",  "Add diced potatoes and continue to simmer until the potatoes are tender.",  "Season with salt and pepper to taste.",  "Serve hot, garnished with chopped fresh parsley."]
const friedChickenSteps: string[] = ["Preheat oil in a deep fryer or a large pot to 350°F.",  "In a bowl, mix flour, salt, black pepper, garlic powder, and paprika.",  "Dip each piece of chicken in beaten eggs, then coat in the seasoned flour mixture.",  "Fry the chicken in batches for 10-15 minutes, until the coating is crispy and the chicken is cooked through.",  "Remove the chicken from the oil and let drain on a paper towel-lined plate.",  "Serve hot and enjoy!"]
const steakSteps: string[] = ["Preheat a grill or grill pan to high heat.",  "Season steak generously with salt and black pepper on both sides.",  "Grill the steak for 3-5 minutes on each side, depending on the thickness and desired doneness.",  "Remove the steak from the grill and let it rest for 5 minutes before slicing.",  "Serve hot and enjoy!"]



export const recipesList: IRecipe[] = [
    { id: 1, category_id: 3, name: 'Carbonara', image: 'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2021/02/05/Baked-Feta-Pasta-4_s4x3.jpg.rend.hgtvcom.616.493.suffix/1615916524567.jpeg', description: 'Delicious pasta recipe', steps: "carbonaraSteps" },
    { id: 2, category_id: 3, name: 'Margarita', image: 'https://static.toiimg.com/thumb/53110049.cms?width=1200&height=900', description: 'Yummy pizza recipe', steps: "margaritaSteps" },
    { id: 3, category_id: 1, name: 'Caesar Salad', image: 'https://natashaskitchen.com/wp-content/uploads/2019/01/Caesar-Salad-Recipe-3.jpg', description: 'Healthy salad recipe', steps: "caesarSteps" },
    { id: 4, category_id: 2, name: 'Hamburger Burger', image: 'https://images.pexels.com/photos/3616956/pexels-photo-3616956.jpeg?cs=srgb&dl=pexels-daniel-reche-3616956.jpg&fm=jpg', description: 'Good and delicious', steps: "hamburgerSteps" },
    { id: 5, category_id: 4, name: 'Chicken soup', image: 'https://hips.hearstapps.com/hmg-prod/images/lemon-chicken-orzo-soup-recipe-1646765355.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*', description: 'Amazing chicked soup', steps: "chickenSoupSteps" },
    { id: 6, category_id: 5, name: 'Fried chicken', image: 'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2011/6/3/1/FNM_070111-Fried-Chicken-026_s4x3.jpg.rend.hgtvcom.616.462.suffix/1382539796174.jpeg', description: 'Fried chicken like KFC', steps: "friedChickenSteps" },
    { id: 6, category_id: 5, name: 'Taco rabbed flank steak', image: 'https://www.thespruceeats.com/thmb/L54BnjGsRtPmwMhsJtWBnpNvDA0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/taco-rubbed-flank-steak-recipe-1805956-Hero-01_edit-2-141548be1eed407e9a51f4d1f616dd80.jpg', description: 'Tasty beef', steps: "steakSteps" },
];
