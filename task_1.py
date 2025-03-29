from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        current_date = datetime.today().date()
        user_date = datetime.strptime(date, "%Y-%m-%d").date()
        return (user_date - current_date).days
    except ValueError:
        print("Помилка: неправильний формат дати. Використовуйте YYYY-MM-DD.")
        return None

def main():
   print( get_days_from_today("2024-07-31"))
    
if __name__=="__main__":
    main()