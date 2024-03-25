def sing_alouette(n, lapart):
    print("Chantez \"Alouette, gentille alouette, alouette, je te plumerai.\"")

    for i in range(n):
        print(f"Chantez \"Je te plumerai {lapart[i]}. Je te plumerai {lapart[i]}\"")

        for j in range(i, -1, -1):
            print(f"Chantez \"Et {lapart[j]}! Et {lapart[j]}!\"")

    print("Chantez \"Alouette! Alouette! Aaaaaa...\"")
    print("Chantez \"... alouette, gentille alouette, alouette, je te plumerai.\"")


n = 3
lapart = ["la tête", "le bec", "les ailes"]

sing_alouette(n, lapart)
