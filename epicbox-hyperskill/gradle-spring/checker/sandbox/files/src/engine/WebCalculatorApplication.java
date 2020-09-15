package engine;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
class ArithmeticRestController {
    @GetMapping("/{operation}")
    public String calculate(@PathVariable String operation,
                            @RequestParam int a,
                            @RequestParam int b) {

        switch (operation) {
            case "add":
                return String.valueOf(a + b);
            case "subtract":
                return String.valueOf(a - b);
            case "mult":
                return String.valueOf(a * b);
            default:
                return "Unknown operation";
        }
    }
}

@SpringBootApplication
public class WebCalculatorApplication {
    public static void main(String[] args) {
        SpringApplication.run(WebCalculatorApplication.class, args);
    }
}
