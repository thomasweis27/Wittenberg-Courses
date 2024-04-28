public class HashCodeEx1 {
    private static int m;
    public static void  main(String[] args) {
        m = 34;
        String letters = "ABCD";
        int hashCode = 0;
        //System.out.println(arrSize(str.length()), 2);
        //String[] strArr = {"AB", "AC", "AD", "BC", "BD", "CD", "BA", "CA", "DA", "CB", "BD", "DC"};    //permuteLetters.permuteLetterInStr(letters, 2);
        String[] strArr = {"John 32", "Mathhew 18", "Luke 56", "Jerry 24", "Tom 21", "Kerry 45", "Linus 36", "Caleb 52", "Adam 27", "Philps 30"}; 

        System.out.println("Naive Modulo Hash Code Results: ");
        for (int i=0; i<strArr.length; i++){
            System.out.println(strArr[i]+" = "+ HashCodeGen.naiveXYhashMod(strArr[i], 69));
        }
        System.out.println("Efficient Modulo Hash Code Results: ");
        for (int i=0; i<strArr.length; i++){
            System.out.println(strArr[i]+" = "+ HashCodeGen.efficientXYhashMod(strArr[i], 69, 31));
        }
//        System.out.println("XOR Hash Code Results: ");
//        for (int i=0; i<strArr.length; i++){
//            System.out.println(strArr[i]+" = "+ HashCodeGen.XORhash(strArr[i], 34));
//        }
//        System.out.println("Object Hash Code Results: ");
//        for (int i=0; i<strArr.length; i++){
//            System.out.println(strArr[i]+" = "+ HashCodeGen.ObjectHashCode(strArr[i]));
//        }
    }
}