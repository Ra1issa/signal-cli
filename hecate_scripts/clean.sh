cd ..
sudo update-alternatives --set java /usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java
./gradlew clean
cd lib
rm  signal-client-java-*.jar

cd ../../libsignal-client
sudo update-alternatives --set java /usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java
cargo clean
cd java
./gradlew clean

cd ../../hecate
cargo clean
cd java
cargo clean
