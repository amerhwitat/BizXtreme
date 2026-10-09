package io.amerhwitat.bizxtreme.api;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import io.amerhwitat.bizxtreme.core.BizXtremeCore;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;
import org.junit.jupiter.api.Test;

/** Verifies the public API against shared, language-neutral contract vectors. */
class BizXtremeApiContractTest {
    private static final Path FIXTURES =
        Path.of("..", "contracts", "fixtures", "bizxtreme-runtime-v1.tsv");

    @Test
    void healthContractsMatchSharedVectors() throws IOException {
        assertTrue(Files.isRegularFile(FIXTURES), "Missing shared fixtures: " + FIXTURES);
        int vectors = 0;
        for (String line : Files.readAllLines(FIXTURES, StandardCharsets.UTF_8)) {
            if (line.isBlank() || line.startsWith("#")) continue;
            String[] fields = line.split("\\t", -1);
            assertEquals(4, fields.length, "Malformed fixture line: " + line);
            Map<String, String> expected = parseExpected(fields[3]);
            Map<String, String> actual;
            switch (fields[0]) {
                case "core-health" -> actual = new BizXtremeCore(fields[1], fields[2]).health();
                case "api-default" -> actual = new BizXtremeApi().health();
                default -> throw new AssertionError("Unknown fixture case: " + fields[0]);
            }
            assertEquals(expected, actual, "Contract vector: " + fields[0]);
            vectors++;
        }
        assertEquals(3, vectors, "Fixture count changed; update the acceptance count intentionally");
    }

    private static Map<String, String> parseExpected(String encoded) {
        return Arrays.stream(encoded.split(";", -1))
            .map(pair -> pair.split("=", 2))
            .collect(Collectors.toMap(pair -> pair[0], pair -> pair[1]));
    }
}
