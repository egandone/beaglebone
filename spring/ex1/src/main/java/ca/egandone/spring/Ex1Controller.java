package ca.egandone.spring;

import org.springframework.web.bind.annotation.*;

@RestController
public class Ex1Controller {

	@RequestMapping("/")
	public String index() {
		return "the index page";
	}
}
