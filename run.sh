sender_phone=+16172991780
message=Hello
receiver_phone_me=+18572345222
receiver_phone=+16174190472
nic=+18573165383

export LD_LIBRARY_PATH="/home/petitpenguin/Documents/Github/hecate/java/target/debug/"

./gradlew run --args='-u +16174190472 send -m "Ill see you on the dark side of the moon" +16172991780'
./gradlew run --args='-u +16172991780 receive'

# ./gradlew run --args='-u +16174190472 register --captcha '
# ./gradlew run --args='-a +16174190472 verify'
