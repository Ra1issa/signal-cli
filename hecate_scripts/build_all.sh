mkdir -p ~/Documents/hecate/data

cd ../../hecate/java
cargo build --release
cp target/release/libhecate_jni.so ../../signal-cli/

echo "Compiling libsignal-client"
cd ../../libsignal-client/java
sudo update-alternatives --set java /usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java
java -version
./gradlew :java:build
cp java/build/libs/signal-client-java-*.jar ../../signal-cli/lib/


echo "Compiling signal-cli"
cd ../../signal-cli
sudo update-alternatives --set java /usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java
java -version
./gradlew build
./gradlew installDist
./gradlew distTar
