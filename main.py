# Модель: Метод простої ітерації (5 семестр)
# Автор: Ковальжі Сергій, група АІ-235

from flask import Flask, request, jsonify

app = Flask(__name__)

def simple_iteration(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = (x**2 + 2) / 3
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    return None, max_iter

@app.route('/calculate', methods=['GET'])
def calculate():
    x0 = float(request.args.get('x', 0.5))
    result, iters = simple_iteration(x0)
    
    return jsonify({
        "status": "success",
        "model": "Method of simple iteration",
        "developer": "Sergey Kovalzhi",
        "group": "AI-235",
        "input_x0": x0,
        "result_root": round(result, 5) if result else None,
        "iterations": iters
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)