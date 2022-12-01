# only linewalks members can access it.
git clone REPO_URL
mv clue-connect/clue_pb2.py ./pyclue/pb
mv clue-connect/clue_pb2_grpc.py ./pyclue/pb
rm -rf clue-connect
