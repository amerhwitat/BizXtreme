package io.amerhwitat.bizx;

public final class UnifiedGame {
    public static void main(String[] args) {
        String mode = "default";
        double cash = 10000;
        for (int i = 0; i < args.length; i++) {
            if ("--mode".equals(args[i]) && i + 1 < args.length) mode = args[++i];
            else if ("--cash".equals(args[i]) && i + 1 < args.length) cash = Double.parseDouble(args[++i]);
        }
        System.out.printf("{\"application\":\"BizXtreme Unified Game\",\"mode\":\"%s\",\"runtime\":\"java\",\"cash\":%.2f,\"status\":\"started\"}%n", mode, cash);
    }
}
