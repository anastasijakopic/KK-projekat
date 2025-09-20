void obradaPodataka(int broj) {
  try {
    int rezultat = 100 ~/ broj;
    print("Rezultat je $rezultat");
  } on IntegerDivisionByZeroException {
    print("Greška: dijeljenje nulom");
  } finally {
    print("Završena obrada.");
  }
}