from js import Response
import random

business = ["a coffee roastery", "a pizza shop", "an animal shelter", "a street food vendor"]
concepts = ["landing page", "a nav menu", "a chatbot", "an order review screen"]

async def on_fetch(request, env):
    return Response.new("{ \"business\": \"" + random.choice(business)+ "\", \"concept\": \""+ random.choice(concepts)+ "\" }")
