package tests;

import engine.WebCalculatorApplication;
import org.hyperskill.hstest.dynamic.input.DynamicTestingMethod;
import org.hyperskill.hstest.exception.outcomes.WrongAnswer;
import org.hyperskill.hstest.mocks.web.response.HttpResponse;
import org.hyperskill.hstest.stage.SpringTest;
import org.hyperskill.hstest.testcase.CheckResult;

public class WebCalcTest extends SpringTest {
    public WebCalcTest() {
        super(WebCalculatorApplication.class, 8889);
    }

    static void checkStatusCode(HttpResponse resp, int status) {
        if (resp.getStatusCode() != status) {
            throw new WrongAnswer(
                resp.getRequest().getMethod() + " " +
                    resp.getRequest().getLocalUri() +
                    " should respond with status code " + status + ", " +
                    "responded: " + resp.getStatusCode() + "\n\n" +
                    "Response body:\n\n" + resp.getContent()
            );
        }
    }

    @DynamicTestingMethod
    public CheckResult testGetSum() {
        String url = "/add";

        HttpResponse resp = get(url)
            .addParam("a", "10")
            .addParam("b", "20")
            .send();

        checkStatusCode(resp, 200);

        if (!resp.getContent().equals("30")) {
            return CheckResult.wrong("10 + 20 should return 30");
        }

        return CheckResult.correct();
    }

    @DynamicTestingMethod
    public CheckResult testGetSubtract() {
        String url = "/subtract";

        HttpResponse resp = get(url)
            .addParam("a", "10")
            .addParam("b", "20")
            .send();

        checkStatusCode(resp, 200);

        if (!resp.getContent().equals("-10")) {
            return CheckResult.wrong("10 - 20 should return -10");
        }

        return CheckResult.correct();
    }

    @DynamicTestingMethod
    public CheckResult testGetMult() {
        String url = "/mult";

        HttpResponse resp = get(url)
            .addParam("a", "10")
            .addParam("b", "20")
            .send();

        checkStatusCode(resp, 200);

        if (!resp.getContent().equals("200")) {
            return CheckResult.wrong("10 * 20 should return 200");
        }

        return CheckResult.correct();
    }

    @DynamicTestingMethod
    public CheckResult testUnknownOperation() {
        String url = "/test";

        HttpResponse resp = get(url)
            .addParam("a", "10")
            .addParam("b", "20")
            .send();

        checkStatusCode(resp, 200);

        if (!resp.getContent().equals("Unknown operation")) {
            return CheckResult.wrong("GET /test should return " +
                "\"Unknown operation\"");
        }

        return CheckResult.correct();
    }
}
