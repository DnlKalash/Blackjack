# 🎰 Projekt Blackjack - Aplikacja Webowa Django

## 📋 Opis Projektu

**Blackjack Web Game** to kompleksowa aplikacja webowa stworzona w Django, która umożliwia grę w klasycznego Blackjacka. Projekt łączy w sobie zaawansowaną logikę gry, system autentyfikacji użytkowników oraz nowoczesny interfejs użytkownika.

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

### Funkcjonalności
- ✅ Pełna gra Blackjack
- ✅ System użytkowników
- ✅ JWT Authentication
- ✅ MongoDB Integration
- ✅ Session Management
- ✅ Responsive UI

---



### Konfiguracja
1. **MongoDB Atlas**: Połączenie z chmurową bazą danych
2. **SECRET_KEY**: Konfiguracja klucza bezpieczeństwa
3. **DEBUG**: Ustawienia deweloperskie/produkcyjne

### Uruchomienie
```bash
python manage.py runserver
```



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

# UWL Blackjack

  

```mermaid

graph TB

%% URL endpoints

URLs[URLs<br/>+url_main<br/>+url_blackjack]

%% Interface layer



Auth[Autentyfikacja JWT<br/>zarządzanie użytkownikami]

%% Main controller

WidokGlowny[Main.views<br/>+htmlshablon : HttpResponse<br/>+register : HttpResponse<br/>+login  : HttpResponse<br/>+logout : HttpResponse<br/>+jwt_required]

%% Blackjack logic

WidokBlackjack[Blackjack.views<br/>+widok_blackjack zadania : HttpResponse]

LogikaBlackjack[logic<br/>-Dict sesja<br/>-Dict gra<br/>+__init__ zadanie<br/>+save_game<br/>+create_new_game : Dict<br/>+first_bet balance <br/>+Hit<br/>+stand<br/>+draw_card : Tuple<br/>+update_scores who cards : int<br/>+calculate_score cards : int<br/>+determine_winner<br/>+reset]



%% Forms

FormularzAkcjiGry[GameActionFormy<br/>+ChoiceField akcja<br/>-Lista AKCJE]

FormularzUzytkownika[UserForm<br/>+CharField nazwa_uzytkownika<br/>+EmailField email<br/>+CharField haslo<br/>+waliduj_nazwa_uzytkownika : String<br/>+waliduj_email : String<br/>+waliduj_haslo : String<br/>+zapisz : Uzytkownik]

%% Configuration



%% User model

Uzytkownik[User<br/>-String nazwa_uzytkownika<br/>-String email<br/>-String haslo<br/>-Lista list ostatni_wynik<br/>+ustaw_haslo surowe_haslo<br/>+sprawdz_haslo surowe_haslo : bool<br/>+zapisz]

%% MongoDB integration

MongoDB[Model MongoDB<br/>przy użyciu MongoEngine]

%% Relationships



URLs --> WidokGlowny



Auth --> WidokGlowny

WidokGlowny --> FormularzUzytkownika

WidokGlowny --> Uzytkownik

WidokBlackjack --> LogikaBlackjack



WidokBlackjack --> FormularzAkcjiGry

FormularzAkcjiGry --> LogikaBlackjack







%% Labels for relationships

WidokGlowny -.->|kieruje do| URLs
URLs -.->|kieruje do| WidokBlackjack




FormularzUzytkownika -.->|tworzy| Uzytkownik

Uzytkownik -.->|zarządza| MongoDB