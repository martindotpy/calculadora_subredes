# Recuerda instalar las dependencias con el siguiente comando
# En Windows:
# pip install tabulate numpy -q
# En SO basados en Unix:
# pip3 install tabulate numpy -q

import numpy as np
import tabulate as tb

ip = [192, 168, 10, 0]
mask = [255, 255, 255, 0]
cantidad_de_subredes = (
    4  # Recuerda que la cantidad de subredes debe ser una potencia de 2
)

# Calculate the number of bits for the mask
ip.append(
    sum([f"{mask[i]:08b}".count("1") for i in range(len(mask))]),
)

# N of bits for subnets
bits_for_subnets = np.log2(cantidad_de_subredes)

if bits_for_subnets % 1:
    raise ValueError("El número de subredes debe ser una potencia de 2")

bits_for_subnets = bits_for_subnets.astype(int)

# New mask
new_mask = ip[4] + bits_for_subnets
hosts = 2 ** (32 - new_mask) - 2

# Create the new subnets
new_subnets = []
for i in range(2**bits_for_subnets):
    new_subnets.append(
        f"{i:0{bits_for_subnets}b}{'0' * (8 - bits_for_subnets)}"
    )

# Subnet mask
sub_mask = [
    255,
    255,
    255,
    sum([
        int(
            f"{2**bits_for_subnets - 1:0{bits_for_subnets}b}{'0' * (8 - bits_for_subnets)}"[
                i
            ]
        )
        * 2 ** (7 - i)
        for i in range(8)
    ]),
]

new_subnets = [
    [
        ip[0],
        ip[1],
        ip[2],
        sum([int(subnet[i]) * 2 ** (7 - i) for i in range(8)]),
    ]
    for subnet in new_subnets
]

aux_new_subnets = new_subnets.copy()
new_subnets = []

for i in range(len(aux_new_subnets)):
    first_host = aux_new_subnets[i][-1] + 1
    last_host = aux_new_subnets[i][-1] + hosts
    broadcast = aux_new_subnets[i][-1] + hosts + 1

    new_subnets.append([
        f"Subred {i + 1}",
        hosts,
        f"{'.'.join(map(str, aux_new_subnets[i]))}/{new_mask}",
        f"{'.'.join(map(str, sub_mask))}",
        f"{'.'.join(map(str, aux_new_subnets[i][:3] + [first_host]))}",
        f"{'.'.join(map(str, aux_new_subnets[i][:3] + [last_host]))}",
        f"{'.'.join(map(str, aux_new_subnets[i][:3] + [broadcast]))}",
    ])

table = tb.tabulate(
    new_subnets,
    headers=[
        "N° de subred",
        "N° de Hosts",
        "IP de la red",
        "Máscara",
        "Primer Host",
        "Último Host",
        "Broadcast",
    ],
    tablefmt="pretty",
)

print(f"""
Dirección IP: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}/{ip[4]}  
Máscara de red: {mask[0]}.{mask[1]}.{mask[2]}.{mask[3]}

Requerimientos: {cantidad_de_subredes} subredes

{table}""")
