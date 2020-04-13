import assistant.PersonalAssistant;
import org.hyperskill.hstest.testcase.CheckResult;
import org.hyperskill.hstest.stage.StageTest;
import org.hyperskill.hstest.testcase.TestCase;

import java.util.List;

public class PersonalAssistantTest extends StageTest {

    public PersonalAssistantTest() {
        super(PersonalAssistant.class);
    }

    @Override
    public List<TestCase> generate() {
        return List.of(
            new TestCase<>()
        );
    }

    @Override
    public CheckResult check(String reply, Object clue) {
        return CheckResult.correct();
    }
}
