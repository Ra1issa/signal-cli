clean:
	sudo update-alternatives --set java /usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java
	./gradlew clean
	cd lib && rm  signal-client-java-*.jar
	sudo update-alternatives --set java /usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java
	cd ../libsignal-client && cargo clean
	cd ../libsignal-client/java && ./gradlew clean
	cd ../hecate && cargo clean
	cd ../hecate/java && cargo clean

build_hecate:
		echo "Compiling Hecate"
		mkdir -p ~/Documents/hecate/data
		cd ../hecate/java && cargo build --release && cp target/release/libhecate_jni.so ../../signal-cli/

build_libsignal:
		echo "Compiling libsignal-client"
		sudo update-alternatives --set java /usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java
		cd ../libsignal-client/java && ./gradlew :java:build && cp java/build/libs/signal-client-java-*.jar ../../signal-cli/lib/

build_signacli:
		echo "Compiling signal-cli"
		sudo update-alternatives --set java /usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java
		java -version
		./gradlew build
		./gradlew installDist
		./gradlew distTar

build_all: build_hecate build_hecate build_signacli

copy_setup:
	cd ../hecate/data && cp plat_keys.txt mod_keys.txt user_id.txt mod_pk.txt plat_pk.txt ~/Documents/hecate/data/

run_sender_daemon:
	export LD_LIBRARY_PATH="." && ./gradlew run --args='-u +16172991780 daemon'

run_receiver_daemon:
	export LD_LIBRARY_PATH="." && ./gradlew run --args='-u +16174190472 daemon'

run_sender_daemon_send:
	export LD_LIBRARY_PATH="." && ./gradlew run --args='--dbus send -m "Ill see you on the dark side of the moon" +16174190472'

run_send_nodaemon:
		export LD_LIBRARY_PATH="." && ./gradlew run --args='-u +16172991780 send -m "Ill see you on the dark side of the moon" +16174190472'

run_receive_nodaemon:
		export LD_LIBRARY_PATH="." && ./gradlew run --args='-u +16174190472 receive'

java_versions:
	sudo update-alternatives --remove-all java
	sudo update-alternatives --remove-all jar
	sudo update-alternatives --remove-all jarsigner
	sudo update-alternatives --remove-all javac
	sudo update-alternatives --remove-all javadoc
	sudo update-alternatives --remove-all javap
	sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/java" 10 \
	--slave "/usr/bin/jar"          "jar"           "/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/jar" \
	--slave "/usr/bin/jarsigner"    "jarsigner"     "/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/jarsigner" \
	--slave "/usr/bin/javac"        "javac"         "/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/javac" \
	--slave "/usr/bin/javadoc"      "javadoc"       "/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/javadoc" \
	--slave "/usr/bin/javap"        "javap"         "/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/javap"
	sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/java" 20 \
	--slave "/usr/bin/jar"          "jar"           "/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/jar" \
	--slave "/usr/bin/jarsigner"    "jarsigner"     "/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/jarsigner" \
	--slave "/usr/bin/javac"        "javac"         "/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/javac" \
	--slave "/usr/bin/javadoc"      "javadoc"       "/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/javadoc" \
	--slave "/usr/bin/javap"        "javap"         "/usr/lib/jvm/java-1.17.0-openjdk-amd64/bin/javap"
