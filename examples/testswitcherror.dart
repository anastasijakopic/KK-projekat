String test() {
  switch (broj) { // <- 'broj' nije definisan
    case 1:
      return "jedan";
    case 2:
      return "dva";
    default:
      return "nepoznat";
  }
}
