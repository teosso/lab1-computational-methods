# Модель: Метод Ньютона (5 семестр)
# Автор: Ковальжі Сергій, група АІ-235

def newton_method(func, func_deriv, x0, tol=1e-5, max_iter=100):
    """
    Знаходження кореня рівняння методом Ньютона.
    """
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = func_deriv(x)
        
        if dfx == 0:
            print("Похідна дорівнює нулю. Зупинка алгоритму.")
            return None
            
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            print(f"Корінь знайдено за {i+1} ітерацій: {x_new}")
            return x_new
            
        x = x_new
        
    print("Перевищено ліміт ітерацій.")
    return None

if __name__ == "__main__":
    # Приклад: знаходження кореня для рівняння x^2 - 4 = 0
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    
    print("Запуск моделі: Метод Ньютона")
    newton_method(f, df, x0=5.0)