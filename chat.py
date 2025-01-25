from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('minecraft.html')

if __name__ == '__main__':
    app.run(debug=True)
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minecraft - Google Search Style</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f1f1f1;
        }
        .navbar {
            background-color: #f8f9fa;
            padding: 15px;
            text-align: center;
            font-size: 20px;
            border-bottom: 1px solid #e0e0e0;
        }
        .search-box {
            text-align: center;
            margin-top: 50px;
        }
        .search-box input[type="text"] {
            width: 60%;
            padding: 12px;
            font-size: 18px;
            border: 1px solid #d9d9d9;
            border-radius: 24px;
            outline: none;
        }
        .search-box input[type="submit"] {
            padding: 12px 24px;
            font-size: 18px;
            border: none;
            background-color: #4285f4;
            color: white;
            border-radius: 24px;
            cursor: pointer;
        }
        .search-box input[type="submit"]:hover {
            background-color: #357ae8;
        }
        .content {
            max-width: 1000px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
        }
    </style>
</head>
<body>

    <div class="navbar">
        <b>Google - Minecraft</b>
    </div>

    <div class="search-box">
        <form action="#" method="GET">
            <input type="text" placeholder="Search Minecraft..." name="q">
            <input type="submit" value="Search">
        </form>
    </div>

    <div class="content">
        <h1>Minecraft</h1>
        <p>
            Minecraft is a sandbox video game developed by Mojang. The game was created by Markus "Notch" Persson in the Java programming language. 
            Following several early private testing versions, it was first made public in May 2009 before fully releasing in November 2011, with Jens Bergensten then taking over development. 
            Minecraft has since been ported to several other platforms and is the best-selling video game of all time, with over 200 million copies sold across all platforms.
        </p>
        <p>
            In Minecraft, players explore a blocky, procedurally generated 3D world, discovering and extracting raw materials, crafting tools and items, and building structures or earthworks. 
            Depending on the game mode, players can also fight computer-controlled "mobs", as well as cooperate with or compete against other players in the same world. 
        </p>
    </div>

</body>
</html>


