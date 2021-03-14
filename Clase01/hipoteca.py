# hipoteca.py
# Ejercicio de hipoteca
# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%.
# Pidió $500000 al banco y acordó un pago mensual fijo de $2684,11.
# ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
# Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado hasta el momento y el saldo restante.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    if ((saldo - pago_mensual) > 0):
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado += pago_mensual
        if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
            saldo -= pago_extra
            total_pagado += pago_extra
        print(mes, round(total_pagado, 2), round(saldo, 2))
    else:
        total_pagado += saldo
        saldo = 0
        print(mes, round(total_pagado, 2), round(saldo, 2))
print('Total pagado:', round(total_pagado, 1))
print("Meses:", mes)
