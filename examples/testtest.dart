int obradiListu() {
  List<int> brojevi = [1, 2, 3, 4, 5];
  int suma = 0;

  for (var broj in brojevi) {
    if (broj % 2 == 0) {
      suma += broj;
    }
  }

  return suma;
}
