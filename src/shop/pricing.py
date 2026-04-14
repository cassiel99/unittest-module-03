def final_price_cents(
    base_cents: int, discount_percent: int = 0, tax_percent: int = 20
) -> int:
    """
    Контракт:
    - base_cents: int, >= 0
    - discount_percent: int, 0..100
    - tax_percent: int, 0..100
    Логика:
    - discount применяется к base
    - затем добавляется tax
    - результат округляется до целых центов (int)
    """
    if not isinstance(base_cents, int) or not isinstance(discount_percent, int) or not isinstance(tax_percent, int):
        raise TypeError("all arguments must be int")
    if base_cents < 0:
        raise ValueError("base_cents must be >= 0")
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")
    if not (0 <= tax_percent <= 100):
        raise ValueError("tax_percent must be between 0 and 100")

    after_discount = base_cents * (1 - discount_percent / 100)
    after_tax = after_discount * (1 + tax_percent / 100)
    return int(after_tax)
