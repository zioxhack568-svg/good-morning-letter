from flask import Flask

app = Flask(__name__)

@app.route('/')
def good_morning():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>💌 A Letter for You</title>
      <style>
        body {
          margin: 0;
          padding: 0;
          height: 100vh;
          background: linear-gradient(135deg, #ffe6f0, #ffd1dc);
          font-family: 'Comic Sans MS', cursive, sans-serif;
          display: flex;
          justify-content: center;
          align-items: center;
          overflow: hidden;
          flex-direction: column;
        }

        .envelope-wrapper {
          position: relative;
          width: 280px;
          height: 180px;
          background: #fff0f6;
          border: 3px solid #ff99cc;
          border-radius: 12px;
          box-shadow: 0 15px 30px rgba(255, 105, 180, 0.2);
          transition: all 0.3s ease-in-out;
        }

        .envelope-wrapper::before {
          content: '';
          position: absolute;
          width: 100%;
          height: 100%;
          background: #ffc0cb;
          clip-path: polygon(0 0, 50% 50%, 100% 0);
          top: 0;
          left: 0;
          border-top-left-radius: 12px;
          border-top-right-radius: 12px;
        }

        .heart-sticker {
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          font-size: 2.5em;
          cursor: pointer;
          z-index: 2;
          transition: transform 0.2s ease;
        }

        .heart-sticker:hover {
          transform: translate(-50%, -50%) scale(1.1);
        }

        #instruction {
          margin-top: 20px;
          font-size: 1.1em;
          color: #d63384;
          font-family: 'Comic Sans MS', cursive, sans-serif;
          animation: fadeIn 2s ease;
          text-align: center;
        }

        .card {
          background: #fff0f6;
          padding: 40px 30px;
          border-radius: 24px;
          box-shadow: 0 15px 40px rgba(255, 105, 180, 0.2);
          max-width: 420px;
          text-align: center;
          border: 2px dashed #ffc0cb;
          display: none;
          animation: fadeIn 1.2s ease forwards;
          z-index: 3;
          position: relative;
        }

        .card h1 {
          font-size: 2.2em;
          color: #ff69b4;
          margin-bottom: 15px;
        }

        .card p {
          font-size: 1.1em;
          color: #d63384;
          line-height: 1.6em;
        }

        .heart {
          position: absolute;
          width: 16px;
          height: 16px;
          background: #ff69b4;
          transform: rotate(45deg);
          animation: float 7s infinite ease-in;
          opacity: 0.7;
          z-index: 0;
        }

        .heart::before,
        .heart::after {
          content: '';
          position: absolute;
          width: 16px;
          height: 16px;
          background: #ff69b4;
          border-radius: 50%;
        }

        .heart::before {
          top: -8px;
          left: 0;
        }

        .heart::after {
          top: 0;
          left: -8px;
        }

        @keyframes float {
          0% {
            transform: translateY(0) rotate(45deg);
            opacity: 0;
          }
          50% {
            opacity: 1;
          }
          100% {
            transform: translateY(-800px) rotate(45deg);
            opacity: 0;
          }
        }

        @keyframes fadeIn {
          0% { opacity: 0; transform: scale(0.95); }
          100% { opacity: 1; transform: scale(1); }
        }

        @media (max-width: 480px) {
          .envelope-wrapper {
            width: 220px;
            height: 140px;
          }

          .heart-sticker {
            font-size: 2em;
          }

          #instruction {
            font-size: 1em;
          }

          .card {
            padding: 30px 20px;
          }

          .card h1 {
            font-size: 1.8em;
          }

          .card p {
            font-size: 1em;
          }
        }
      </style>
    </head>
    <body>

      <div id="envelope" class="envelope-wrapper">
        <div class="heart-sticker" onclick="openLetter()">💖</div>
      </div>

      <p id="instruction">Tap the heart to open your morning letter 💖</p>

      <div id="card" class="card">
        <h1>🌞 Good Morning! 🌸</h1>
        <p>Sending you soft sunshine, warm hugs, and pink skies to start your day 💗🧸<br><br>
        You’re wonderful. Hope today brings you tiny joys and big smiles! ✨🌼</p>
      </div>

      <script>
        function openLetter() {
          document.getElementById("envelope").style.display = "none";
          document.getElementById("instruction").style.display = "none";
          document.getElementById("card").style.display = "block";

          for (let i = 0; i < 40; i++) {
            let heart = document.createElement('div');
            heart.className = 'heart';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDelay = Math.random() * 5 + 's';
            heart.style.width = heart.style.height = (Math.random() * 10 + 10) + 'px';
            document.body.appendChild(heart);
          }
        }
      </script>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
