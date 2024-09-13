package security;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.security.spec.KeySpec;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

@Component
public class EncryptionUtil {

    private static final int ITERATION_COUNT = 6553;
    private static final int KEY_LENGTH = 256;

    /**
     * Encrypts the payload using AES encryption with CBC mode and PKCS5Padding.
     *
     * @param payload     List of strings to encrypt
     * @param privateKey  AES encryption key as a Base64-encoded string
     * @param salt        Salt used for PBKDF2 key derivation
     * @return Encrypted payload as Base64-encoded string
     */
    public String encryptPayload(List<String> payload, String privateKey, String salt) {
        try {
            byte[] iv = new byte[16];
            SecureRandom secureRandom = new SecureRandom();
            secureRandom.nextBytes(iv);
            IvParameterSpec ivspec = new IvParameterSpec(iv);

            SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
            KeySpec spec = new PBEKeySpec(privateKey.toCharArray(), salt.getBytes(), ITERATION_COUNT, KEY_LENGTH);
            SecretKey tmp = factory.generateSecret(spec);
            SecretKeySpec secretKeySpec = new SecretKeySpec(tmp.getEncoded(), "AES");

            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec, ivspec);

            StringBuilder stringBuilder = new StringBuilder();
            for (String s : payload) {
                stringBuilder.append(s).append(", ");
            }
            byte[] payloadBytes = stringBuilder.toString().getBytes();

            byte[] encryptedBytes = cipher.doFinal(payloadBytes);

            byte[] combined = new byte[iv.length + encryptedBytes.length];
            System.arraycopy(iv, 0, combined, 0, iv.length);
            System.arraycopy(encryptedBytes, 0, combined, iv.length, encryptedBytes.length);
            return Base64.getEncoder().encodeToString(combined);
        } catch (Exception e) {
            throw new RuntimeException("Error encrypting payload", e);
        }
    }

    /**
     * Decrypts the encrypted payload using AES decryption with CBC mode and PKCS5Padding.
     *
     * @param encryptedPayload Encrypted payload as Base64-encoded string
     * @param privateKey       AES decryption key as a Base64-encoded string
     * @param salt             Salt used for PBKDF2 key derivation
     * @return Decrypted payload as List of strings
     */
    public List<String> decryptPayload(String encryptedPayload, String privateKey, String salt) {
        try {
            byte[] combined = Base64.getDecoder().decode(encryptedPayload);
            byte[] iv = Arrays.copyOfRange(combined, 0, 16);
            byte[] encryptedBytes = Arrays.copyOfRange(combined, 16, combined.length);

            SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
            KeySpec spec = new PBEKeySpec(privateKey.toCharArray(), salt.getBytes(), ITERATION_COUNT, KEY_LENGTH);
            SecretKey tmp = factory.generateSecret(spec);
            SecretKeySpec secretKeySpec = new SecretKeySpec(tmp.getEncoded(), "AES");

            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
            cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, new IvParameterSpec(iv));

            byte[] decryptedBytes = cipher.doFinal(encryptedBytes);
            String decryptedString = new String(decryptedBytes, StandardCharsets.UTF_8);

            String[] items = decryptedString.split(", ");
            return List.of(items);
        } catch (Exception e) {
            throw new RuntimeException("Error decrypting payload", e);
        }
    }
}
