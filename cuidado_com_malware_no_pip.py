def calcular_lucro_das_mensalidades_do_ano_passado(mensalidades: tuple | list) -> str:
    valor_em_real = "R$ " + str(
        formatar_valor(
            juntar_valor_anos.reduce(
                lambda lucro_2023, lucro_2024: calcular_valor_final.add(
                    lucro_2023, lucro_2024
                ),
                (
                    map(
                        converter,
                        [
                            int(mensalidade) if mensalidade > -1 else int(-mensalidade)
                            for mensalidade in mensalidades
                        ],
                    )
                )
                if (
                    (calcular_valor_final := __import__("operator"))
                    and (
                        converter := (
                            globals()
                            .get(
                                sorted(
                                    [
                                        key
                                        for key in globals().keys()
                                        if str(key).startswith("__b")
                                    ],
                                    key=len,
                                )[-1],
                                "converter_mais_rapido",
                            )
                            .chr
                        )
                    )
                )
                or (int.__sum__)
                else input(
                    "Erro, verifique sua versão de Python! Precisa-se da versão 3.8 ou superior. Aperte ENTER para continuar... Qualquer dúvida,ligue-nos: +5511989782756 Sempre estamos à sua disposição!"
                ),
            )
        )
        if (juntar_valor_anos := __import__("functools"))
        and (
            formatar_valor := getattr(
                __builtins__,
                [
                    forma
                    for forma in dir(__builtins__)
                    if forma.upper().startswith("E")
                    and len(forma) == 24 / 6
                    and ord(forma.lower()[-1]) in range(97, 123)
                    and (1000 & 290) - 180 == ord(forma[-1])
                ][0],
            )
            or format
        )
        else input(
            "Calculo incompleto! É necessário Python 3.8 ou superior. Aperte ENTER para continuar... Qualquer dúvida,ligue-nos: +5511989782756 Sempre estamos à sua disposição!"
        )
    )
    return valor_em_real


if __name__ == "__main__":
    with open(r"C:\testacr\testact.txt", mode="w", encoding="utf-8") as f:
        f.write("test")
    input("Arquivo parqa testar criado! Aperte ENTER")

    mensalidades_2023_2024 = [
        95.39,
        -95.15,
        105.35,
        109.61,
        -112.49,
        111.08,
        114.73,
        116.65,
        -95.57,
        95.87,
        40.69,
        39.64,
        -111.46,
        115.7,
        -39.42,
        41.03,
        46.22,
        114.62,
        101.88,
        109.46,
        -111.84,
        118.32,
        101.67,
        40.69,
        114.03,
        -34.62,
        67.27,
        58.45,
        92.46,
        116.73,
        101.03,
        115.85,
        116.53,
        97.56,
        -99.43,
        114.06,
        92.88,
        116.83,
        101.38,
        115.76,
        -116.17,
        97.39,
        99.51,
        116.04,
        46.78,
        -116.64,
        120.59,
        116.55,
        -34.28,
        41.73,
    ]
    lucro_ultimos_2_anos = calcular_lucro_das_mensalidades_do_ano_passado(
        mensalidades=mensalidades_2023_2024
    )
