# only linewalks members can access it.
git clone https://khclab.kakaohealthcare.local/dp/clue-connect.git
mv clue-connect/clue_pb2.py ./pyclue/pb
mv clue-connect/clue_pb2_grpc.py ./pyclue/pb
rm -rf clue-connect
