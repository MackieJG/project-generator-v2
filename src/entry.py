from js import Response
import random

business = [
    "a coffee roastery", 
    "a pizza shop", 
    "an animal shelter", 
    "a street food vendor",
    "a bookstore",
    "a gym",
    "a clothing boutique",
    "a travel agency",
    "a music store",
    "a hardware store",
    "a gardening center",
    "a pet grooming service",
    "a car wash",
    "a bakery",
    "a barber shop",
    "a sushi restaurant",
    "a flower shop",
    "a photography studio",
    "a fitness studio",
    "a juice bar",
    "a language school",
    "a yoga studio",
    "a food truck",
    "a car rental service",
    "a tutoring center"
]

concepts = [
    "landing page", 
    "a nav menu", 
    "a chatbot", 
    "an order review screen",
    "a payment gateway",
    "a product catalog",
    "a booking system",
    "a search functionality",
    "a user profile page",
    "a feedback form",
    "a newsletter subscription",
    "a calendar integration",
    "a review system",
    "a notification system",
    "a recommendation engine",
    "a contact form",
    "a blog section",
    "a social media integration",
    "an admin dashboard",
    "a rating system",
    "a map integration",
    "a shopping cart",
    "a wishlist feature",
    "a video gallery",
    "a quiz functionality"
]


async def on_fetch(request, env):
    
               
    return Response.new("{ \"business\": \"" + random.choice(business)+ "\", \"concept\": \""+ random.choice(concepts)+ "\" }")
