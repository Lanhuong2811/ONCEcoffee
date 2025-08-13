import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL
from helpers import vnd

# Configure application
app = Flask(__name__)
app.secret_key = os.urandom(24)

app.jinja_env.filters["vnd"] = vnd

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
db = SQL("sqlite:///oncecoffee.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Shop page
@app.route("/shop")
def shop():
    double_honey_beans = db.execute("SELECT * FROM beans WHERE collection = 'double'")
    origin_black_honey_beans = db.execute("SELECT * FROM beans WHERE collection = 'origin'")
    return render_template("shop.html", double_honey_beans=double_honey_beans, origin_black_honey_beans=origin_black_honey_beans)

# Register route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not email or not password or not confirmation:
            return render_template("apology.html", message="Missing credentials", code=400)
        if password != confirmation:
            return render_template("apology.html", message="Passwords must match", code=400)

        hash_pw = generate_password_hash(password)
        try:
            user_id = db.execute("INSERT INTO users (email, hash) VALUES (?, ?)", email, hash_pw)
        except:
            return render_template("apology.html", message="Email already registered", code=400)

        session["user_id"] = user_id
        return redirect("/")
    return render_template("register.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return render_template("apology.html", message="Missing credentials", code=400)

        rows = db.execute("SELECT * FROM users WHERE email = ?", email)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return render_template("apology.html", message="Invalid email or password", code=400)

        session["user_id"] = rows[0]["id"]
        return redirect("/")
    return render_template("login.html")

# Logout route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = request.form.get("product_id")
    name = request.form.get("name")
    price_raw = request.form.get("price")
    try:
        price = int(price_raw) if price_raw is not None else 0
    except ValueError:
        price = 0

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append({
        "product_id": product_id,
        "name": name,
        "price": price
    })

    return redirect("/cart")

@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total=total)

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    index = int(request.form.get("index"))
    if "cart" in session:
        session["cart"].pop(index)
    return redirect("/cart")

@app.route("/checkout", methods=["POST"])
def checkout():
    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")
    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)

    # Gửi đơn hàng ra console (sau có thể gửi email)
    print("----- ĐƠN HÀNG MỚI -----")
    print(f"Tên: {name}")
    print(f"SĐT: {phone}")
    print(f"Địa chỉ: {address}")
    print("Sản phẩm:")
    for item in cart_items:
        print(f"- {item['name']} ({item['price']} VND)")
    print(f"Tổng cộng: {total} VND")
    print("------------------------")

    # Xóa giỏ hàng
    session["cart"] = []

    # Hiển thị trang cảm ơn
    return render_template("thankyou.html", name=name)

