package com.sharansrj567;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication(scanBasePackages = {
	    "com.sharansrj567",
	    "controller",
	    "service",
	    "model",
	    "security",
	})
	@EntityScan(basePackages = "model")
public class CodeSanitizeApplication {

	public static void main(String[] args) {
		SpringApplication.run(CodeSanitizeApplication.class, args);
	}

}
