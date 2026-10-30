
# 📚 Book Store (Django Web Application)

[ 🇬🇧 English ](#english) | [ 🇦🇲 Հայերեն ](#armenian)


<span id="english"></span>
## 🇬🇧 English

> An interactive web application built with Python and Django framework, managing a comprehensive book catalog. This project demonstrates advanced database modeling using Django ORM (Object-Relational Mapping), model relationships, dynamic routing, and an extensively customized Django Admin interface.

### 📌 About the Project

The **Book Store** project focuses on complex database schema design. It allows tracking books, authors, publisher addresses, and countries using Django’s core relationship fields (`ForeignKey`, `ManyToManyField`, `OneToOneField`) alongside dynamic, SEO-friendly routing with slugs.

### ✨ Features

- **Advanced Django Models:** Well-structured relational schema connecting Books, Authors, Addresses, and Countries.
- **SEO-Friendly URLs (Slugs):** Automatic generation of readable slugs for book detail pages (e.g., `/books/harry-potter-1`).
- **Django Admin Customization:** Filter configurations, search fields, prepopulated slug fields, and list displays.
- **ORM Aggregation & Querying:** Real-time database metrics (average ratings, total count of books).
- **Template Inheritance:** Modular and clean HTML structure using Django Template Language (DTL) and CSS styling.

### 🛠 Tech Stack

- **Backend:** Python 3.x, Django
- **Database:** SQLite3 (Django ORM)
- **Frontend:** HTML5, CSS3, Django Templates

### 🚀 Getting Started

1. **Clone the repository:** 
   git clone https://github.com/MarkosyanShooshan/book-store.git
   cd book-store
Create and activate virtual environment:
Windows:
python -m venv venv
venv\Scripts\activate
macOS / Linux:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Apply database migrations:
python manage.py migrate
Create a superuser (optional, for Admin Panel):
python manage.py createsuperuser
Run development server:
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.



<span id="armenian"></span>
## 🇦🇲 Հայերեն

> Գրքերի կառավարման ինտերակտիվ վեբ-հավելված՝ ստեղծված Python-ով և Django ֆրեյմվորքով։ Նախագիծը ցուցադրում է Django ORM-ի (Object-Relational Mapping), տվյալների բազայի ռելյացիաների (relationships) և Django Admin Panel-ի հզոր հնարավորությունները։

---

## 📌 Նախագծի մասին (About)

**Book Store** նախագիծը նվիրված է տվյալների բազաների խորացված մոդելավորմանը։ Հավելվածը թույլ է տալիս կառավարել գրքերի կատալոգը, դրանց հեղինակներին, հրատարակչություններին և երկրներին՝ օգտագործելով Django-ի բարդ կապերը (One-to-One, One-to-Many, Many-to-Many) և դինամիկ երթուղավորումը (Slugs):

---

## ✨ Հիմնական հնարավորությունները (Features)

- **Խորացված Django Models** — Գրքերի, հեղինակների և հասցեների փոխկապակցված ռելյացիաներ (`ForeignKey`, `ManyToManyField`, `OneToOneField`):
- **SEO-Friendly URLs (Slugs)** — Գրքերի մանրամասն էջերի հասցեների ավտոմատ ստեղծում վերնագրի հիման վրա (օր.՝ `/books/harry-potter-1`):
- **Հզոր Django Admin Customization** — Ադմինիստրատիվ վահանակի ճկուն կարգավորում (ֆիլտրեր, որոնման դաշտեր, ավտոմատ լրացվող slug-եր, աղյուսակային ցուցադրում):
- **ORM Aggregation & Querying** — Տվյալների բազայի վիճակագրական հաշվարկներ (միջին գնահատականներ, գրքերի ընդհանուր քանակ և այլն):
- **Մոդուլային Շաբլոններ (Templates)** — Կոկիկ դիզայն՝ բազային շաբլոնների և ստատիկ CSS ֆայլերի կիրառմամբ։

---

## 🛠 Օգտագործված տեխնոլոգիաները (Tech Stack)

- **Backend:** Python 3.x, Django
- **Database:** SQLite3 (Django ORM)
- **Frontend:** HTML5, CSS3, Django Templates

---

## 📂 Կառուցվածքը (Structure)

```text
book_store/
│
├── book_outlet/            # Հիմնական հավելվածը (Models, Views, Admin)
│   ├── models.py           # Տվյալների մոդելները (Book, Author, Address, Country)
│   ├── admin.py            # Ադմին պանելի կարգավորումները
│   ├── views.py            # Լոգիկան (գրքերի ցանկ, մանրամասն դիտում)
│   └── urls.py
│
├── templates/              # HTML շաբլոններ
├── static/                 # CSS ոճեր
├── manage.py
├── requirements.txt
└── .gitignore


🚀 Տեղադրում և Գործարկում (Setup Guide)
1. Կլոնավորել նախագիծը

git clone https://github.com/MarkosyanShooshan/book-store.git
cd book-store

2. Ստեղծել վիրտուալ միջավայր

python -m venv venv
Ակտիվացնել.
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

3. Տեղադրել անհրաժեշտ գրադարանները

pip install -r requirements.txt

4. Կատարել միգրացիաները

python manage.py migrate

5. Ստեղծել ադմինիստրատոր (ըստ ցանկության)

python manage.py createsuperuser

6. Միացնել սերվերը

python manage.py runserver
Բացեք բրաուզերում՝
👉 http://127.0.0.1:8000/ (կամ ադմին պանելը՝ /admin)


👤 Հեղինակ (Author)
Շուշան Մարկոսյան — https://github.com/MarkosyanShooshan/


