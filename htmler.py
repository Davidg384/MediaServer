import os

f = open("index.html", "w+")
f.write("""
<html>
<header>
    <title>Index</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../../../default.css">
    <div class="name">
      BereaFlix
    </div>
    <nav>
      <ul>
        <li><a href="../../../index.html">Home</a></li>
        <li><a href="../../../anime/anime.html">Anime</a></li>
        <li><a href="../../../movies/movies.html">Movies</a></li>
        <li><a href="../../tv.html">TV Shows</a></li>
      </ul>
    </nav>
</header>
<br><br><br><br>
<a href="../index.html" style="color:black; margin-left:10px;">Back</a>
<br>
<body>
        """)
i = 1
for file in sorted(os.listdir()):
    if ".mp4" in file:
        f.write("""        
        <div class="thumb">
        <a href="{0}"><img src="video.png"></a>
        <div class="nametag">{1}</div>
        </div>
        """.format(file, str(i)))
        if i % 4 == 0:
            f.write("<br>\n")
        i += 1
f.write("""
    </body>
    </html>
        """)
f.close()
