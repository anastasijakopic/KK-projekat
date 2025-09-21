void test() {
  int broj = 5;
  try {
    var rezultat = broj + a; // <- 'a' nije definisan
  } catch (e) {
    print(e.toString());
    var poruka = e.toString();
    print(nedefinisanaPromjenljiva); // <- nije definisana
  } finally {
    int broj = 2;
    print(kraj);               // <- nije definisan
    print(josJednaNepoznata);  // <- nije definisana
  }
}
