# 🛒 Electronic Retail

**Electronic Retail** — это API-платформа для управления иерархической сетью по продаже электроники (заводы, розничные сети, ИП).

---

## 🚀 Возможности

- Иерархия: завод → розничная сеть → ИП
- Контакты, задолженность, поставщик
- Фильтрация по стране и городу
- CRUD API с авторизацией
- Админка Django
- Доступ к API — только активным пользователям
- Полностью docker-изолированный стек

---

## ⚙️ Технологии

- Python 3.12
- Django 
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- Nginx

---

## 📁 Установка и запуск (локально, через Docker)

### 1. Клонируй проект:

```bash
git clone https://github.com/your_username/electronic_retail.git
cd electronic_retail
```

### 2. Создай `.env`:

```bash
cp .env_exanple .env
```

Заполни нужные значения (пароли, ключи и т.д.).

### 3. Собери и запусти контейнеры:

```bash
docker-compose up --build
```

### 4. Открой в браузере:

- Приложение: [http://localhost](http://localhost)
- Админка: [http://localhost/admin/](http://localhost/admin/)

## 📜 Aleksospishev
