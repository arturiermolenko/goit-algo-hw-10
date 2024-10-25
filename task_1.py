import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Визначення змінних
# A - "Лимонад"
# B - "Фруктовий сік"
A = pulp.LpVariable("A", lowBound=0, cat="Integer")  # Кількість продукту А
B = pulp.LpVariable("B", lowBound=0, cat="Integer")  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += pulp.lpSum([A, B]), "Total_Production"

# Додавання обмежень
model += (2 * A + B <= 100, "Water")
model += (A <= 50, "Sugar")
model += (A <= 30, "Lemon")
model += (2 * B <= 40, "Fruit_Puree")

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Кількість виробленого лимонаду: {A.varValue}")
print(f"Кількість виробленого фруктового соку: {B.varValue}")
print(f"Загальна кількість вироблених продуктів: {A.varValue + B.varValue}")
print("Статус моделі:", pulp.LpStatus[model.status])

