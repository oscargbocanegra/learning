import org.junit.Test;
import static org.junit.Assert.assertTrue;

public class JvmArgumentTest {

    @Test
    public void testJvmArgument() {
        String jvmArgs = System.getProperty("sun.java.command");
        assertTrue("JVM argument --add-opens is not applied", jvmArgs.contains("--add-opens java.base/java.util=ALL-UNNAMED"));
    }
}