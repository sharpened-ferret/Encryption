import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int testShift = 2;
        System.out.println("Hello, world!");
        String encrypted = UniCharShift.CharacterShiftEncryptAndReverse("Hello, world!", testShift);
        System.out.println(encrypted);
        String decrypted = UniCharShift.CharacterShiftDecryptAndReverse(encrypted, testShift);
        System.out.println(decrypted);

    }
}
