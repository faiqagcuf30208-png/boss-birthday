
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Birthday Surprise for Boss",
    page_icon="🎁",
    layout="wide"
)

st.markdown("""
<style>
header, footer, #MainMenu {
    visibility: hidden;
}
.stApp {
    background: #080808;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

page = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #080808;
    color: #f5d78e;
    font-family: Georgia, serif;
    overflow-x: hidden;
}

.screen {
    display: none;
    min-height: 850px;
    width: 100%;
    padding: 35px 15px;
    text-align: center;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(ellipse at center, #241b0c 0%, #080808 70%);
}

.screen.active {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.gold {
    color: #f5d78e;
    text-shadow: 0 0 15px #d49b28;
}

h1 {
    font-size: clamp(35px, 7vw, 65px);
    letter-spacing: 5px;
    margin: 15px 0;
}

h2 {
    font-size: clamp(24px, 5vw, 38px);
}

p {
    color: #e9d8ad;
    font-size: 18px;
    line-height: 1.8;
}

button {
    background: linear-gradient(135deg, #f8df9c, #bd8727);
    color: #17100a;
    border: none;
    border-radius: 30px;
    padding: 15px 32px;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: 2px;
    cursor: pointer;
    margin: 20px 8px;
    box-shadow: 0 0 20px #c99b43;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 35px #f5d78e;
}

.small-text {
    color: #c9a85d;
    letter-spacing: 3px;
    font-size: 13px;
}

/* Stars */

.stars {
    position: absolute;
    width: 4px;
    height: 4px;
    background: #f8df9c;
    border-radius: 50%;
    box-shadow: 0 0 12px #f8df9c;
    animation: twinkle 2s infinite alternate;
}

@keyframes twinkle {
    from { opacity: 0.2; transform: scale(0.6); }
    to { opacity: 1; transform: scale(1.5); }
}

/* Gift */

.gift-area {
    margin: 40px auto;
    cursor: pointer;
    width: 180px;
    height: 180px;
    position: relative;
}

.gift {
    position: absolute;
    width: 150px;
    height: 115px;
    background: linear-gradient(135deg, #d6a23d, #80520f);
    left: 15px;
    bottom: 0;
    border-radius: 5px;
    box-shadow: 0 0 35px #c28a27;
}

.gift::before {
    content: "";
    position: absolute;
    width: 25px;
    height: 115px;
    left: 62px;
    background: #f9e0a0;
}

.gift::after {
    content: "";
    position: absolute;
    height: 20px;
    width: 150px;
    background: #f0ca76;
    left: 0;
    top: 45px;
}

.gift-lid {
    position: absolute;
    width: 170px;
    height: 35px;
    background: #e8bf65;
    left: 5px;
    top: 30px;
    border-radius: 5px;
    z-index: 2;
    transition: 0.8s;
}

.gift-bow {
    position: absolute;
    width: 40px;
    height: 30px;
    border: 9px solid #f9e6b3;
    border-radius: 50%;
    top: -18px;
    left: 65px;
    z-index: 3;
}

.gift.open .gift-lid {
    transform: translateY(-100px) rotate(-20deg);
}

.gift.open {
    animation: giftGlow 1s ease;
}

@keyframes giftGlow {
    50% { box-shadow: 0 0 70px #ffe5a0; }
}

/* Butterflies */

.butterfly {
    position: absolute;
    font-size: 28px;
    animation: fly 7s linear infinite;
    pointer-events: none;
}

@keyframes fly {
    0% { transform: translate(-100px, 100px) rotate(0); opacity: 0; }
    20% { opacity: 1; }
    100% { transform: translate(100vw, -150px) rotate(360deg); opacity: 0; }
}

/* Cake */

.cake {
    position: relative;
    width: 210px;
    height: 145px;
    margin: 45px auto 25px;
}

.cake-top {
    position: absolute;
    top: 0;
    left: 10px;
    width: 190px;
    height: 55px;
    border-radius: 50%;
    background: #f0c9a0;
    border: 5px solid #d6a24a;
    z-index: 2;
}

.cake-body {
    position: absolute;
    top: 25px;
    left: 10px;
    width: 190px;
    height: 100px;
    border-radius: 0 0 20px 20px;
    background: linear-gradient(#9b4d34, #55251c);
    border: 4px solid #d6a24a;
}

.cake-body::after {
    content: "★  ★  ★";
    position: absolute;
    top: 40px;
    width: 100%;
    color: #f5d78e;
    font-size: 22px;
    text-align: center;
}

.candle {
    position: absolute;
    width: 9px;
    height: 55px;
    background: #fff0bd;
    top: -48px;
    z-index: 3;
}

.candle:nth-child(1) { left: 55px; }
.candle:nth-child(2) { left: 100px; }
.candle:nth-child(3) { left: 145px; }

.flame {
    position: absolute;
    width: 16px;
    height: 23px;
    background: orange;
    border-radius: 50% 50% 50% 0;
    transform: rotate(-45deg);
    top: -25px;
    left: -4px;
    box-shadow: 0 0 20px orange;
    animation: flicker 0.5s infinite alternate;
}

@keyframes flicker {
    from { transform: rotate(-45deg) scale(0.8); }
    to { transform: rotate(-45deg) scale(1.1); }
}

.flame.off {
    display: none;
}

/* Wishes */

.wish-line {
    opacity: 0;
    transform: translateY(15px);
    animation: appear 1s forwards;
    margin: 12px 0;
    font-size: clamp(17px, 3vw, 23px);
}

@keyframes appear {
    to { opacity: 1; transform: translateY(0); }
}

/* Roses and petals */

.rose {
    font-size: 65px;
    display: inline-block;
    animation: bloom 2s ease-in-out infinite alternate;
    filter: drop-shadow(0 0 15px #b88a39);
}

@keyframes bloom {
    from { transform: scale(0.7) rotate(-8deg); }
    to { transform: scale(1.15) rotate(8deg); }
}

.petal {
    position: absolute;
    top: -30px;
    font-size: 22px;
    animation: fall 7s linear forwards;
    pointer-events: none;
}

@keyframes fall {
    to {
        transform: translateY(950px) rotate(700deg);
        opacity: 0;
    }
}

/* Fireworks */

#fireworks {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}

.final-content {
    position: relative;
    z-index: 2;
}
</style>
</head>

<body>

<!-- SCREEN 1 -->
<section class="screen active" id="one">
    <div class="small-text">A SPECIAL SURPRISE IS WAITING FOR YOU</div>

    <h2 class="gold">Dear Boss...</h2>

    <p>
        Today is not an ordinary day.<br>
        Something special has been prepared just for you.
    </p>

    <div class="gift-area" id="gift">
        <div class="gift">
            <div class="gift-lid">
                <div class="gift-bow"></div>
            </div>
        </div>
    </div>

    <p class="small-text">TAP THE GIFT TO UNLOCK YOUR SURPRISE</p>

    <button type="button" id="openGiftBtn">
        OPEN YOUR GIFT ✨
    </button>
</section>

<!-- SCREEN 2 -->
<section class="screen" id="two">
    <div class="small-text">A MOMENT MADE JUST FOR YOU</div>

    <h1 class="gold">HAPPY BIRTHDAY</h1>
    <h1 style="color:#fff0c5;">BOSS 👑</h1>

    <p>
        A wonderful person deserves a wonderful celebration.
    </p>

    <div style="font-size:65px; margin:20px;">🎊 🎉 ✨</div>

    <button type="button" data-action="cake">
        CONTINUE TO YOUR CAKE 🎂
    </button>
</section>

<!-- SCREEN 3 -->
<section class="screen" id="three">
    <div class="small-text">MAKE A WISH</div>

    <h2 class="gold">A CAKE JUST FOR YOU!</h2>

    <div class="cake">
        <div class="cake-top"></div>
        <div class="cake-body"></div>

        <div class="candle">
            <div class="flame"></div>
        </div>

        <div class="candle">
            <div class="flame"></div>
        </div>

        <div class="candle">
            <div class="flame"></div>
        </div>
    </div>

    <p>Close your eyes, make a wish and blow the candles!</p>

    <button type="button" id="blowBtn">
        🌬️ BLOW THE CANDLES
    </button>

    <button type="button" id="wishContinue" style="display:none;">
        READ YOUR BIRTHDAY WISHES 💌
    </button>
</section>

<!-- SCREEN 4 -->
<section class="screen" id="four">
    <div class="small-text">WORDS FROM THE HEART</div>

    <h2 class="gold">A FEW SPECIAL WORDS</h2>

    <div id="wishes"></div>

    <button type="button" data-action="final">
        ONE LAST SURPRISE 🌹
    </button>
</section>

<!-- SCREEN 5 -->
<section class="screen" id="five">
    <canvas id="fireworks"></canvas>

    <div class="final-content">
        <div class="small-text">WITH RESPECT & BEST WISHES</div>

        <h1 class="gold">HAPPY BIRTHDAY!</h1>

        <div id="roses">
            <span class="rose">🌹</span>
            <span class="rose">🌹</span>
            <span class="rose">🌹</span>
        </div>

        <h2 style="color:#fff0c5;">Dear Boss 👑</h2>

        <p>
            May your life always shine with happiness,<br>
            success, good health and endless blessings.
        </p>

        <p class="gold">
            Thank you for your guidance and support.<br>
            Wishing you a beautiful year ahead!
        </p>

        <div style="font-size:35px;">✨ 🎂 🎉 ✨</div>

        <button type="button" id="replayBtn">
            WATCH AGAIN ↻
        </button>
    </div>
</section>

<script>
/* Screen navigation */

function showScreen(id) {
    document.querySelectorAll(".screen").forEach(function(item) {
        item.classList.remove("active");
    });

    const next = document.getElementById(id);

    if (next) {
        next.classList.add("active");
    }

    window.scrollTo(0, 0);
}

/* Gift opening */

function openGift() {
    const gift = document.getElementById("gift");

    if (gift) {
        gift.classList.add("open");
    }

    setTimeout(function() {
        showScreen("two");
        butterflies();
    }, 700);
}

/* Butterflies */

function butterflies() {
    for (let i = 0; i < 8; i++) {
        const butterfly = document.createElement("div");
        butterfly.className = "butterfly";
        butterfly.innerHTML = "🦋";
        butterfly.style.top = Math.random() * 80 + "%";
        butterfly.style.left = "-40px";
        butterfly.style.animationDelay = Math.random() * 3 + "s";

        document.getElementById("two").appendChild(butterfly);

        setTimeout(function() {
            butterfly.remove();
        }, 9000);
    }
}

/* Candles */

function blowCandles() {
    document.querySelectorAll(".flame").forEach(function(flame) {
        flame.classList.add("off");
    });

    document.getElementById("blowBtn").style.display = "none";
    document.getElementById("wishContinue").style.display = "inline-block";

    for (let i = 0; i < 15; i++) {
        const sparkle = document.createElement("div");
        sparkle.innerHTML = "✨";
        sparkle.style.position = "absolute";
        sparkle.style.left = Math.random() * 90 + "%";
        sparkle.style.top = Math.random() * 80 + "%";
        sparkle.style.fontSize = "25px";
        sparkle.style.pointerEvents = "none";

        document.getElementById("three").appendChild(sparkle);

        setTimeout(function() {
            sparkle.remove();
        }, 1800);
    }
}

/* Wishes appear one by one */

function showWishes() {
    const messages = [
        "May your day be filled with happiness and laughter.",
        "May success follow you in every step you take.",
        "May you always have reasons to smile.",
        "Thank you for being a wonderful leader and inspiration.",
        "May this new year bring you endless opportunities.",
        "Wishing you good health, peace and prosperity."
    ];

    const container = document.getElementById("wishes");
    container.innerHTML = "";

    messages.forEach(function(message, index) {
        const line = document.createElement("div");
        line.className = "wish-line";
        line.textContent = message;
        line.style.animationDelay = (index * 1.2) + "s";
        container.appendChild(line);
    });
}

/* Falling petals */

function petals() {
    const screen = document.getElementById("five");

    for (let i = 0; i < 35; i++) {
        const petal = document.createElement("div");
        petal.className = "petal";
        petal.innerHTML = Math.random() > 0.5 ? "🌸" : "🌹";
        petal.style.left = Math.random() * 100 + "%";
        petal.style.animationDelay = Math.random() * 6 + "s";
        petal.style.animationDuration = (5 + Math.random() * 5) + "s";

        screen.appendChild(petal);

        setTimeout(function() {
            petal.remove();
        }, 11000);
    }
}

/* Fireworks animation */

let fireworksAnimation = null;

function startFireworks() {
    const canvas = document.getElementById("fireworks");
    const ctx = canvas.getContext("2d");

    canvas.width = window.innerWidth;
    canvas.height = 850;

    if (fireworksAnimation) {
        cancelAnimationFrame(fireworksAnimation);
    }

    let particles = [];

    function burst() {
        const x = Math.random() * canvas.width;
        const y = Math.random() * (canvas.height * 0.65);
        const colors = ["#f5d78e", "#ffffff", "#e8b84c", "#ffcc66"];

        for (let i = 0; i < 35; i++) {
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 4 + 1;

            particles.push({
                x: x,
                y: y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                life: 70,
                color: colors[Math.floor(Math.random() * colors.length)]
            });
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        if (Math.random() < 0.055) {
            burst();
        }

        particles.forEach(function(particle) {
            particle.x += particle.vx;
            particle.y += particle.vy;
            particle.vy += 0.025;
            particle.life--;

            ctx.globalAlpha = Math.max(0, particle.life / 70);
            ctx.fillStyle = particle.color;
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, 2.5, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.globalAlpha = 1;

        particles = particles.filter(function(p) {
            return p.life > 0;
        });

        fireworksAnimation = requestAnimationFrame(animate);
    }

    animate();
}

/* Button and gift click events */

document.getElementById("gift").addEventListener("click", openGift);

document.getElementById("openGiftBtn").addEventListener("click", openGift);

document.querySelector('[data-action="cake"]').addEventListener("click", function() {
    showScreen("three");
});

document.getElementById("blowBtn").addEventListener("click", blowCandles);

document.getElementById("wishContinue").addEventListener("click", function() {
    showWishes();
    showScreen("four");
});

document.querySelector('[data-action="final"]').addEventListener("click", function() {
    showScreen("five");
    petals();
    startFireworks();
});

document.getElementById("replayBtn").addEventListener("click", function() {
    if (fireworksAnimation) {
        cancelAnimationFrame(fireworksAnimation);
        fireworksAnimation = null;
    }

    document.querySelectorAll(".butterfly, .petal").forEach(function(item) {
        item.remove();
    });

    document.getElementById("gift").classList.remove("open");

    document.querySelectorAll(".flame").forEach(function(flame) {
        flame.classList.remove("off");
    });

    document.getElementById("blowBtn").style.display = "inline-block";
    document.getElementById("wishContinue").style.display = "none";

    showScreen("one");
});

/* Background stars */

for (let i = 0; i < 45; i++) {
    const star = document.createElement("div");
    star.className = "stars";
    star.style.left = Math.random() * 100 + "%";
    star.style.top = Math.random() * 100 + "%";
    star.style.animationDelay = Math.random() * 3 + "s";
    document.body.appendChild(star);
}
</script>

</body>
</html>
"""

components.html(page, height=900, scrolling=True)
