mkdir -p ~/Documents/hecate/data

cd ../../hecate/java
cargo build --release
cp target/release/libhecate_jni.so ../../signal-cli/
