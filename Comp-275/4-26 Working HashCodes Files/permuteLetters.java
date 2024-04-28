public class permuteLetters{
    public static String[] permuteLetterInStr(String str, int r){
        String [] strArr = new String[arrSize(str.length(),r)];
        int k=0;
        for (int i=0; i<str.length(); i++){
            for (int j=i+1; j<str.length(); j++){
                strArr[k]= str.charAt(i)+ "" + str.charAt(j);
                k++;
            }
        }

        for (int i=0; i<str.length(); i++){
            for (int j=i+1; j<str.length(); j++){
                strArr[k]= str.charAt(j)+ "" + str.charAt(i);
                k++;
            }
        }
    
        return strArr;
    }

    public static int arrSize(int n, int r){
        int fact=1;
        int temp = 0;
        for(int k=1; k<=n; k++)
            fact*=k;

        temp=fact;
        for(int k=1; k<=n; k++)
            fact*=k;

        return temp/fact;

    }
}