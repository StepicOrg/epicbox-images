import calculator.Main;
import org.hyperskill.hstest.stage.StageTest;
import org.hyperskill.hstest.testcase.CheckResult;
import org.hyperskill.hstest.testcase.TestCase;
import org.hyperskill.hstest.testing.TestedProgram;

import static org.hyperskill.hstest.testing.expect.Expectation.expect;

import java.util.Arrays;
import java.util.List;

public class Test extends StageTest<String> {

    @Override
    public List<TestCase<String>> generate() {
        return Arrays.asList(
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of one-digit positive numbers
                    String output = main.execute("0 1").trim();
                    return new CheckResult(output.equals("1"), "Your program cannot sum two positive single digits");
                }),
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of one-digit positive numbers
                    String output = main.execute("1 0").trim();
                    return new CheckResult(output.equals("1"), "Your program cannot sum two positive single digits");
                }),
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of one-digit positive numbers
                    String output = main.execute("5 7").trim();
                    return new CheckResult(output.equals("12"), "Your program cannot sum two positive single digits");
                }),
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of three-digit numbers
                    String output = main.execute("100 123").trim();
                    return new CheckResult(output.equals("223"), "Your program cannot sum two three-digit number");
                }),
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of positive and negative number
                    String output = main.execute("-1 5").trim();
                    return new CheckResult(output.equals("4"), "Your program cannot sum negative and positive number");
                }),
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of positive and negative number
                    String output = main.execute("5 -2").trim();
                    return new CheckResult(output.equals("3"), "Your program cannot sum positive and negative number");
                }),
                new TestCase<String>().setDynamicTesting(() -> {
                    TestedProgram main = new TestedProgram(Main.class);
                    main.start();

                    // sum of two negative numbers
                    String output = main.execute("-300 -400").trim();
                    return new CheckResult(output.equals("-700"), "Your program cannot sum two negative numbers");
                })
        );
    }
}
