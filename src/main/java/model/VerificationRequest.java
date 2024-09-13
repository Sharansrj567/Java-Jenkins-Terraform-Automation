package model;

import java.util.List;

public class VerificationRequest {

	private String encryptedPayload;
    private List<String> functions;

	public String getEncryptedPayload() {
		return encryptedPayload;
	}
	public void setEncryptedPayload(String encryptedPayload) {
		this.encryptedPayload = encryptedPayload;
	}
	public List<String> getFunctions() {
		return functions;
	}
	public void setFunctions(List<String> functions) {
		this.functions = functions;
	}
}
