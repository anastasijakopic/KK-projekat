void proveri() {
  int broj = 10;
  var rezultat = broj * faktor; // <- faktor (nije definisan)

  if (rezultat > prag) {        // <- prag (nije definisan)
    print("Prešao prag!");
  }

  for (var i in niz) {          // <- niz (nije definisan)
    print(i);
  }

  var zbir = a + b;             // <- a, b (nisu definisani)
}
