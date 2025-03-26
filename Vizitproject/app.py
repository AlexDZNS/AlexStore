from flask import Flask, render_template

app = Flask(__name__)

# Информация о компании/специалисте
company_name = "Alex Store"
company_description = "Предлагаю свои услуги в сфере IT"
company_telegram = "https://t.me/AlexDZNS"  # Замените на ваш username
company_email = "alexstore@gmail.com"

# Список товаров (пример)
products = [
    {
        'id': 1,
        'name': 'Разработка сайта',
        'description': 'Сделаю сайт под ваш товар или что-то другое на ваш выбор',
        'price': "4999 - 19999",
        'image': 'static/images/сайт.webp' # замените на ваш путь
    },
    {
        'id': 2,
        'name': 'Разработка Telegram Бота',
        'description': 'Сделаю вашего личного бота в Telegram',
        'price': "от 1000",
        'image': 'static/images/бот.webp' # замените на ваш путь
    }
]


@app.route("/")
def index():
    """Главная страница."""
    return render_template("index.html",
                           company_name=company_name,
                           company_description=company_description)

@app.route("/contacts")
def contacts():
    """Страница контактов."""
    return render_template("contacts.html",
                           company_name=company_name,
                           company_telegram=company_telegram,
                           company_email=company_email)

@app.route("/products")
def products_page():
    """Страница с товарами."""
    return render_template("products.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)


