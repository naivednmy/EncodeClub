import os
from openai import OpenAI

from models import ChefGPT

client = OpenAI()

chef_personality_list = {
    "asian cook": "You are talented at Chinese, Japanese cuisine, but awful at French food. When your clients ask for recipe or any information about French dishes, you must politely decline the request.",
    "french cook": "You are expertised at French cuisine. When your clients asks for recipe or any information beyond French cuisine, you should try your best to answer, but make sure to remind the clients you are not expertised at them." 
}

personality = input(f"Type the personality of the chef. Available options are {chef_personality_list.keys()}. \n")
print(f"Chef is a {personality}.")

ChefGPT(client, chef_personality_list[personality])
