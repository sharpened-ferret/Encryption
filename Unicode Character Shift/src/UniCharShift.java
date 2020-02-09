/**
 * This class contains a few simple cipher methods
 * An encryption version is listed first for each technique, followed by the corresponding decryptor
 *
 * File Created: 09/02/2020
 *
 * @author Neil Woodhouse
 * @Version 1.0
 */
public class UniCharShift {

    /**
     * This function does a simple character shift cipher on the input text and returns the resultant string
     * @param inputString The text string to be encrypted
     * @param shiftDistance The size of character shift required (+ or -)
     * @return The encrypted string
     */
    public static String CharacterShiftEncrypt(String inputString, int shiftDistance) {
        String outputString = "";
        char[] inputText = inputString.toCharArray();
        for (char character : inputText) {
            int unicodeValue = character;
            char shiftedChar = (char)(unicodeValue + shiftDistance);
            outputString+=shiftedChar;
        }
        return outputString;
    }

    /**
     * This function reverses a simple character shift cipher and returns the resultant string
     * @param inputString The text string to be encrypted
     * @param shiftDistance The size of character shift required (+ or -)
     * @return The encrypted string
     */
    public static String CharacterShiftDecrypt(String inputString, int shiftDistance) {
        String outputString = "";
        char[] inputText = inputString.toCharArray();
        for (char character : inputText) {
            int unicodeValue = character;
            char shiftedChar = (char)(unicodeValue - shiftDistance);
            outputString+=shiftedChar;
        }
        return outputString;
    }



    /**
     * This function does a simple character shift cipher and reverses the character order
     * It returns the reversed and enciphered string
     * @param inputString The text string to be encrypted
     * @param shiftDistance The size of character shift required (+ or -)
     * @return The encrypted string
     */
    public static String CharacterShiftEncryptAndReverse(String inputString, int shiftDistance) {
        String outputString = "";
        char[] inputText = inputString.toCharArray();
        for (int i = inputText.length-1; i>=0; i--) {
            int unicodeValue = inputText[i];
            char shiftedChar = (char)(unicodeValue + shiftDistance);
            outputString+=shiftedChar;
        }
        return outputString;
    }

    /**
     * This function deciphers an input string that has been encrypted by character shifting and reversing the character
     * order. It returns the deciphered string
     * @param inputString The text string to be encrypted
     * @param shiftDistance The size of character shift required (+ or -)
     * @return The encrypted string
     */
    public static String CharacterShiftDecryptAndReverse(String inputString, int shiftDistance) {
        String outputString = "";
        char[] inputText = inputString.toCharArray();
        for (int i = inputText.length-1; i>0; i--) {
            int unicodeValue = inputText[i];
            char shiftedChar = (char)(unicodeValue - shiftDistance);
            outputString+=shiftedChar;
        }
        return outputString;
    }


}
