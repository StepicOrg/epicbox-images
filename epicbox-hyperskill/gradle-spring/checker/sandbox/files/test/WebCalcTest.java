package tests;

import engine.WebCalculatorApplication;
import org.hyperskill.hstest.dynamic.DynamicTest;
import org.hyperskill.hstest.exception.outcomes.WrongAnswer;
import org.hyperskill.hstest.mocks.web.response.HttpResponse;
import org.hyperskill.hstest.stage.SpringTest;
import org.hyperskill.hstest.testcase.CheckResult;

public class WebCalcTest extends SpringTest {
    public WebCalcTest() {
        super(WebCalculatorApplication.class);
    }

    @DynamicTest
    public CheckResult testGetSum() {
        return CheckResult.correct();
    }
}
