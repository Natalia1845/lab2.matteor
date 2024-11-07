# Данні для першого пакету акцій
profit_1_spriyatlivo = 40000  # Сприятлива ситуація
profit_1_mensh_spriyatlivo = 10000  # Менш сприятлива ситуація
probability_1_spriyatlivo = 0.5
probability_1_mensh_spriyatlivo = 0.5

# Данні для другого пакету акцій
profit_2_spriyatlivo = 30000  # Сприятлива ситуація
profit_2_mensh_spriyatlivo = 5000  # Несприятлива ситуація
probability_2_spriyatlivo = 0.5
probability_2_mensh_spriyatlivo = 0.5

# Розрахунок очікуваного прибутку для першого пакету акцій
expected_profit_1 = (profit_1_spriyatlivo * probability_1_spriyatlivo) + (profit_1_mensh_spriyatlivo * probability_1_mensh_spriyatlivo)

# Розрахунок очікуваного прибутку для другого пакету акцій
expected_profit_2 = (profit_2_spriyatlivo * probability_2_spriyatlivo) + (profit_2_mensh_spriyatlivo * probability_2_mensh_spriyatlivo)

# Виведення результатів
print(f"Очікуваний прибуток для першого пакету акцій: {expected_profit_1}")
print(f"Очікуваний прибуток для другого пакету акцій: {expected_profit_2}")

# Оптимальне рішення
if expected_profit_1 > expected_profit_2:
    print("Оптимальне рішення: вибір першого пакету акцій.")
else:
    print("Оптимальне рішення: вибір другого пакету акцій.")
