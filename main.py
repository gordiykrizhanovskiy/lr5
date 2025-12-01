import functions_framework
from flask import request, make_response
import random

@functions_framework.http
def random_roll(request):
    a = int(request.args.get("min", 1))
    b = int(request.args.get("max", 6))
    count = int(request.args.get("count", 1))

    rolls = [random.randint(a, b) for _ in range(count)]
    result = rolls[0] if count == 1 else rolls
    total = sum(rolls)

    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <title>🎲 Random Roll</title>
        <style>
          body {{
            background: radial-gradient(circle at center, #1e1e2f, #0b0b12);
            color: #fff;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            margin-top: 100px;
          }}
          .box {{
            display: inline-block;
            background: #282a36;
            padding: 30px 50px;
            border-radius: 20px;
            box-shadow: 0 0 15px rgba(255,255,255,0.2);
          }}
          h1 {{
            font-size: 60px;
            color: #50fa7b;
            margin: 0;
          }}
          h2 {{ color: #8be9fd; margin-bottom: 10px; }}
          p  {{ color: #f8f8f2; }}
        </style>
      </head>
      <body>
        <div class="box">
          <h2>🎲 Random Roll</h2>
          <h1>{result}</h1>
          <p>min = {a}, max = {b}, count = {count}</p>
          <p><b>Sum:</b> {total}</p>
        </div>
      </body>
    </html>
    """

    resp = make_response(html)
    resp.headers["Content-Type"] = "text/html"
    return resp
