class Main {
  public static void main(String[] args) {
    String ct = "110010111001110011110011110111111001110000110100110001110101110111110011110001110001111000110000110100110101111001110100110010110001110111111000110000110110110010110100110101110101111000111001110001110001110001110101110110111000110011111001110011111001110110110000110101110100110010111001110000110110110011110001110010110110110010110101110000110011110111110100110110110011110010111000110101110100";

    String pt ="";
    for (int i = 0; i < ct.length(); i +=6){
      int charCode = Integer.parseInt(ct.substring(i, i+6), 2);
      pt = pt + new Character((char)charCode).toString();
    }

    System.out.println("flag{" + pt + "}");
  }
}