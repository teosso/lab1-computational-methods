import os

# Модель: Метод простої ітерації (5 семестр)
# Автор: Ковальжі Сергій, група АІ-235

def simple_iteration(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        # Приклад простої функції x_new = (x^2 + 2) / 3
        x_new = (x**2 + 2) / 3
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return None, max_iter

if __name__ == "__main__":
    # Зчитуємо змінні середовища, які передасть Docker
    student = os.getenv("STUDENT_NAME", "Ковальжі Сергій")
    group = os.getenv("GROUP", "АІ-235")
    mode = os.getenv("MODE", "comfort") # або eco залежно від твого номера

    print("-" * 40)
    print("🚀 Запуск сервісу в Docker контейнері")
    print(f"Модель: Метод простої ітерації")
    print(f"Студент: {student}")
    print(f"Група: {group}")
    print(f"Режим (MODE): {mode.upper()}")
    print("-" * 40)

    print("Виконання розрахунків...")
    result, iters = simple_iteration(x0=0.5)
    print(f"Результат: Корінь знайдено за {iters} ітерацій. Занчення = {result:.5f}")
    print("-" * 40)