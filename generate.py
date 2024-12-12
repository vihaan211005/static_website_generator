import pandas as pd

index_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Kanchan Studio</title>
</head>
<body>
    <header>
        <h1>Kanchan Studio</h1>
    </header>
    <div class="product-grid">
"""

def index_mid(name, price):
	string = """        <div class=\"product\">
            <a href=\""""+name+""".html\"> <img src=\""""+name+""".jpg\" alt=\""""+name+"""\"></a>
            <h3>"""+name+"""</h3>
            <p class="price">₹"""+price+"""</p>
            <a href=https://api.whatsapp.com/send?phone=919811928787&text=Hello%2C%20I%20would%20like%20to%20order%20"""+name.replace(" ", "%20")+"""><button>BUY</button></a>
        </div>
"""
	return string

index_end = """    </div>
</body>
</html>
"""

def description(name, description): return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>"""+name+"""</title>
</head>
<body>
    <div class="description-page">
        <img src=\""""+name+""".jpg\" alt=\""""+name+"""\" class="product-image">
        <h1>"""+name+"""</h1>
        <p class="product-description">"""+description+"""</p>
        <button onclick="window.location.href='index.html'" class="back-button">Back to Products</button>
    </div>
</body>
</html>
"""

df = pd.read_csv('products.csv')
for i in range(df.shape[0]):
	index_start+=index_mid(df["names"][i], str(df["price"][i]))
	describe=(description(df["names"][i], df["description"][i]))
	with open(df["names"][i]+".html", "w") as file:
    		file.write(describe)

index_start+=index_end
print(index_start)

with open("index.html", "w") as file:
	file.write(index_start)
