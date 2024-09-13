package controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import model.VerificationRequest;
import service.VerificationService;

@RestController
@CrossOrigin(origins = "*")
public class MainController {
	
	@Autowired
	private VerificationService verificationService;
	
	@GetMapping("/get-data")
	public Map<String, Object> getData(){
		return verificationService.generateEncryptedDataset();
	}

	@PostMapping("/verify-functions")
	public Map<String, Object> verifyFunctions(@RequestBody VerificationRequest request){
		return verificationService.verifyFunctions(request);
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
