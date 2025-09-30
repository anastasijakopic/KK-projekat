int faktorijel(int n) {
    int rezultat = 1;
    for (var i = 1; i <= n; i++) {
        rezultat = rezultat * i;
    }
    return rezultat;
}

String ocijeniBroj(int broj) {
    switch (broj % 2) {
        case 0:
            return "Paran";
        case 1:
            return "Neparan";
        default:
            return "Nepoznato";
    }
}

int zbirDoN(int n) {
    int s = 0;
    int i = 1;
    while (i <= n) {
        s = s + i;
        i = i + 1;
    }
    return s;
}

void obradaPodataka(int broj) {
  try {
    var rezultattt = 100 / broj; 
    print("Rezultat je $rezultattt");
  } on IntegerDivisionByZeroException {
    print("Greška: dijeljenje nulom");
  } finally {
    print("Završena obrada.");
  }
}

