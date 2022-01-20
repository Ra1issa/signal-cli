./gradlew clean

echo "Compiling signal-cli"
cd ..
sudo update-alternatives --set java /usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java
java -version
./gradlew build
./gradlew installDist
./gradlew distTar
