let selectedGender = "";
let selectedSeason = "";

// Function to add messages
function addMessage(content, sender) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', sender);
    messageDiv.innerHTML = content.replace(/\n/g, '<br>');
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Function to generate outfit ideas
function getOutfitIdeas(season, gender) {
    const outfits = {
        men: {
            summer: [
                "☀️ **Casual Beach Look:**\n1️⃣ White T-shirt\n2️⃣ Denim Shorts\n3️⃣ Flip-Flops\n4️⃣ Beaded Bracelet\n5️⃣ Aviator Sunglasses",
                "👔 **Office Casual:**\n1️⃣ Light Blue Shirt\n2️⃣ Chinos\n3️⃣ Loafers\n4️⃣ Leather Watch\n5️⃣ Wayfarer Sunglasses"
            ],
            winter: [
                "🧥 **Layered Look:**\n1️⃣ Wool Coat\n2️⃣ Black Sweater & Jeans\n3️⃣ Leather Boots\n4️⃣ Scarf\n5️⃣ Round Metal Sunglasses",
                "❄️ **Casual Winter:**\n1️⃣ Hoodie\n2️⃣ Joggers\n3️⃣ Sneakers\n4️⃣ Beanie\n5️⃣ Tinted Sunglasses"
            ]
        },
        women: {
            summer: [
                "🌸 **Brunch Outfit:**\n1️⃣ Floral Crop Top\n2️⃣ High-Waist Shorts\n3️⃣ Sandals\n4️⃣ Minimalist Necklace\n5️⃣ Oversized Sunglasses",
                "💃 **Casual Chic:**\n1️⃣ Sleeveless Blouse\n2️⃣ A-line Skirt\n3️⃣ Ballet Flats\n4️⃣ Pearl Earrings\n5️⃣ Cat-Eye Sunglasses"
            ],
            winter: [
                "🧣 **Cozy Winter:**\n1️⃣ Knitted Sweater\n2️⃣ Fleece Leggings\n3️⃣ Ankle Boots\n4️⃣ Woolen Scarf\n5️⃣ Tortoiseshell Sunglasses",
                "❄️ **Winter Formal:**\n1️⃣ Long Wool Coat\n2️⃣ Turtleneck & Dress Pants\n3️⃣ Knee-High Boots\n4️⃣ Leather Gloves\n5️⃣ Round Sunglasses"
            ]
        }
    };
    return outfits[gender][season].join("\n\n");
}

// Function to get trending shirts
function getShirtTrends() {
    return "👕 **Trending Shirts in 2025:**\n\n1️⃣ **Oversized Graphic Tee** – Bold prints and streetwear vibes.\n\n2️⃣ **Minimalist Linen Shirt** – Clean, breathable, and stylish for all occasions.";
}

// Function to get outfit ideas based on skin tone
function getSkinToneOutfits(tone) {
    const outfits = {
        dark: [
            "🔥 **Dark Skin Tone Outfit Idea 1:**\n1️⃣ Earthy Brown Blazer\n2️⃣ Cream Turtleneck\n3️⃣ Dark Jeans\n4️⃣ Chelsea Boots\n5️⃣ Gold Accessories",
            "🌟 **Dark Skin Tone Outfit Idea 2:**\n1️⃣ Navy Blue Suit\n2️⃣ White Shirt\n3️⃣ Loafers\n4️⃣ Black Leather Belt\n5️⃣ Classic Sunglasses"
        ],
        white: [
            "🌞 **White Skin Tone Outfit Idea 1:**\n1️⃣ Pastel Pink Polo Shirt\n2️⃣ White Chinos\n3️⃣ Loafers\n4️⃣ Silver Watch\n5️⃣ Aviator Sunglasses",
            "🎀 **White Skin Tone Outfit Idea 2:**\n1️⃣ Dark Green Sweater\n2️⃣ Beige Trousers\n3️⃣ Sneakers\n4️⃣ Black Leather Watch\n5️⃣ Classic Wayfarers"
        ]
    };
    return outfits[tone].join("\n\n");
}

// Function to process user input
function processUserInput() {
    const userInput = document.getElementById('userInput').value.trim().toLowerCase();
    document.getElementById('userInput').value = '';

    addMessage(`You: ${userInput}`, 'user-message');

    let response = '';

    if (userInput.includes('hi') || userInput.includes('hello')) {
        response = "Hello! I'm your Fashion Assistant. Would you like outfit ideas for men or women?";
    } else if (userInput.includes('men')) {
        selectedGender = "men";
        response = "Would you like summer or winter fashion ideas for men?";
    } else if (userInput.includes('women')) {
        selectedGender = "women";
        response = "Would you like summer or winter fashion ideas for women?";
    } else if ((userInput.includes('summer') || userInput.includes('winter')) && selectedGender) {
        selectedSeason = userInput.includes('summer') ? "summer" : "winter";
        response = getOutfitIdeas(selectedSeason, selectedGender);
    } else if (userInput.includes('shirt')) {
        response = getShirtTrends();
    } else if (userInput.includes('dark')) {
        response = getSkinToneOutfits("dark");
    } else if (userInput.includes('white')) {
        response = getSkinToneOutfits("white");
    } else {
        response = "I didn’t understand that. You can ask for 'Men' or 'Women' fashion ideas, 'Summer' or 'Winter' outfits, or type 'shirt', 'dark skin', or 'white skin'.";
    }

    addMessage(response, 'assistant-message');
}

// Initialize greeting message on page load
window.onload = () => {
    addMessage("Hello! I'm your Fashion Assistant. Would you like outfit ideas for men or women?", 'assistant-message');
}

// Event listener for send button
document.getElementById('sendMessage').addEventListener('click', processUserInput);

// Event listener for enter key
document.getElementById('userInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        processUserInput();
    }
});
