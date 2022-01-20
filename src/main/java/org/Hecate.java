package org;

public class Hecate{
    // This declares that the static `hello` method will be provided
    // a native library.
    public static native char[] inject_mfrank_jni(String input);
    public static native String remove_mfrank_jni(char[] input);
    static {
        // This actually loads the shared object that we'll be creating.
        // The actual location of the .so or .dll may differ based on your
        // platform.
        System.loadLibrary("hecate_jni");
    }
}
