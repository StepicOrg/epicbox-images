import assistant.PersonalAssistant;
import org.hyperskill.hstest.v1.CheckResult;
import org.hyperskill.hstest.v1.MainMethodTest;
import org.hyperskill.hstest.v1.TestCase;


public class PersonalAssistantTest extends MainMethodTest {

    public PersonalAssistantTest() throws Exception {
        super(PersonalAssistant.class);
    }

    @Override
    public TestCase[] generateTestCases() {
        return new TestCase[] {
            new TestCase<>()
        };
    }

    @Override
    public CheckResult check(String reply, Object clue) {
        return new CheckResult(reply.trim().matches(".+\\n.+\\d+.+\\n?"));
    }
}
