import assistant.PersonalAssistant;
import org.hyperskill.hstest.v3.testcase.CheckResult;
import org.hyperskill.hstest.v3.stage.MainMethodTest;
import org.hyperskill.hstest.v3.testcase.TestCase;

import java.util.List;


public class PersonalAssistantTest extends MainMethodTest {

    public PersonalAssistantTest() throws Exception {
        super(PersonalAssistant.class);
    }

    @Override
    public List<TestCase> generateTestCases() {
        return List.of(
            new TestCase<>()
        );
    }

    @Override
    public CheckResult check(String reply, Object clue) {
        return new CheckResult(reply.trim().matches(".+\\n.+\\d+.+\\n?"));
    }
}
