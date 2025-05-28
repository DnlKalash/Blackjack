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
    URLs[URLe<br/>+lista_wzorce_url_glowne<br/>+lista_wzorce_url_blackjack]
    
    %% Interface layer
    Interface[Interfejs gry<br/>obsługuje akcje gracza]
    Auth[Autentyfikacja JWT<br/>zarządzanie użytkownikami]
    
    %% Main controller
    WidokGlowny[WidokGlowny<br/>+html_szablon zadania : HttpResponse<br/>+rejestracja zadania : HttpResponse<br/>+logowanie zadania : HttpResponse<br/>+wylogowanie zadania : HttpResponse<br/>+wymagane_jwt funkcja_widoku]
    
    %% Blackjack logic
    WidokBlackjack[WidokBlackjack<br/>+widok_blackjack zadania : HttpResponse]
    
    LogikaBlackjack[LogikaBlackjack<br/>-Dict sesja<br/>-Dict gra<br/>+__init__ zadanie<br/>+zapisz_gre<br/>+stworz_nowa_gre saldo : Dict<br/>+pierwszy_zaklad kwota<br/>+dobierz<br/>+pas<br/>+dobierz_karte : Tuple<br/>+aktualizuj_punkty kto, karty : int<br/>+oblicz_punkty karty : int<br/>+ocenij_zwyciezce<br/>+restart]
    
    GlownaLogika[Główna logika gry<br/>zarządca stanu gry + sesji]
    
    %% Forms
    FormularzAkcjiGry[FormularzAkcjiGry<br/>+ChoiceField akcja<br/>-Lista AKCJE]
    
    FormularzUzytkownika[FormularzUzytkownika<br/>+CharField nazwa_uzytkownika<br/>+EmailField email<br/>+CharField haslo<br/>+waliduj_nazwa_uzytkownika : String<br/>+waliduj_email : String<br/>+waliduj_haslo : String<br/>+zapisz : Uzytkownik]
    
    %% Configuration
    Konfiguracja[Konfiguracja<br/>+String SECRET_KEY<br/>+Boolean DEBUG<br/>+Lista INSTALLED_APPS<br/>+Lista MIDDLEWARE<br/>+Dict DATABASES<br/>+String BLACKJACK_SESSION_ID]
    
    %% User model
    Uzytkownik[Uzytkownik<br/>-String nazwa_uzytkownika<br/>-String email<br/>-String haslo<br/>-Lista list ostatni_wynik<br/>+ustaw_haslo surowe_haslo<br/>+sprawdz_haslo surowe_haslo : bool<br/>+zapisz]
    
    %% MongoDB integration
    MongoDB[Model MongoDB<br/>przy użyciu MongoEngine]
    
    %% Relationships
    URLs --> Interface
    URLs --> WidokGlowny
    Interface --> WidokGlowny
    Auth --> WidokGlowny
    
    WidokGlowny --> FormularzUzytkownika
    WidokGlowny --> Uzytkownik
    
    WidokBlackjack --> LogikaBlackjack
    GlownaLogika --> LogikaBlackjack
    
    LogikaBlackjack --> FormularzAkcjiGry
    FormularzAkcjiGry --> LogikaBlackjack
    
    LogikaBlackjack --> Konfiguracja
    FormularzUzytkownika --> Uzytkownik
    Uzytkownik --> MongoDB
    
    %% Labels for relationships
    WidokGlowny -.->|kieruje do| WidokBlackjack
    WidokBlackjack -.->|używa| LogikaBlackjack
    LogikaBlackjack -.->|korzysta z| Konfiguracja
    FormularzUzytkownika -.->|tworzy| Uzytkownik
    Uzytkownik -.->|zarządza| MongoDB
