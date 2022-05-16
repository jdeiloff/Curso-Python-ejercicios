# hipoteca.py ejercicio 1.8

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_extra = 1000
    elif pago_mensual > saldo:
        pago_mensual = saldo * (1+tasa/12)
    else:
        pago_extra = 0    
    saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
    total_pagado = total_pagado + pago_mensual + pago_extra
    print(f"Mes = {mes} Pagado = ${total_pagado} Restan = ${saldo}")




print(f"Se pagaron en total: ${round(total_pagado, 2)} en {mes} meses")