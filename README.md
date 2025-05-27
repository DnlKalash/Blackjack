# 🎰 Projekt Blackjack - Aplikacja Webowa Django

## 📋 Opis Projektu

**Blackjack Web Game** to kompleksowa aplikacja webowa stworzona w Django, która umożliwia grę w klasycznego Blackjacka online. Projekt łączy w sobie zaawansowaną logikę gry, system autentyfikacji użytkowników oraz nowoczesny interfejs użytkownika.

---

## 🏗️ Architektura Projektu

### Struktura Aplikacji
```
myproject/
├── main/           # Główna aplikacja - autentyfikacja i strona główna
├── blackjack/      # Aplikacja gry Blackjack
└── myproject/      # Konfiguracja projektu Django
```

### Technologie Wykorzystane
- **Backend**: Django 5.2+
- **Baza Danych**: MongoDB (MongoEngine)
- **Autentyfikacja**: JWT (JSON Web Tokens)
- **Frontend**: Standardowe szablony HTML
- **Hosting Bazy**: MongoDB Atlas

---

## 🎮 Funkcjonalności Gry

### Główne Mechanizmy Blackjacka
- **Kompletna logika gry**: Hit, Stand, obsługa asów (1/11)
- **System zakładów**: Dynamiczne zarządzanie saldem gracza
- **Automatyczny dealer**: AI dealer zgodny z zasadami kasyna
- **Sesyjne zapisywanie**: Stan gry zachowywany w sesji

### Algorytm Gry
- Tasowanie kart z 4 kolorami (♠, ♥, ♦, ♣)
- Automatyczne obliczanie wyniku z obsługą asów
- Logika wygrywania: 1.5x stawka za wygraną
- Reset gry z zachowaniem salda

---

## 👤 System Użytkowników

### Rejestracja i Logowanie
- **Bezpieczna rejestracja**: Walidacja username, email, hasła
- **JWT Authentication**: Tokeny z 24-godzinną ważnością
- **Haszowanie haseł**: Django's make_password/check_password
- **Walidacja formularzy**: Sprawdzanie unikalności danych

### Zarządzanie Sesjami
- **HttpOnly Cookies**: Bezpieczne przechowywanie tokenów JWT
- **Automatyczne wylogowanie**: Po wygaśnięciu tokenu
- **Persistent Sessions**: Zachowanie stanu gry między sesjami

---

## 🎨 Interfejs Użytkownika

### Responsywny Design
- **Motyw kasyna**: Zielone tło, złote akcenty (#ffcc00)
- **Intuicyjny interfejs**: Czytelne przyciski akcji
- **Dynamiczne updates**: Aktualizacja stanu gry w czasie rzeczywistym

### Strony Aplikacji
- **Strona główna**: Powitanie i nawigacja
- **Rejestracja/Logowanie**: Formularze z walidacją
- **Gra Blackjack**: Główny interfejs gry

---

## 🔧 Implementacja Techniczna

### Model Danych (MongoDB)
```python
class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    last_result = ListField(FloatField(), default=[])
```

### Logika Gry (blackjack/logic.py)
- **BlackjackLogic**: Główna klasa zarządzająca grą
- **Sesyjne przechowywanie**: Django sessions
- **Algorytmy**: Tasowanie, obliczanie wyniku, AI dealera

### Routing URL
```python
# Główne ścieżki
'/' - Strona główna
'/register' - Rejestracja
'/login' - Logowanie
'/game/' - Gra Blackjack
```

---

## 🛡️ Bezpieczeństwo

### Zabezpieczenia Implemented
- **CSRF Protection**: Django CSRF middleware
- **JWT Tokens**: Bezpieczna autentyfikacja
- **Password Hashing**: Django's built-in hashers
- **Input Validation**: Walidacja wszystkich formularzy
- **HttpOnly Cookies**: Ochrona przed XSS

### Walidacja Danych
- **Username**: Unikalność, długość
- **Email**: Format, unikalność
- **Password**: Minimum 8 znaków
- **Bet Amount**: Walidacja liczbowa, limity

---

## 📊 Statystyki Projektu

### Pliki Kodu
- **Python Files**: 12 plików
- **HTML Templates**: 4 szablony
- **Linie kodu**: ~500+ linii
- **Aplikacje**: 2 (main, blackjack)

### Funkcjonalności
- ✅ Pełna gra Blackjack
- ✅ System użytkowników
- ✅ JWT Authentication
- ✅ MongoDB Integration
- ✅ Session Management
- ✅ Responsive UI

---

## 🚀 Deployment i Uruchomienie

### Wymagania
```bash
pip install django mongoengine pyjwt djongo
```

### Konfiguracja
1. **MongoDB Atlas**: Połączenie z chmurową bazą danych
2. **SECRET_KEY**: Konfiguracja klucza bezpieczeństwa
3. **DEBUG**: Ustawienia deweloperskie/produkcyjne

### Uruchomienie
```bash
python manage.py runserver
```

---

## 📈 Możliwości Rozwoju

### Planowane Funkcjonalności
- **Multiplayer**: Gra wieloosobowa
- **Tournaments**: System turniejów
- **Statistics**: Szczegółowe statystyki gracza
- **Mobile App**: Aplikacja mobilna
- **Live Chat**: Czat między graczami

### Optymalizacje
- **Caching**: Redis dla lepszej wydajności
- **API**: REST API dla aplikacji mobilnej
- **Testing**: Unit tests i integration tests
- **CI/CD**: Automatyczne wdrażanie

---

## 👨‍💻 Informacje o Projekcie

**Status**: Projekt dla uczelni  
**Technologie**: Django, MongoDB, JWT, HTML/CSS  
**Architektura**: MVC (Model-View-Controller)  
**Baza danych**: NoSQL (MongoDB)  

**Projekt demonstruje**:
- Zaawansowane wykorzystanie Django
- Integrację z MongoDB
- Implementację JWT authentication
- Logika gry w blackjacka
- Responsive web design

---

