def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    radek, sloupec = cilova_pozice
    akt_radek, akt_sloupec = aktualni_pozice

    # 1. KROK: Je cílová pozice na šachovnici? (řádky i sloupce 1 až 8)
    if radek < 1 or radek > 8 or sloupec < 1 or sloupec > 8:
        return False

    # 2. KROK: Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. KROK: Pohyb podle typu figury
    rozdil_radku = abs(radek - akt_radek)
    rozdil_sloupcu = abs(sloupec - akt_sloupec)

    if typ == "král":
        # Max. 1 pole v jakémkoliv směru, ale musí se pohnout (ne zůstat na místě)
        return rozdil_radku <= 1 and rozdil_sloupcu <= 1 and (rozdil_radku + rozdil_sloupcu) > 0

    elif typ == "jezdec":
        # Tvar L: 2+1 nebo 1+2
        return (rozdil_radku == 2 and rozdil_sloupcu == 1) or \
               (rozdil_radku == 1 and rozdil_sloupcu == 2)

    return False
