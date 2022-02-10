# only linewalks members can access it.
git clone https://github.com/linewalks/clue-connect.git
mv clue-connect/clue_pb2.py ./pyclue/pb
mv clue-connect/clue_pb2_grpc.py ./pyclue/pb
rm -rf clue-connect
