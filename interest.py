""" Voy a hacer unas cuentas que me permitan saber cuanto dinero
 pagaria si voy pagando una cuota inventada por mi.
 no voy a evaluar errores ni cuando el usuario ingresa algo que no es un numero,
 voy a usar recursividad."""



def calculate_price(fees, price_product, monto_a_pagar):
    if fees == 0:
        return round(monto_a_pagar, 2)
    else:
        surcharge_anual = calculate_surcharge(price_product)
        price = price_product + surcharge_anual
        paid = price / fees
        monto_a_pagar = monto_a_pagar + paid
        return calculate_price(
            fees = fees-1,
            price_product = price-paid,
            monto_a_pagar= monto_a_pagar
            )

def calculate_amount_variable(fees,  price_product):
    monto_a_pagar = 0
    paid = price_product / fees
    monto = monto_a_pagar + paid
    monto = calculate_price(
        fees = fees-1,
        price_product = price_product - paid,
        monto_a_pagar= monto
        )
    return monto

def calculate_surcharge(price_product):
    #Porcentaje basado en que el banco hace un interes de 100% anual en 12 cuotas es el recargo mensual.
    return round(price_product * 10 /120, 10)

def calculate_amount_traditional(fees,price_product, surcharge):
    amount = price_product + fees * surcharge
    return round(amount, 2)

def calculate_quantity_money(fees,price_product):
    #El interes que realiza el banco es de un 100% anual.
    surcharge = calculate_surcharge(price_product)
    amount_traditional = calculate_amount_traditional(fees,price_product,surcharge)
    amount_variable = calculate_amount_variable(fees, price_product)
    return f"tu monto tradicional es de {amount_traditional} y tu monto variable es de {amount_variable}"

def how_many_installments():
    fees = int(input("¿en cuántas cuotas lo quieres hacer? (debe ser un número entero): "))
    if isinstance(fees, int):
        return fees
    else:
        how_many_installments()

def tell_me_your_price():
    price_product = float(input("Dime el precio (debe ser un número) de tu producto: "))
    if isinstance(price_product, float):
        return price_product
    else:
        tell_me_your_price()


def buy_product():
    price_product = tell_me_your_price()
    fees = how_many_installments()
    quantity_money = calculate_quantity_money(fees,price_product)
    return print(quantity_money)

buy_product()