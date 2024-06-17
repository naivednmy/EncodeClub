def ChefGPT(client, chef_personality):
    messages = [
        {
            "role": "system",
            "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
        }
    ]
    messages = [
        {
            "role": "system",
            "content": f"{chef_personality}",
        }
    ]
    messages.append(
        {
            "role": "system",
            "content": "".join(["Your client is going to ask for three categories of suggestions: (1) suggesting dishes based on ingredients, ",
                                "(2) giving recipes to dishes, or (3) criticizing the recipes given by the user input.\n",
                                "If what the client is asking for does not belong to the above 3 scenarios, you should deny the request and ask to try again. ",
                                "If the client passes one or more ingredients, you should suggest a dish name that can be made with these ingredients. But suggest the dish name only, and not the recipe at this stage. ",
                                "If the client passes a dish name, you should give a recipe for that dish. ",
                                "If the client passes a recipe for a dish, you should criticize the recipe and suggest changes.\n",
                                "If you don't understand the client's request, you must honestly say you don't know and ask to try again."])
        }
    )

    task = input("Type the request in full sentences. I am able to provide the following suggestions: (1) suggesting dishes based on ingredients, (2) giving recipes to dishes, or (3) criticizing the recipes given by the user input.\n")

    messages.append(
        {
            "role": "user",
            "content": f"Suggest me {task}"
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

    while True:
        print("\n")
        user_input = input()
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)
        
        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )