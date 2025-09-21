void obradaPodataka(int broj) {
  try {
    var rezultat = 100 / broj; 
    print("Rezultat je $rezultat");
  } on IntegerDivisionByZeroException {
    print("Greška: dijeljenje nulom");
  } finally {
    print("Završena obrada.");
  }
}
